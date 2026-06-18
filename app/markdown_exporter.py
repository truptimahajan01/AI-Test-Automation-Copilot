import os
from datetime import datetime

class MarkdownExporter:
    def export(self, report_data):
        os.makedirs(
            "reports",
            exist_ok=True
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename =  f"reports/report_{timestamp}.md"
        content = self._build_markdown(report_data)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "file_name": os.path.basename(filename),
            "file_path": filename
        }

    def _build_markdown(self, report_data):
        summary = report_data["bug_report"]["summary"]
        error = report_data["error"]
        generated_at = report_data["generated_at"]
        severity = report_data["bug_report"]["severity"]
        reproduction_steps = report_data["bug_report"]["reproduction_steps"]

        steps_text = ""

        for index, step in enumerate(reproduction_steps, start=1):
            steps_text += f"{index}. {step}\n"

        return f"""
# Bug Report 

## Error
{error}

## Generated at
{generated_at}

## Summary
{summary}

## Severity
{severity}

## Reproduction steps
{steps_text}
"""