
from agent.llm_client import LLMClient


def main():

    print("Connecting to TokenWise AI...")

    try:
        ai = LLMClient()

        result = ai.generate_response(
            "Explain Python functions in simple English."
        )

        print("\n===== AI RESPONSE =====")
        print(result["response"])

        print("\n===== TOKEN USAGE =====")
        print("Model:", result["model"])
        print("Input Tokens:", result["input_tokens"])
        print("Output Tokens:", result["output_tokens"])
        print("Total Tokens:", result["total_tokens"])

        print("\nAI connection successful!")

    except Exception as error:
        print("\nAI connection failed:", error)


if __name__ == "__main__":
    main()
