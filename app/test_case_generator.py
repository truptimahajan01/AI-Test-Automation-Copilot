class TestCaseGenerator:
    def generate_test_cases(self, user_story):
        return [
            {
                "test_case_id": 1,
                "title": "Verify successful login",
                "priority": "High"
            },
            {
                "test_case_id": 2,
                "title": "Verify invalid password",
                "priority": "Medium"
            }
        ]