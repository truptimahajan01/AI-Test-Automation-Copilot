from fastapi import FastAPI, File, UploadFile
from app.log_analyzer import LogFileReader, LogAnalyzer, AISummaryGenerator
from app.test_case_generator import TestCaseGenerator
from app.models import GenerateTestsRequest
from app.error_analyzer import ErrorAnalyzer
app = FastAPI()

@app.get("/health")
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
   ai_summary_generator = AISummaryGenerator()
   try:
       ai_summary = (
           ai_summary_generator.generate_summary(analysis)
       )
   except Exception as e:
        ai_summary = {
            "summary": None,
            "errors": str(e)
        }
   return {
       "analysis": analysis,
       "ai_summary": ai_summary
   }

@app.post("/analyze-error")
def analyze_error(error: str):
    analyzer = ErrorAnalyzer()
    return analyzer.analyze(error)
