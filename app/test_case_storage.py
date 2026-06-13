from datetime import datetime

class TestCaseStorage:

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    def create_directory(self):
        os.makedirs(
            "generated_tests",
            exist_ok=True
        )

    def create_filename(self, user_story, timestamp):
        words = user_story.lower().split()
        short_name = "_".join(words[:5])
        return f"generated_tests/{short_name}_{timestamp}.json"

    def save_json(self, user_story, test_cases):
        self.create_directory()
        file_path = self.create_filename(user_story, timestamp)
        with open(file_path, "w") as file:
            json.dump(test_cases, file, indent=4)

        return file_path