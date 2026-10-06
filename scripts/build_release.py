#!/usr/bin/env python3
"""Validate package structure and build portable ZIPs; never install or publish."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'plugins' / 'email-assistant'
EXPECTED_SKILLS = {
    'manage-email-assistant', 'setup-email', 'email-triage',
    'pocket-meeting-summary', 'pocket-meeting-follow-up',
    'pocket-summary-to-wrike', 'wrike-tasks', 'pocket-meeting-context',
    'requested-actions', 'sync-wrike-completion',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    portable = read_json(PACKAGE / 'plugin.json')
    compatibility = read_json(PACKAGE / '.codex-plugin' / 'plugin.json')
    marketplace = read_json(ROOT / '.agents' / 'plugins' / 'marketplace.json')
    version = portable['version']
    require(re.fullmatch(r'\d+\.\d+\.\d+', version), 'Invalid release version')
    require(portable['name'] == 'email-assistant', 'Unexpected plugin identity')
    require(portable['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Unexpected schema declaration')
    for field in ('name', 'version', 'description', 'author', 'keywords'):
        require(portable[field] == compatibility[field], f'Manifest mismatch: {field}')
    interface = portable['extensions']['com.openai']['interface']
    require(interface == compatibility['interface'], 'Manifest interface mismatch')
    require(len(interface['displayName']) <= 30, 'Display name too long')
    require(len(interface['shortDescription']) <= 30, 'Subtitle too long')
    prompts = interface['defaultPrompt']
    require(len(prompts) <= 3 and all(len(p) <= 128 for p in prompts), 'Invalid starter prompts')
    require(compatibility['skills'] == './skills/', 'Invalid compatibility skill path')
    entries = [p for p in marketplace['plugins'] if p['name'] == portable['name']]
    require(len(entries) == 1, 'Marketplace must have exactly one matching plugin')
    require((ROOT / entries[0]['source']['path']).resolve() == PACKAGE.resolve(), 'Marketplace target mismatch')
    actual = {p.name for p in (PACKAGE / 'skills').iterdir() if p.is_dir()}
    require(actual == EXPECTED_SKILLS, f'Unexpected skills: {actual}')
    for name in sorted(actual):
        skill = PACKAGE / 'skills' / name / 'SKILL.md'
        content = skill.read_text(encoding='utf-8')
        require(content.startswith('---\n'), f'Missing frontmatter: {name}')
        fields = content.split('---', 2)[1]
        require(re.search(r'^name:\s*' + re.escape(name) + r'\s*$', fields, re.M), f'Skill name mismatch: {name}')
        require(re.search(r'^description:\s*\S', fields, re.M), f'Missing description: {name}')
        require('TODO' not in content, f'Unfinished scaffold: {name}')
    for field in ('logo', 'composerIcon'):
        icon = PACKAGE / interface[field]
        require(icon.is_file() and icon.resolve().is_relative_to(PACKAGE.resolve()), f'Invalid asset: {field}')
        if icon.suffix == '.svg':
            attributes = ET.parse(icon).getroot().attrib
            require(attributes.get('width') == attributes.get('height') and int(attributes['width']) >= 48, 'Invalid SVG dimensions')
    links = 0
    files = []
    for path in sorted(PACKAGE.rglob('*')):
        require(not path.is_symlink(), f'Symlink prohibited: {path.relative_to(ROOT)}')
        if not path.is_file():
            continue
        require(path.name != '.env' and not path.name.startswith('.env.'), 'Environment file in plugin')
        require(path.suffix not in {'.pem', '.key', '.pyc'}, 'Key/cache file in plugin')
        files.append(path)
        if path.suffix in {'.md', '.yaml', '.json', '.svg'}:
            content = path.read_text(encoding='utf-8')
            require('/Users/' not in content and '/home/' not in content, f'Nonportable path: {path.relative_to(ROOT)}')
            for link in re.findall(r'\]\(([^)]+)\)', content):
                if '://' in link or link.startswith('#'):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                require(target.is_file() and target.is_relative_to(PACKAGE.resolve()), f'Broken or escaping link: {path.relative_to(ROOT)} -> {link}')
                links += 1
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    guide_names = ('ADMIN-GUIDE.md', 'RELEASE-NOTES.md', 'ROLLOUT-TRACKER.csv', 'START-HERE.md', 'USER-GUIDE.md')
    guides = [ROOT / 'docs' / name for name in guide_names]
    require(all(p.is_file() for p in guides), 'Missing delivery guides')
    documentation = guides + [ROOT / 'README.md', ROOT / 'PILOT.md']
    for path in documentation:
        content = path.read_text(encoding='utf-8')
        require('/Users/' not in content and '/home/' not in content, 'Nonportable guide')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            require(target.is_file() and target.is_relative_to(ROOT), f'Broken guide link: {link}')
    artifact_specs = [
        (dist / f'email-assistant-{version}.zip', PACKAGE, 'email-assistant', files),
        (dist / f'email-assistant-marketplace-{version}.zip', ROOT, 'email-assistant-marketplace',
         files + documentation + [ROOT / '.gitignore', ROOT / '.agents/plugins/marketplace.json', Path(__file__).resolve()]),
    ]
    receipts = []
    for archive, base, prefix, members in artifact_specs:
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
            for path in sorted(members):
                require(path.is_file() and not path.is_symlink(), f'Invalid package member: {path}')
                output.write(path, Path(prefix) / path.relative_to(base))
        with zipfile.ZipFile(archive) as saved:
            require(saved.testzip() is None, 'ZIP integrity failed')
            names = saved.namelist()
            require(len(names) == len(set(names)), 'Duplicate ZIP paths')
            require(all(not name.startswith('/') and '..' not in Path(name).parts for name in names), 'Unsafe ZIP path')
            require(sum(name.endswith('/SKILL.md') for name in names) == len(EXPECTED_SKILLS), 'ZIP skill count mismatch')
            for path in members:
                require(saved.read(str(Path(prefix) / path.relative_to(base))) == path.read_bytes(), 'Archive readback mismatch')
        receipts.append(f'- {archive.name}: {len(names)} files, {archive.stat().st_size} bytes.')
    report = f'''# Package validation

Release: {version}. This report describes structural validation by scripts/build_release.py.

- All {len(EXPECTED_SKILLS)} expected skill entrypoints have matching names and nonempty descriptions.
- Portable and compatibility manifests agree on identity and presentation.
- Marketplace path, documented text limits, icon paths and SVG dimensions pass.
- {links} relative Markdown references resolve within the plugin.
- Plugin text has no author-machine absolute paths; no symlinks, environment files, key files, or Python cache files are included.
- Both release ZIPs pass integrity, unique-path, path-safety, {len(EXPECTED_SKILLS)}-skill, and byte-for-byte archive readback checks.
- Client guides have valid local links; the client delivery ZIP includes these guides and only this release's packages.

These checks do not certify the complete platform schema, installation, or skill behavior. Run the skill-creator validator separately after editing skills. Individual-account installation and update delivery, live connector behavior, user isolation, rule-change handling, meeting reports, and scheduled cloud execution remain pending in PILOT.md. No publication or scheduling is performed by this build.

'''
    report += '\n'.join(receipts) + '\n'
    (dist / 'VALIDATION.md').write_text(report, encoding='utf-8')
    delivery_members = documentation + [dist / 'VALIDATION.md'] + [spec[0] for spec in artifact_specs]
    payloads = {}
    for path in delivery_members:
        name = path.name if path.parent == dist else str(path.relative_to(ROOT))
        payloads[name] = path.read_bytes()
    payloads['SHA256SUMS.txt'] = ''.join(
        f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name, data in sorted(payloads.items())
    ).encode('utf-8')
    delivery = dist / f'email-assistant-client-delivery-{version}.zip'
    with zipfile.ZipFile(delivery, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payloads.items()):
            archive.writestr('email-assistant-client-delivery/' + name, data)
    with zipfile.ZipFile(delivery) as archive:
        require(archive.testzip() is None, 'Client delivery integrity failed')
        require(len(archive.namelist()) == len(payloads), 'Client delivery member mismatch')
        for name, data in payloads.items():
            require(archive.read('email-assistant-client-delivery/' + name) == data, 'Client delivery readback mismatch')
    checksums = ''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in sorted(dist.glob('*.zip')))
    (dist / 'SHA256SUMS.txt').write_text(checksums, encoding='utf-8')
    print(report)
    print(f'Client delivery verified: {delivery.name}, {len(payloads)} files')


if __name__ == '__main__':
    main()
