import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile"
    )

    @classmethod
    def validate(cls):

        if not cls.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing. Check your .env file."
            )

        return True