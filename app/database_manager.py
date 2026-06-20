import os
import sqlite3
from datetime import datetime
import json

class DatabaseManager:

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect("data/database.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_story TEXT,
            test_cases TEXT,
            file_path TEXT,
            created_at TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error TEXT,
            summary TEXT,
            severity TEXT,
            file_path TEXT,
            created_at TEXT
        )
        """)

        self.conn.commit()

    def save_report(self, report_data, file_path):
        error = report_data["error"]
        summary = report_data["bug_report"]["summary"]
        severity = report_data["bug_report"]["severity"]
        created_at = report_data["generated_at"]

        self.cursor.execute("""
        INSERT INTO reports (error, summary, severity, file_path, created_at)
        VALUES (?, ?, ?, ?, ?)
        """, (error, summary, severity, file_path, created_at))

        self.conn.commit()

    def save_test_case(self, user_story, test_cases, file_path):
        created_at = datetime.now().isoformat()
        test_case_json = test_cases

        self.cursor.execute("""
            INSERT INTO test_cases (user_story, test_cases, file_path, created_at)
            VALUES (?, ?, ?, ?)
        """, (user_story, test_case_json, file_path, created_at))

        self.conn.commit()

    def close(self):
        self.conn.close()


    def get_all_test_cases(self):
        self.cursor.execute(
            "SELECT * FROM test_cases"
        )

        rows =  self.cursor.fetchall()

        result = []
        for row in rows:
            result.append(dict(row))

        return result

    def get_test_case_by_id(self, test_case_id):
        self.cursor.execute(
            "SELECT * FROM test_cases WHERE id = ?",
            (test_case_id,)
        )

        row = self.cursor.fetchone()

        if not row:
            return None

        return dict(row)

    def get_all_reports(self):
        self.cursor.execute("SELECT * FROM reports")
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(row))

        return result

    def get_report_by_id(self, report_id):
        self.cursor.execute("SELECT * FROM reports WHERE id = ?", (report_id,))
        row = self.cursor.fetchone()
        if not row:
            return None
        return dict(row)