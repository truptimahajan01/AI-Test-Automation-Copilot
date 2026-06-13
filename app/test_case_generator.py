from app.ai_client import AIClient
from app.prompt_builder import PromptBuilder
from fastapi import HTTPException

class TestCaseGenerator:
    def generate_test_cases(self, user_story):

        if not user_story or not user_story.strip():
            raise HTTPException(
                status_code=400,
                detail="User story cannot be empty"
            )


        prompt_builder = PromptBuilder()
        prompt = prompt_builder.build_test_case_prompt(
            user_story
        )

        ai_client = AIClient()

        try:
            return ai_client.generate(prompt)
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e)
            }