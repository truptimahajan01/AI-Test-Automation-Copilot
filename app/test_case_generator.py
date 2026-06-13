from app.ai_client import AIClient
from app.prompt_builder import PromptBuilder

class TestCaseGenerator:
    def generate_test_cases(self, user_story):
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