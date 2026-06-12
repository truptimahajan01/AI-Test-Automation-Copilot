from pydantic import BaseModel

class GenerateTestsRequest(BaseModel):
    user_story: str