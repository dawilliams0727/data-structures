import os
import unittest
from .hash_substring import get_occurrences_, get_occurrences

class TestDatum:

    def __init__(self, id: int, pattern: str, text: str, occurences: list[int] = None):
        self.id: int = id
        self.pattern: str = pattern
        self.text: str = text
        self.occurences: list[int] = occurences


class TestHashSubstring(unittest.TestCase):
    def setUp(self):
        self.testData: list[TestDatum] = []
        tempOccurences: dict[int, list[int]] = {}
        test_dir = os.path.join(os.path.dirname(__file__), "tests")

        for filename in os.listdir(test_dir):
            filepath: str = os.path.join(test_dir, filename)
            fileId: int = int(filename.split(".")[0])
            with open(filepath, "r") as file:
                if not filepath.endswith(".a"):
                    lines = file.readlines()
                    self.testData.append(
                        TestDatum(int(filename.split(".")[0]), lines[0].rstrip("\n"), lines[1].rstrip("\n"))
                    )
                else:
                    lines = file.readline().split(" ")
                    tempOccurences[fileId] = list(map(int, lines))
        for datum in self.testData:
            datum.occurences = tempOccurences[datum.id]

    def test_naive(self):
        for test in self.testData:
            self.assertEqual(get_occurrences_(test.pattern, test.text), test.occurences)


    def test_get_occurences(self):
        for test in self.testData:
            self.assertEqual(get_occurrences(test.pattern, test.text), test.occurences)