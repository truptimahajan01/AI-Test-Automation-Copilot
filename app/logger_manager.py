class LoggerManager:
    def log_info(self, message):
         self._write_log("INFO", message)

    def log_warning(self, message):
        self._write_log("WARNING", message)

    def log_error(self, message):
        self._write_log("ERROR", message)

    def _write_log(self, level, message):
        with open("logs/app.log", "a") as file:
            log_message = f"[{level}] {message} \n"
            file.write(log_message)