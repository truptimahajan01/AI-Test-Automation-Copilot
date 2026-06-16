from google import genai
from dotenv import load_dotenv
from app.config_manager import ConfigManager
import json

load_dotenv()
config = ConfigManager()

class AIClient:
    def __init__(self):
        api_key = config.get("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing")

        self.client = genai.Client(
            api_key=api_key
        )

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        response = response.text

        response = response.replace("```json", "")
        response = response.replace("```", "")

        return response
        # try:
        #     return json.loads(response)
        # except json.JSONDecodeError:
        #     return {
        #         "error": "invalid JSON returned from GEMINI",
        #         "raw_response": response
        #     }