import unittest
import os
from .hash_chains import QueryProcessor_, QueryProcessor, Query

class TestData:
    def __init__(self, test_number: int, num_buckets: int, n: int, queries: list[str]):
        self.test_number: int = int(test_number)
        self.num_buckets: int = int(num_buckets)
        self.num_queries: int = int(n)
        self.queries = [Query(query=q.split()) for q in queries]
        self.result: list[str] | None

class TestHashChains(unittest.TestCase):
    def setUp(self):
        self.test_data: list[TestData] = []
        dir: str = os.path.dirname(__file__)
        test_folder: str = os.path.join(dir, "tests")
        tempResults: dict[int, str] = {}

        for filename in os.listdir(test_folder):
            filepath: str = os.path.join(test_folder, filename)
            with open(filepath, "r") as file:
                if filepath.endswith(".a"):
                    lines = file.readlines()
                    tempResults[int(filename.split(".")[0])] = [r.strip("\n") for r in lines]
                else:
                    lines = file.readlines()
                    num_buckets, num_queries = map(int,lines[:2])
                    queries = [s.strip("\n") for s in lines[2:]]
                    self.test_data.append(TestData(
                        filename, num_buckets, num_queries, queries
                    ))
        for test in self.test_data:
            test.result = tempResults[test.test_number]
        del(tempResults)

    def test_naive_imp(self):
        for test in self.test_data:
            proc: QueryProcessor_ = QueryProcessor_(test.num_buckets)
            actual: list[str] = []
            for i in range(test.num_queries):
                result = proc.process_query(test.queries[i])
                if result != None:
                    actual.append(result)
            self.assertEqual(actual, test.result)

    def test_chain_imp(self):
        for test in self.test_data:
            proc: QueryProcessor = QueryProcessor(test.num_buckets)
            actual: list[str] = []
            for i in range(test.num_queries):
                result = proc.process_query(test.queries[i])
                if result != None:
                    actual.append(result)
            self.assertEqual(actual, test.result)