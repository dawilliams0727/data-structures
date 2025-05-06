#!/usr/bin/env python3

import unittest
from is_bst import IsBinarySearchTree

class TestDatum:
    def __init__(self, tree: list[list[int]], expected: bool):
        # tree is a list of [key, left_index, right_index]
        self.tree = tree
        # expected == True  → CORRECT; False → INCORRECT
        self.expected = expected

class TestIsBST(unittest.TestCase):
    def setUp(self):
        """Test data generated with ChatGPT o1 mini high
        """
        self.testData = [
            # empty tree
            TestDatum([], True),

            # single node
            TestDatum([[10, -1, -1]], True),

            # perfect small BST
            TestDatum([
                [2, 1, 2],
                [1, -1, -1],
                [3, -1, -1],
            ], True),

            # right child equals root → not allowed under strict
            TestDatum([
                [2, 1, 2],
                [1, -1, -1],
                [2, -1, -1],
            ], False),

            # left‐subtree violation: 5 in left of 4
            TestDatum([
                [4, 1, 2],
                [2, 3, 4],
                [6, -1, 5],
                [1, -1, -1],
                [3, -1, -1],
                [7, -1, -1],
            ], True),

            # deeper violation: 5 in left subtree of 4
            TestDatum([
                [4, 1, 2],
                [2, 3, 4],
                [6, -1, 5],
                [1, -1, -1],
                [5, -1, -1],  # <-- 5 is not < 4
                [7, -1, -1],
            ], False),

            # chain to the right only, strictly increasing
            TestDatum([
                [1, -1, 1],
                [2, -1, 2],
                [3, -1, -1],
            ], True),

            # chain to the left only, strictly decreasing
            TestDatum([
                [3, 1, -1],
                [2, 2, -1],
                [1, -1, -1],
            ], True),
        ]

    def test_strict_bst(self):
        for datum in self.testData:
            with self.subTest(tree=datum.tree):
                result = IsBinarySearchTree(datum.tree)
                self.assertEqual(
                    result,
                    datum.expected,
                    msg=f"\nTree: {datum.tree}\nExpected: {datum.expected} but got: {result}"
                )

if __name__ == "__main__":
    unittest.main()
