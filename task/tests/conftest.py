import json
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption(
        "--ctrf",
        action="store",
        dest="ctrf_path",
        default=None,
        help="Write a minimal CTRF-style JSON report to the given path.",
    )


def pytest_sessionfinish(session, exitstatus):
    ctrf_path = session.config.getoption("ctrf_path")
    if not ctrf_path:
        return

    report_path = Path(ctrf_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    tests = []
    for item in session.items:
        outcome = "passed"
        if item in getattr(session, "failed_items", []):
            outcome = "failed"
        elif item in getattr(session, "skipped_items", []):
            outcome = "skipped"
        tests.append(
            {
                "name": item.nodeid,
                "outcome": outcome,
                "duration": 0,
            }
        )

    payload = {
        "results": tests,
        "summary": {
            "passed": sum(1 for t in tests if t["outcome"] == "passed"),
            "failed": sum(1 for t in tests if t["outcome"] == "failed"),
            "skipped": sum(1 for t in tests if t["outcome"] == "skipped"),
        },
    }
    report_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
