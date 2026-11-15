
from pathlib import Path


class RepositoryReader:

    IGNORED_DIRS = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        ".pytest_cache"
    }

    def __init__(self, root="."):
        self.root = Path(root).resolve()

    def list_files(self):
        files = []

        for path in self.root.rglob("*"):

            if not path.is_file():
                continue

            if any(part in self.IGNORED_DIRS
                   for part in path.relative_to(self.root).parts):
                continue

            files.append(str(path.relative_to(self.root)))

        return sorted(files)

    def read_file(self, filename):

        path = (self.root / filename).resolve()

        # Prevent directory traversal
        if not path.is_relative_to(self.root):
            raise ValueError("Access outside repository is not allowed")

        if not path.is_file():
            raise FileNotFoundError(filename)

        # Limit reading to 100 KB
        if path.stat().st_size > 100 * 1024:
            raise ValueError("File exceeds the 100 KB reading limit")

        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raise ValueError("File is not valid UTF-8 text")
