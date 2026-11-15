
import unittest
import tempfile

from pathlib import Path
from unittest.mock import patch

from tools.file_writer import RepositoryWriter


class TestRepositoryWriter(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.writer = RepositoryWriter(
            root=self.temp_dir.name
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_approved_file_write(self):

        with patch("builtins.input", return_value="yes"):

            result = self.writer.write_file(
                "sample.py",
                "print('Hello TokenWise AI')"
            )

        self.assertTrue(result["success"])

        saved_file = Path(self.temp_dir.name) / "sample.py"

        self.assertTrue(saved_file.exists())

        self.assertEqual(
            saved_file.read_text(encoding="utf-8"),
            "print('Hello TokenWise AI')"
        )

    def test_rejected_file_write(self):

        with patch("builtins.input", return_value="no"):

            result = self.writer.write_file(
                "rejected.py",
                "print('This should not be saved')"
            )

        self.assertFalse(result["success"])

        saved_file = Path(self.temp_dir.name) / "rejected.py"

        self.assertFalse(saved_file.exists())

    def test_block_external_path(self):

        with self.assertRaises(ValueError):

            self.writer.write_file(
                "../outside.py",
                "print('Unsafe')"
            )

    def test_block_env_file(self):

        with self.assertRaises(ValueError):

            self.writer.write_file(
                ".env",
                "SECRET=value"
            )

    def test_update_existing_file(self):

        saved_file = Path(self.temp_dir.name) / "sample.py"

        # Create original file
        saved_file.write_text(
            "print('Old version')",
            encoding="utf-8"
        )

        # Approve the update
        with patch("builtins.input", return_value="yes"):

            result = self.writer.write_file(
                "sample.py",
                "print('Updated version')"
            )

        self.assertTrue(result["success"])

        self.assertEqual(
            saved_file.read_text(encoding="utf-8"),
            "print('Updated version')"
        )


if __name__ == "__main__":
    unittest.main()
