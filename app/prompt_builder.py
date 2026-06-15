class PromptBuilder:
    def build_test_case_prompt(self, user_story):
        if len(user_story.strip()) < 15 or len(user_story.split()) < 3:
            return f"""
{self._get_role()}
{self._get_rules()}
{self._get_task()}
User Story: 
{user_story}
{self._get_output_format()}
"""


        return f"""
{self._get_role()}

{self._get_task()}

User Story:
{user_story}

{self._get_output_format()}
"""

    def _get_role(self):
        return "You are a Senior QA Automation Engineer."

    def _get_task(self):
        return "Generate comprehensive positive, negative and edge test cases."

    def _get_rules(self):
        return "The user provided a short user story\n. Infer reasonable assumptions based on common software behavior."

    def _get_output_format(self):
        return " Return the response in JSON format\n. Return ONLY valid JSON\n. Do not use markdown\n. Do not wrap response in ```json\n. Do not provide explanations\n."

    def build_log_summary_prompt(self,log_summary):
        return f"""
        {self._get_role()}
        Analyze the following log summary.

        Log Summary:
        {log_summary}

        Identify:
        1. Most common failures
        2. Possible root cause
        3. Recommended next steps

        Return exactly 3 bullet points:
        1. Main issue
        2. Possible root cause
        3. Recommended action

        Keep each bullet under 1 sentence.
        """
