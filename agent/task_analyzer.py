
class TaskAnalyzer:

    def analyze(self, task: str):

        task = task.lower()

        simple_keywords = [
            "print",
            "rename",
            "change",
            "simple",
            "calculator"
        ]

        medium_keywords = [
            "function",
            "class",
            "api",
            "database",
            "validation"
        ]

        complex_keywords = [
            "architecture",
            "authentication",
            "machine learning",
            "entire application",
            "system design"
        ]

        if any(word in task for word in complex_keywords):
            complexity = "COMPLEX"

        elif any(word in task for word in medium_keywords):
            complexity = "MEDIUM"

        else:
            complexity = "SIMPLE"

        return {
            "task": task,
            "complexity": complexity
        }
