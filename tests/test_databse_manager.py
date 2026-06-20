from app.database_manager import DatabaseManager

def test_save_test_case():
    db = DatabaseManager()

    db.save_test_case(
        "Login",
        [{"id": "TC-001"}],
        "generated_tests/login.json"
    )

    result = db.get_all_test_cases()

    assert result[-1]["user_story"] == "Login"

def test_get_test_case_by_id():
    db = DatabaseManager()
    db.save_test_case(
    "Login",
    [{"id": "TC-001"}],
    "generated_tests/login.json"
    )
    result = db.get_test_case_by_id(1)

    assert result["user_story"] == "Login"

def test_get_test_case_by_invalid_id():
    db = DatabaseManager()
    result = db.get_test_case_by_id(999)

    assert result is None
