
class TokenTracker:

    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0

    def estimate_tokens(self, text: str):

        if not text:
            return 0

        return max(1, len(text) // 4)

    def track_usage(self, input_text: str, output_text: str):

        input_tokens = self.estimate_tokens(input_text)
        output_tokens = self.estimate_tokens(output_text)

        return self.track_actual_usage(
            input_tokens,
            output_tokens
        )

    def track_actual_usage(self, input_tokens: int, output_tokens: int):

        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

        total = input_tokens + output_tokens
        self.total_tokens += total

        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total,
            "session_total": self.total_tokens
        }

    def get_usage(self):

        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_tokens
        }

    def reset(self):

        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0
