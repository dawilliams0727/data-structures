import unittest
import time
from .phone_book import process_queries, process_queries_, Query

class TestPhoneBook(unittest.TestCase):
    def setUp(self) -> None:
        self.queries: list[list[Query]] = []
        self.responses: list[list[str]] = []
        exampleInputs = [
           [ "add 911 police","add 76213 Mom","add 17239 Bob",
            "find 76213","find 910","find 911","del 910",
            "del 911","find 911","find 76213","add 76213 daddy",
            "find 76213"],["find 3839442","add 123456 me",
            "add 0 granny","find 0","find 123456","del 0",
            "del 0","find 0"
            ]
        ]
        exampleOutputs = [
            ["Mom", "not found", "police", "not found", "Mom", "daddy"],
            ["not found", "granny", "me", "not found"]
        ]
        for i in range(len(exampleInputs)):
            self.queries.append(
                [Query(q.split()) for q in exampleInputs[i]]
            )
            self.responses.append(
                exampleOutputs[i]
            )

    def test_native_implementation(self) -> None:
        naive_start = time.perf_counter()
        for i in range(len(self.queries)):
            self.assertEqual(process_queries_(self.queries[i]), self.responses[i])
        naive_time = time.perf_counter() - naive_start
        print(f"Naive Time: {naive_time}")

    def test_process_queries_with_example_data(self) -> None:
        fast_start = time.perf_counter()
        for i in range(len(self.queries)):
            self.assertEqual(process_queries(self.queries[i]), self.responses[i])
        fast_time = time.perf_counter() - fast_start
        print(f"Fast Time {fast_time}")
