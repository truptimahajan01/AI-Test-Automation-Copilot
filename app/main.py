from fastapi import FastAPI, File, UploadFile, HTTPException

from app.database_manager import DatabaseManager
from app.log_analyzer import LogFileReader, LogAnalyzer, AISummaryGenerator
from app.test_case_generator import TestCaseGenerator
from app.models import GenerateTestsRequest
from app.error_analyzer import ErrorAnalyzer
from app.bug_report_generator import BugReportGenerator
from app.markdown_exporter import MarkdownExporter
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

@app.post("/generate-bug-report")
def generate_bug_report(errorG: str):
    error_analyzer = ErrorAnalyzer()

    error_analysis = (
        error_analyzer.analyze(errorG)
    )

    bug_report_generator = (BugReportGenerator())

    bug_report = bug_report_generator.generate(errorG,error_analysis["analysis"])

    exporter = MarkdownExporter()
    report_file = exporter.export(bug_report)

    return {
        "bug_report": bug_report,
        "report_file": report_file
    }

@app.get("/test-cases")

def get_test_cases():
    db = DatabaseManager()

    test_cases = db.get_all_test_cases()
    return {
        "count": len(test_cases),
        "test_cases": test_cases
    }

@app.get("/test-cases/{test_case_id}")
def test_case(test_case_id: int):
    db = DatabaseManager()
    test_case = db.get_test_case_by_id(test_case_id)

    if test_case is None:
        raise HTTPException(status_code=404, detail="Test case not found")

    return test_case

@app.get("/report")
def test_case_report():
    db = DatabaseManager()
    report = db.get_all_reports()
    return {
        "count": len(report),
        "report": report
    }

@app.get("/report/{report_id}")
def report(report_id: int):
    db = DatabaseManager()
    report = db.get_report_by_id(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report