from fastapi import UploadFile, HTTPException


class LogFileReader:
    def read(self, file):
        content = file.file.read().decode("utf-8")
        if not content.strip():
            raise HTTPException(status_code=400, detail="Log file empty")
        return {
            "content": content,
            "line_count": len(content.splitlines())
        }



class LogAnalyzer:
    def analyze(self, log_data):
        content = log_data["content"]
        errors = []
        warnings = []

        for line in content.splitlines():
            if line.lower().startswith("error"):
                errors.append(line)
            if line.lower().startswith("warning"):
                warnings.append(line)

        if len(errors) == 0 and len(warnings) == 0:
            status = "healthy"
        else:
            status = "unhealthy"

        return {
            "error_count": len(errors),
            "warning_count": len(warnings),
            "status": status,
            "errors": errors,
            "warnings": warnings
        }


