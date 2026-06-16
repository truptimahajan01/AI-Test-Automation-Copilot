from app.ai_client import AIClient
from app.prompt_builder import PromptBuilder
from app.test_case_storage import TestCaseStorage
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
            test_cases = ai_client.generate(prompt)
            storage = TestCaseStorage()

            file_path = storage.save_json(
                user_story,
                test_cases
            )

            return {
                "test_cases": test_cases,
                "file_path": file_path
            }
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=500,
                detail="Invalid JSON returned from AI"
            )

        except Exception as e:
            return {
                "status": "failed",
                "message": str(e)
            }
