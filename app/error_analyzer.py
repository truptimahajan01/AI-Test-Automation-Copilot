from fastapi import HTTPException
from datetime import datetime
from app.prompt_builder import PromptBuilder
from app.ai_client import AIClient

class ErrorAnalyzer:
    def analyze(self,error):
        if not error or not error.strip():
            raise HTTPException(status_code=400, detail="Error message cannot be empty")

        prompt_builder = PromptBuilder()

        prompt = prompt_builder.build_error_analysis_prompt(error)

        ai_client = AIClient()

        try:
            analysis = ai_client.generate(prompt)
        except Exception as e:
            analysis = f"AI unavailable: {str(e)}"

        return {
            "error": error,
            "analysis": analysis,
            "generated_at": datetime.now().isoformat(),
            }