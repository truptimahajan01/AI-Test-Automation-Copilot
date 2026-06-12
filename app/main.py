from fastapi import FastAPI

from app.test_case_generator import TestCaseGenerator
from app.models import GenerateTestsRequest

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/generate-tests")
def generate_tests(generate_tests_request: GenerateTestsRequest):
    generator = TestCaseGenerator()
    results = generator.generate_test_cases(generate_tests_request.user_story)
    return {"test_cases": results}