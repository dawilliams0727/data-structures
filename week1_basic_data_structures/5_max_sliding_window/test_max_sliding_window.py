import unittest
from random import randint
from max_sliding_window import max_sliding_windows_dequeue, max_sliding_window_naive, max_sliding_windows_stacks

class TestMaxSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.tests = []
        self.answers = []
        print("preparing data")
        for _ in range(20): # random array
            array = [randint(0, int(10e5)) for _ in range(randint(1, int(10e3)))]
            m = randint(1, len(array))
            self.tests.append((array, m))
            self.answers.append(max_sliding_window_naive(array, m))
        print("finished random")
        for _ in range(10): # increasing array
            array = [i for i in range(randint(1, int(10e3)))]
            m = randint(1, len(array))
            self.tests.append((array, m))
            self.answers.append(max_sliding_window_naive(array, m))
        print("Finished increasing")
        for _ in range(10): # decreasing array
            n = randint(1, int(10e3))
            array = [n-i for i in range(n) ]
            m = randint(1, len(array))
            self.tests.append((array, m))
            self.answers.append(max_sliding_window_naive(array, m))
        print("finished decreasing")
        self.tests.append(([1,1,1,1,1,1], 3))
        self.answers.append(max_sliding_window_naive([1,1,1,1,1,1], 3))
        self.tests.append(([1,1,1,1,1,1], 6))
        self.answers.append(max_sliding_window_naive([1,1,1,1,1,1], 6))

    def test_deque_implementation(self):
        print("starting test_deque")
        for i, test in enumerate(self.tests):
            #print(f"{test}\nexpected{self.answers[i]}")
            self.assertEqual(max_sliding_windows_dequeue(test[0], test[1]), self.answers[i] )
    def test_stacks_implementation(self):
        print("starting test_stacks")
        for i, test in enumerate(self.tests):
            #print(f"{test}\nexpected{self.answers[i]}")
            self.assertEqual(max_sliding_windows_stacks(test[0], test[1]), self.answers[i] )
if __name__ == "__main__":
    unittest.main()