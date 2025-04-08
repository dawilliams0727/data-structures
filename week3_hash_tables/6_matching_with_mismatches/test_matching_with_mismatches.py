import unittest
from matching_with_mismatches import solve

class TestDatum:
    def __init__(self, mismatches: int, text:str, pattern: str, expected: list[int]):
        self.k: int = int(mismatches)
        self.text: str = text
        self.pattern: str = pattern
        self.expected: list[int] = expected

class TestMisMatch(unittest.TestCase):
    def setUp(self):
        self.testData: list[TestDatum] = []
        input: str = [
            "0 ababab baaa",
            "1 ababab baaa", 
            "1 xabcabc ccc",
            "2 xabcabc ccc",
            "3 aaa xxx"
        ]
        output: list[list[int]] = [
            [],
            [1],
            [],
            [1, 2, 3, 4],
            [0]
        ]

        for i in range(len(input)):
            m, t, p = input[i].split(" ")
            e = output[i]
            self.testData.append(
                TestDatum(m,t,p,e)
            )

    def test_mismatch(self):
        for test in self.testData:
            self.assertEqual(solve(test.k, test.text, test.pattern), test.expected) 

if __name__ == "__main__":
    unittest.main()