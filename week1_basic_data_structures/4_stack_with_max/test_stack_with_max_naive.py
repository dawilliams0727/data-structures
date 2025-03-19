import os
import unittest
from stack_with_max_naive import StackWithMax

class TestStackWithMax(unittest.TestCase):
    def setUp(self):
        self.test_files = []
        self.answer_files = []
        tests_folder = os.path.join(os.path.dirname(__file__), "tests")
        for filename in os.listdir(tests_folder):
            
            filepath = os.path.join(tests_folder, filename)
            if filename.endswith('.a'):
                with open(filepath, 'r') as file:
                    results = list(map(str.strip,file.readlines()))
                    self.answer_files.append(results)
            else:
                with open(filepath, 'r') as file:
                    num_queries = int(file.readline())
                    queries = list(map(str.strip,file.readlines()))
                    self.test_files.append(queries)

    def test_provided_samples(self):
        for i in range(len(self.test_files)):
            self.stack = StackWithMax()
            data = self.test_files[i]
            expected = self.answer_files[i]
            actual = []
            print(f"{i+1}.) {data} Expected: {expected}")
            for query in data:
                if "push" in query:
                    _,val = query.split()
                    self.stack.Push(val)
                elif "pop" in query:
                    self.stack.Pop()
                elif "max" in query:
                    max = self.stack.Max()
                    if max:
                        actual.append(max)
                        
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()