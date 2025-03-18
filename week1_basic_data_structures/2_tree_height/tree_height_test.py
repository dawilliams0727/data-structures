import os
import time
import unittest
from tree_height import compute_height

class TestTreeHeight(unittest.TestCase):
    def setUp(self):
        self.test_files = []
        self.answer_files = []
        tests_folder = os.path.join(os.path.dirname(__file__), "tests")
        for filename in os.listdir(tests_folder):
            
            filepath = os.path.join(tests_folder, filename)
            if filename.endswith('.a'):
                with open(filepath, 'r') as file:
                    self.answer_files.append(file.readline().strip())
            else:
                with open(filepath, 'r') as file:
                    _ , parents = file.readlines()
                    parents = parents.strip()
                    data = list(map(int, parents.split()))
                    self.test_files.append(data)
    
    def test_provided_tests(self):
        for i, parents in enumerate(self.test_files):
            print(f"{i+1}: {len(parents)} {parents} expected: {self.answer_files[i]}")
            self.assertEqual(compute_height(len(parents), parents), int(self.answer_files[i]))

if __name__ == "__main__":
    unittest.main()