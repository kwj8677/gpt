from pathlib import Path
import re, sys
root=Path('.')
mag=root/'magazine'; site=root/'docs'/'magazine'
issues=sorted(mag.glob('[0-9][0-9]-*.ko.md'))
errors=[]; warnings=[]
if len(issues)!=7: errors.append(f'expected 7 markdown issues, found {len(issues)}')
for p in issues:
    s=p.read_text(encoding='utf-8')
    if '**근거 상태:**' not in s: errors.append(f'{p}: missing evidence status')
    if not re.search(r'무엇이 이 (?:결론|가설)을 바꿀까\?', s): errors.append(f'{p}: missing falsifier section')
    for term in ['박사 수준','doctoral-style','한국이 최고','우리나라가 최고','세계 1위','무조건 옳','당연히 옳','내가 만든 이론','검증된 학술 이론']:
        if term in s: warnings.append(f'{p}: review phrase {term!r}')
htmls=sorted(site.glob('[0-9][0-9]-*.html'))
if len(htmls)!=7: errors.append(f'expected 7 article html files, found {len(htmls)}')
for p in htmls+[site/'index.html',site/'style-guide.html']:
    if not p.exists(): errors.append(f'missing {p}'); continue
    s=p.read_text(encoding='utf-8')
    if '<!doctype html>' not in s.lower(): errors.append(f'{p}: no doctype')
    if '\\[' in s or '\\theta' in s or '\\approx' in s: errors.append(f'{p}: raw latex remains')
    for attr in re.findall(r'(?:src|href)="([^"]+)"',s):
        if attr.startswith(('http:','https:','#','mailto:')): continue
        target=(p.parent/attr).resolve()
        if not target.exists(): errors.append(f'{p}: broken local ref {attr}')
index=(site/'index.html').read_text(encoding='utf-8')
if index.count('class="feed-article"') != len(issues): errors.append('index: continuous feed does not contain all issues')
if 'class="issue-row"' in index: errors.append('index: old click-through issue cards remain')
if index.find('id="column-07"') > index.find('id="column-01"'): errors.append('index: newest column is not first')
for p in issues:
    title=p.read_text(encoding='utf-8').splitlines()[0].removeprefix('# ').strip()
    if title not in index: errors.append(f'index: missing full-feed title {title}')
css=(site/'style.css').read_text(encoding='utf-8')
for needle in ['Noto Serif KR','Noto Sans KR','word-break: keep-all','font-variant-numeric: tabular-nums','@media print','@media (max-width: 480px)']:
    if needle not in css: errors.append(f'CSS missing {needle}')
for p in (mag/'assets').glob('*.svg'):
    s=p.read_text(encoding='utf-8')
    if "Arial, 'Noto Sans KR'" in s: errors.append(f'{p}: Arial-first font stack remains')
print('issues',len(issues),'html',len(htmls))
print('warnings',len(warnings))
for x in warnings: print('WARN',x)
print('errors',len(errors))
for x in errors: print('ERROR',x)
sys.exit(1 if errors else 0)
