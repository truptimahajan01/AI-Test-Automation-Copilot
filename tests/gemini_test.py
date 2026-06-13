from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


class AIClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY"),
        )

    def generate(self, prompt="Generate 3 test cases for Login functionality."):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

client = AIClient()

response = client.generate()

print(response)