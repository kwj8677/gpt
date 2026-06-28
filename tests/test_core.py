from rank_tracker.core import Target, parse_search_results, write_csv
from rank_tracker.core import RankResult, RankMatch


def test_target_matches_domains_and_urls():
    target = Target("site", ("example.com", "https://docs.example.org/rank"))
    assert target.matches("https://www.example.com/post")
    assert target.matches("https://docs.example.org/rank/guide")
    assert not target.matches("https://competitor.example.net/post")


def test_parse_search_results_extracts_duckduckgo_redirects_once():
    html = """
    <a class="result__a" href="//duckduckgo.com/l/?uddg=https%3A%2F%2Fexample.com%2Fa">A result</a>
    <a href="https://duckduckgo.com/settings">Settings</a>
    <a href="https://other.test/page">Other</a>
    <a href="https://other.test/page">Duplicate</a>
    """
    assert parse_search_results(html) == [
        ("A result", "https://example.com/a"),
        ("Other", "https://other.test/page"),
    ]


def test_write_csv_appends_history(tmp_path):
    path = tmp_path / "history.csv"
    write_csv(
        path,
        [RankResult("2026-06-28T00:00:00+00:00", "keyword", "site", 2, (RankMatch(2, "Title", "https://example.com"),), 10)],
    )
    text = path.read_text(encoding="utf-8")
    assert "checked_at,keyword,target,status,best_rank,matched_url,total_results_checked" in text
    assert "keyword,site,found,2,https://example.com,10" in text
