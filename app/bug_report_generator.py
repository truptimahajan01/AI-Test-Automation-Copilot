from app.ai_client import AIClient
import json
from datetime import datetime
from app.prompt_builder import PromptBuilder

class BugReportGenerator:
    def generate(self, error, analysis,):
        prompt_builder = PromptBuilder()
        prompt = prompt_builder.build_bug_report_prompt(error, analysis)

        ai_client = AIClient()

        response = ai_client.generate(prompt)

        bug_report = json.loads(response)

        allowed_severities = {
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        }

        severity = bug_report["severity"]

        if severity not in allowed_severities:
            raise ValueError(
                f"Invalid severity: {severity}"
            )

        required_fields = [
            "summary",
            "severity",
            "reproduction_steps"
        ]

        for field in required_fields:
            if field not in bug_report:
                raise ValueError(
                    f"Missing required field: {field}"
                )

        if not isinstance(bug_report["reproduction_steps"], list):
            raise ValueError("reproduction_steps must be a list")

        if len(bug_report["reproduction_steps"]) == 0:
            raise ValueError("reproduction_steps cannot be an empty")

        return {
            "error": error,
            "generated_at": datetime.now().isoformat(),
            "bug_report": bug_report
        }