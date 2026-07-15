import os
import token
from dotenv import load_dotenv

# This class is used to load the environment variables from the .env file and read the github token from it
class AppConfig:
    @staticmethod
    def token():
        load_dotenv() # load the environment variables from the .env file
        GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") # Read the github token from the .env file
        if not GITHUB_TOKEN:
            raise ValueError("Critical Error: GITHUB_TOKEN is missing from your .env file!")
        return GITHUB_TOKEN
