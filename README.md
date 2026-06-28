# Search Ranking Tracker

키워드별 검색 결과에서 내 사이트가 몇 위에 노출되는지 추적하는 작은 Python 프로그램입니다. 주간 검색 가시성 개선 전략을 실행할 때, 핵심 키워드의 순위 변화를 CSV 이력으로 남기는 용도에 맞췄습니다.

## 기능

- 여러 키워드와 여러 타깃 사이트를 한 번에 확인
- DuckDuckGo HTML 검색 결과를 기본 엔진으로 사용
- 도메인 또는 URL prefix 패턴으로 내 사이트 매칭
- 실행할 때마다 `checked_at`, `keyword`, `target`, `best_rank`, `matched_url`를 CSV에 누적 저장
- 사람이 읽기 쉬운 콘솔 출력과 자동화용 JSON 출력 지원

> 검색 엔진 HTML 구조와 정책은 바뀔 수 있습니다. 중요한 운영 환경에서는 공식 Search API 또는 SERP API의 URL 템플릿을 `--engine-url`로 연결해 사용하세요.

## 빠른 시작

```bash
cp examples/rank-tracker.example.json rank-tracker.json
python -m rank_tracker.cli --config rank-tracker.json --output data/rank-history.csv
```

## 설정 파일

`rank-tracker.json` 예시:

```json
{
  "keywords": ["검색 순위 추적 프로그램", "주간 검색 가시성 개선 전략"],
  "targets": [
    {
      "name": "내 사이트",
      "patterns": ["example.com", "https://www.example.com/blog"]
    }
  ]
}
```

- `keywords`: 순위를 추적할 검색어 목록
- `targets[].name`: 리포트에 표시할 타깃 이름
- `targets[].patterns`: 매칭할 도메인 또는 URL prefix 목록

## 사용법

```bash
python -m rank_tracker.cli \
  --config rank-tracker.json \
  --output data/rank-history.csv \
  --limit 30
```

JSON 출력이 필요하면 `--json`을 추가합니다.

```bash
python -m rank_tracker.cli --config rank-tracker.json --json
```

다른 검색 공급자를 쓰려면 `{query}` 자리표시자를 포함한 URL 템플릿을 넘깁니다.

```bash
python -m rank_tracker.cli --engine-url 'https://duckduckgo.com/html/?q={query}'
```

## 주간 운영 루틴

1. 월요일 오전에 프로그램을 실행해 `data/rank-history.csv`를 갱신합니다.
2. 순위가 하락한 키워드를 콘텐츠 개선 후보로 표시합니다.
3. 개선 후 다음 주 같은 요일에 다시 실행해 `best_rank` 변화를 비교합니다.
4. 미노출 키워드는 제목, 메타 설명, 내부 링크, FAQ 섹션을 우선 보강합니다.

## 개발 및 테스트

```bash
python -m pytest
```
