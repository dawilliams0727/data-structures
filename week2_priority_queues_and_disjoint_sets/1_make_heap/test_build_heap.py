import unittest
import os
import random
from build_heap import build_heap, build_heap_

class TestBuildHeap(unittest.TestCase):
    def setUp(self):
        self.test_data = []
        self.test_answer = []
        test_folder = os.path.join(os.path.dirname(__file__), "tests")

        for filename in os.listdir(test_folder):
            filepath = os.path.join(test_folder, filename)
            if filepath.endswith('a'):
                with open(filepath, 'r') as file:
                    file.readline()
                    result = []
                    lines = file.readlines()
                    for line in lines:
                        i,j = map(int, line.split(" "))
                        result.append((i,j))
                    self.test_answer.append(result)
            else:
                with open(filepath, 'r') as file:
                    file.readline()
                    data = file.readline()
                    self.test_data.append(list(map(int, data.split())))
    
    def test_large_input(self):
        self.assertEqual(build_heap(self.test_data[0]), self.test_answer[0])

    def test_sorted_asc_input(self):
        self.assertEqual(build_heap([1,2,3,4,5]), [])
    
    def test_sorted_desc_input(self):
        self.assertEqual(build_heap([5,4,3,2,1]), [(1,4),(0,1),(1,3)])

    def test_random_input_within_constraints(self):
        for i in range(100):
            data = [random.randint(1, int(10e2)) for _ in range(random.randint(1,int(10e2)))]
            print(f"Starting test case {i}, len data: {len(data)}")
            self.assertEqual(build_heap(data), build_heap_(data))
    

                    
if __name__ == "__main__":
    unittest.main()