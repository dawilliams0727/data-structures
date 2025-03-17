import os
import sys
import unittest
import time
from check_brackets import find_mismatch as check_brackets

class TestCheckBrackets(unittest.TestCase):
    def setUp(self):
        self.test_files = []
        self.answer_files = []
        tests_folder = os.path.join(os.path.dirname(__file__), 'tests')
        
        for filename in os.listdir(tests_folder):
            filepath = os.path.join(tests_folder, filename)
            if filename.endswith('.a'):
                with open(filepath, 'r') as file:
                    self.answer_files.append(file.readline())
            else:
                with open(filepath, 'r') as file:
                    self.test_files.append(file.read().strip())
    
    def test_check_brackets(self):
        i = 1
        for data, answer in zip(self.test_files, self.answer_files):
            print(f"{i}: {data}")
            print(answer)
            self.assertEqual(check_brackets(data), answer.strip())
            i += 1

if __name__ == "__main__":
    unittest.main()