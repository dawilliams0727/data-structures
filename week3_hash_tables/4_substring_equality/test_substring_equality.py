import os
import unittest
from random import randint
from math import pow
from substring_equality import Solver

class TestDatum:
    def __init__(self, string: str, queries: list[tuple[int,int,int]], results: list[str]):
        self.string: str = string
        self.queries: list[tuple] = queries
        self.results: list[str] = results

class TestSubstringEquality(unittest.TestCase):
    def setUp(self):
        self.testData: list[TestDatum] = []
        self.testData.append(
            TestDatum(
                string = "abacabadabacaba",
                queries = [(0,0,7),(2,4,3),(3,5,1),(1,3,2)],
                results = ["Yes", "No", "No", "No"]
            )
        )
        self.testData.append(
            TestDatum(
                string = "abacabadabacaba",
                queries = [(0,4,3),(1,9,5)],
                results = ["Yes", "Yes"]
            )
        )
        self.testData.append(
            TestDatum(
                string = "trololo",
                queries = [(0,0,7),(2,4,3),(3,5,1),(1,3,2)],
                results = ["Yes", "Yes", "Yes", "No"]
            )
        )
        self.testData.append(
            TestDatum(
                string = "a",
                queries = [(0,0,1)],
                results = ["Yes"]
            )
        )
        self.testData.append(
            TestDatum(
                string = "abababab",
                queries = [(0,2,2),(4,6,2),(1,3,2),(3,5,2)],
                results = ["Yes", "Yes", "Yes", "Yes"]
            )
        )
        self.testData.append(
            TestDatum(
                string = "aaaaaaaaaa",
                queries = [(0,1,8)],
                results = ["Yes"]
            )
        )
    
    def test_substring_equality(self):
        for test in self.testData:
            solver = Solver(test.string)
            actual: list[str] = []
            for query in test.queries:
                a, b, l = query
                actual.append("Yes" if solver.ask(a, b, l) else "No")
            self.assertEqual(actual, test.results)

if __name__ == "__main__":
    unittest.main()