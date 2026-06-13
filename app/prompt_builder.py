class PromptBuilder:
    def build_test_case_prompt(self, user_story):
        return f"""
You are a Senior QA Automation Engineer.

Generate positive, negative and edge test cases.

User Story:
{user_story}

Return the response in JSON format.
Return ONLY valid JSON.
Do not use markdown.
Do not wrap response in ```json.
Do not provide explanations.
"""

    def _get_role(self):
        pass

    def _get_task(self):
        pass

    def _get_rules(self):
        pass

    def _get_output_format(self):
        pass