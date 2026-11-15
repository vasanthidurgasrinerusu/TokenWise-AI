
from groq import Groq
from config.settings import Settings


class LLMClient:

    def __init__(self):

        # Verify API configuration
        Settings.validate()

        # Connect to Groq
        self.client = Groq(
            api_key=Settings.GROQ_API_KEY,
            timeout=30.0
        )

        self.model = Settings.GROQ_MODEL

    def generate_response(self, prompt: str):

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        response = self.client.chat.completions.create(
            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are TokenWise AI, an intelligent "
                        "coding assistant. Explain your answers "
                        "clearly and provide safe coding guidance."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_completion_tokens=1024
        )

        message = response.choices[0].message.content

        usage = response.usage

        return {
            "response": message or "",
            "model": response.model,
            "input_tokens": usage.prompt_tokens if usage else 0,
            "output_tokens": usage.completion_tokens if usage else 0,
            "total_tokens": usage.total_tokens if usage else 0
        }
