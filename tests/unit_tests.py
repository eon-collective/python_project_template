"""Script responsible for unit testing."""

import io
import json
import os
import sys
import tempfile
import unittest

from src.modules.process_team_summary import give_details  # G
from src.modules.process_team_summary import introduce_team  # I
from src.modules.process_team_summary import read_data  # S


class TestEmployeeFunctions(unittest.TestCase):
    """Contain application tests for functions."""

    def setUp(self):
        """Set up test environment.

        Create temp dir & JSON file for testing.
        """
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()
        # Create a temporary JSON file with sample data for testing
        self.temp_json_file = os.path.join(self.temp_dir, "teamke.json")
        sample_data = [
            {"Name": "Alice", "Role": "Developer"},
            {"Name": "Bob", "Role": "Manager"},
            {"Name": "Charlie", "Role": "Designer"},
        ]
        with open(self.temp_json_file, "w") as f:
            json.dump(sample_data, f)

    def tearDown(self):
        """Remove the temporary directory and its contents."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_read_data(self):
        """Test reading data from a JSON file."""
        data = read_data(self.temp_dir)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["Name"], "Alice")
        self.assertEqual(data[1]["Role"], "Manager")

    def test_introduce_team(self):
        """Test team introduction based on data."""
        data = read_data(self.temp_dir)
        team_info = introduce_team(data)
        self.assertEqual(team_info["Developer"], ["Alice"])
        self.assertEqual(team_info["Manager"], ["Bob"])
        self.assertEqual(team_info["Designer"], ["Charlie"])

    def test_give_details(self):
        """Test giving team member details."""
        data = read_data(self.temp_dir)
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout to capture print statements
        give_details(data)
        sys.stdout = sys.__stdout__  # Reset redirect
        output = captured_output.getvalue().strip()
        self.assertIn("Alice works as Developer.", output)
        self.assertIn("Charlie works as Designer.", output)


if __name__ == "__main__":
    unittest.main()
