#!/usr/bin/env python3
import unittest
from is_bst_hard import IsBinarySearchTree

class TestDatum:
    def __init__(self, tree: list[list[int]], expected: bool, name: str):
        # tree: each node is [key, left_index, right_index]
        self.tree = tree
        # expected == True → CORRECT; False → INCORRECT
        self.expected = expected
        self.name = name

class TestIsBSTWithDuplicates(unittest.TestCase):
    def setUp(self):
        self.testData = [
            # empty tree
            TestDatum([], True, "empty tree"),

            # single-node tree
            TestDatum([[42, -1, -1]], True, "single node"),

            # simple strict BST
            TestDatum([
                [2, 1, 2],
                [1, -1, -1],
                [3, -1, -1],
            ], True, "simple 3-node BST"),

            # duplicate on right child — now allowed
            TestDatum([
                [2, 1, 2],
                [1, -1, -1],
                [2, -1, -1],  # equal to root, as right child
            ], True, "duplicate on right"),

            # duplicate on left child — still disallowed
            TestDatum([
                [2, 1, -1],
                [2, -1, -1],  # equal to root, but on left
            ], False, "duplicate on left"),

            # deeper: a duplicate far down the right subtree
            TestDatum([
                [5, 1, 2],
                [3, -1, -1],
                [5, -1, 3],  # right child equal
                [7, -1, -1],
            ], True, "duplicate deeper on right"),

            # deeper violation: a left-subtree node ≥ root
            TestDatum([
                [10, 1, 2],
                [5, 3, 4],
                [15, -1, -1],
                [1, -1, -1],
                [12, -1, -1],  # 12 in left subtree of 10
            ], False, "left-subtree violation"),

            # deeper violation: right-subtree node < root
            TestDatum([
                [10, 1, 2],
                [5, -1, -1],
                [12, -1, 3],
                [9, -1, -1],  # 9 in right subtree of 10
            ], False, "right-subtree violation"),

            # large chain of equals on the right — all allowed
            TestDatum([
                [1, -1, 1],
                [1, -1, 2],
                [1, -1, 3],
                [1, -1, -1],
            ], True, "chain of equal rights"),
        ]

    def test_bst_with_duplicates(self):
        for case in self.testData:
            with self.subTest(msg=case.name):
                result = IsBinarySearchTree(case.tree)
                self.assertEqual(
                    result, case.expected,
                    f"{case.name}:\n  tree = {case.tree}\n  expected = {case.expected}, got = {result}"
                )

if __name__ == "__main__":
    unittest.main()
