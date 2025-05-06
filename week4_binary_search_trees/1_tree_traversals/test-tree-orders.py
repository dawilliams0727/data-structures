import os
import unittest
from tree_orders import TreeOrders
from collections import namedtuple

Traversals = namedtuple("Traversals", ["inOrder", "preOrder", "postOrder"])

class TestDatum:
    def __init__(self, treeOrder: TreeOrders, expected: Traversals):
        self.treeOrder: TreeOrders = treeOrder
        self.expected: Traversals = expected

class TestTreeOrders(unittest.TestCase):
    def setUp(self):
        thisDir: str = os.path.dirname(__file__)
        testFolder: str = os.path.join(thisDir, "tests")
        self.testData: list[TestDatum] = []
        
        for filename in os.listdir(testFolder):
            if not filename.endswith(".a"):
                filepath: str = os.path.join(testFolder, filename)
                with open(filepath, "r") as file:
                    treeOrder: TreeOrders = TreeOrders()
                    treeOrder.n = int(file.readline())
                    treeOrder.key = [0 for i in range(treeOrder.n)]
                    treeOrder.left = [0 for i in range(treeOrder.n)]
                    treeOrder.right = [0 for i in range(treeOrder.n)]
                    for i in range(treeOrder.n):
                        [a,b,c] = map(int, file.readline().split())
                        treeOrder.key[i] = a
                        treeOrder.left[i] = b
                        treeOrder.right[i] = c
                    with open(f"{filepath}.a", "r") as result:
                        inOrder: list[int] = list(map(int, result.readline().split()))
                        preOrder: list[int] = list(map(int, result.readline().split()))
                        postOrder: list[int] = list(map(int, result.readline().split()))
                        self.testData.append(TestDatum(
                            treeOrder = treeOrder,
                            expected = Traversals(inOrder, preOrder, postOrder)
                        ))
    def test_in_order_traversal(self):
        for test in self.testData:
            treeOrder = test.treeOrder
            expected = test.expected.inOrder
            self.assertEqual(treeOrder.inOrder(), expected)

    def test_pre_order_traversal(self):
        for test in self.testData:
            treeOrder = test.treeOrder
            expected = test.expected.preOrder
            self.assertEqual(treeOrder.preOrder(), expected)

    def test_post_order_traversal(self):
        for test in self.testData:
            treeOrder = test.treeOrder
            expected = test.expected.postOrder
            self.assertEqual(treeOrder.postOrder(), expected)

if __name__ == "__main__":
    unittest.main()