import unittest
import tempfile
import os
import sys
from pathlib import Path
from cat_plus.cat_plus import main
from io import StringIO
from unittest.mock import patch

sys.path.append(str(Path(__file__).parent.parent / "src"))

class TestCatPlus(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.txt")
        with open(self.test_file, "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

    def tearDown(self):
        # Clean up temporary files
        os.remove(self.test_file)
        os.rmdir(self.temp_dir)

    @patch('sys.argv', ['cat_plus', 'test.txt'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_basic_file_reading(self, mock_stdout):
        with patch('argparse.ArgumentParser.parse_args') as mock_args:
            mock_args.return_value.file = self.test_file
            mock_args.return_value.line_numbers = False
            main()
            self.assertEqual(mock_stdout.getvalue(), "Line 1\nLine 2\nLine 3")

    @patch('sys.argv', ['cat_plus', '-n', 'test.txt'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_line_numbers(self, mock_stdout):
        with patch('argparse.ArgumentParser.parse_args') as mock_args:
            mock_args.return_value.file = self.test_file
            mock_args.return_value.line_numbers = True
            main()
            expected = "     1  Line 1\n     2  Line 2\n     3  Line 3"
            self.assertEqual(mock_stdout.getvalue(), expected)