from pathlib import Path
root=Path('magazine/assets')
for p in root.glob('*.svg'):
    s=p.read_text(encoding='utf-8')
    s=s.replace("Arial, 'Noto Sans KR', sans-serif", "'Noto Sans KR', 'Pretendard', Arial, sans-serif")
    p.write_text(s, encoding='utf-8')
print('updated', len(list(root.glob('*.svg'))), 'svg files')
