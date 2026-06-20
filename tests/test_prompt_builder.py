from app.prompt_builder import PromptBuilder

def test_build_test_case_prompt():
    prompt_builder = PromptBuilder()

    user_story = "Login functionality"

    prompt = prompt_builder.build_test_case_prompt(user_story)

    assert isinstance(prompt, str)
    assert user_story in prompt

def test_build_test_case_prompt_returns_string():
    prompt_builder = PromptBuilder()

    prompt = prompt_builder.build_test_case_prompt("")
    assert isinstance(prompt, str)

