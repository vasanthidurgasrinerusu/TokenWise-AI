
from optimization.token_tracker import TokenTracker


def main():

    tracker = TokenTracker()

    input_text = "Create a Python calculator"

    output_text = """
def add(a, b):
    return a + b
"""

    result = tracker.track_usage(
        input_text,
        output_text
    )

    print("\n===== TOKEN USAGE REPORT =====")

    print("Input Tokens:", result["input_tokens"])
    print("Output Tokens:", result["output_tokens"])
    print("Total Tokens:", result["total_tokens"])
    print("Session Total:", result["session_total"])

    print("\nToken Tracker Test Completed!")


if __name__ == "__main__":
    main()
