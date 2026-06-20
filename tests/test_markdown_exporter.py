from app.markdown_exporter import MarkdownExporter

def test_build_markdown_contains_report_details():
    exporter = MarkdownExporter()

    report_data = {
        "error": "Database connection lost",
        "generated_at": "2026-06-20",
        "bug_report": {
            "summary": "Login failed",
            "severity": "HIGH",
            "reproduction_steps": [
                "Open application",
                "Click login"
            ]
        }
    }

    markdown = exporter._build_markdown(report_data)

    assert "Login failed" in markdown
    assert "HIGH" in markdown
    assert "Open application" in markdown
