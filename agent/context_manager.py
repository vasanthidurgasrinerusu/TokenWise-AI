
class ContextManager:

    def __init__(self, max_files=5):
        self.max_files = max_files

    def select_relevant_files(self, task, repository_files):

        task_words = set(task.lower().split())

        scored_files = []

        for filename in repository_files:

            filename_words = set(
                filename.lower()
                .replace("/", " ")
                .replace("_", " ")
                .replace(".", " ")
                .split()
            )

            score = len(task_words.intersection(filename_words))

            if score > 0:
                scored_files.append((score, filename))

        scored_files.sort(
            key=lambda item: item[0],
            reverse=True
        )

        selected_files = [
            filename
            for score, filename in scored_files[:self.max_files]
        ]

        return selected_files
