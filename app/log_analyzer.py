from fastapi import UploadFile, HTTPException
from datetime import datetime
from app.prompt_builder import PromptBuilder
from app.ai_client import AIClient


class LogFileReader:
    def read(self, file):
        content = file.file.read().decode("utf-8")
        if not content.strip():
            raise HTTPException(status_code=400, detail="Log file empty")
        return {
            "content": content,
            "line_count": len(content.splitlines())
        }



class LogAnalyzer:
    def analyze(self, log_data):
        content = log_data["content"]
        errors = []
        warnings = []

        counts = {
            "ERROR": 0,
            "WARNING": 0,
            "INFO": 0
        }

        for line in content.splitlines():
            for level in counts:
                if line.upper().startswith(level):
                    counts[level] += 1

            if line.upper().startswith("ERROR"):
                errors.append(line)

            if line.upper().startswith("WARNING"):
                warnings.append(line)

        if len(errors) == 0 and len(warnings) == 0:
            status = "healthy"
        else:
            status = "unhealthy"

        return {
            "counts": counts,
            "total_lines": log_data["line_count"],
            "status": status,
            "errors": errors,
            "warnings": warnings
        }

class AISummaryGenerator:
    def generate_summary(self, log_summary):
        prompt_builder = PromptBuilder()

        prompt_data = {
            "counts": log_summary["counts"],
            "errors": log_summary.get("errors", [])[:20],
            "warnings": log_summary.get("warnings", [])[:20]
        }

        prompt = (
            prompt_builder.build_log_summary_prompt(prompt_data)
        )

        ai_client = AIClient()

        summary = ai_client.generate(prompt)
        return {
            "summary": summary,
            "generated_at": datetime.now().isoformat(),
        }


