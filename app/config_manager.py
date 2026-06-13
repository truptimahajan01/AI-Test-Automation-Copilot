import os
from dotenv import load_dotenv

load_dotenv()

class ConfigManager:
    def get(self,key):
        return os.getenv(key)