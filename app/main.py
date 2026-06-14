from fastapi import FastAPI, File, UploadFile
from app.log_analyzer import LogFileReader, LogAnalyzer
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

@app.post("/analyze-log")
def analyze_log(file: UploadFile = File(...)):
   reader = LogFileReader()
   log_data = reader.read(file)
   analyzer = LogAnalyzer()
   analysis = analyzer.analyze(log_data)

   return {
       "line_count": log_data["line_count"],
       **analysis
   }
