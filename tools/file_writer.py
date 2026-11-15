
from pathlib import Path
from difflib import unified_diff

from security.approvals import ApprovalManager

class RepositoryWriter:

    BLOCKED_DIRS = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules"
    }

    def __init__(self, root="."):

        self.root = Path(root).resolve()
        self.approvals = ApprovalManager()

    def write_file(self, filename: str, content: str):

        if not filename or not filename.strip():
            raise ValueError("Filename cannot be empty")

        if not isinstance(content, str):
            raise TypeError("File content must be text")

        target = (self.root / filename).resolve()

        # Prevent writing outside the repository
        if not target.is_relative_to(self.root):
            raise ValueError("Access outside repository is not allowed")

        relative_path = target.relative_to(self.root)

        # Block protected directories
        if any(part in self.BLOCKED_DIRS for part in relative_path.parts):
            raise ValueError("Writing to this directory is not allowed")

        # Protect sensitive files
        protected_names = {
            ".env",
            ".env.local",
            ".env.production"
        }

        if (
            target.name in protected_names
            or target.suffix.lower() in {".pem", ".key"}
            or "secret" in target.name.lower()
            or "credentials" in target.name.lower()
        ):
            raise ValueError("Writing to sensitive files is not allowed")

        if not target.parent.is_dir():
            raise FileNotFoundError("Target directory does not exist")

        # Read existing content
        if target.exists():
            if not target.is_file():
                raise ValueError("Target must be a regular file")

            old_content = target.read_text(encoding="utf-8")
        else:
            old_content = ""

        # Generate change preview
        preview = unified_diff(
            old_content.splitlines(keepends=True),
            content.splitlines(keepends=True),
            fromfile=f"Current: {relative_path}",
            tofile=f"Proposed: {relative_path}"
        )

        print("\n========== CHANGE PREVIEW ==========")

        preview_text = "".join(preview)

        if preview_text:
            print(preview_text)
        else:
            print("No changes detected.")

        print("====================================")

        if old_content == content:
            return {
                "success": False,
                "message": "No changes detected"
            }

        # Ask for approval after showing the preview
        approved = self.approvals.request_approval(
            action="Write or update file",
            filename=str(relative_path)
        )

        if not approved:
            return {
                "success": False,
                "message": "File modification rejected"
            }

        # Apply approved changes
        target.write_text(content, encoding="utf-8")

        return {
            "success": True,
            "message": "File updated successfully",
            "filename": str(relative_path)
        }