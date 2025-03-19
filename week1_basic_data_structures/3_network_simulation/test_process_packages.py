import unittest
import os
from collections import namedtuple
from process_packages import Buffer, process_requests


class TestProcessPackets(unittest.TestCase):
    def setUp(self):
        Request = namedtuple("Request", ["arrived_at", "time_to_process"])
        Response = namedtuple("Response", ["was_dropped", "started_at"])
        TestInput = namedtuple("TestInput", ["buffer_size", "requests"])

        self.test_files = []
        self.answer_files = []
        tests_folder = os.path.join(os.path.dirname(__file__), "tests")
        for filename in os.listdir(tests_folder):
            
            filepath = os.path.join(tests_folder, filename)
            if filename.endswith('.a'):
                with open(filepath, 'r') as file:
                    results = list(map(int,file.readlines()))
                    self.answer_files.append(results)
            else:
                with open(filepath, 'r') as file:
                    buffer_size, num_packets = list(map(int,file.readline().split()))
                    requests = []
                    for _ in range(num_packets):
                        arrived_at, time_to_process = list(map(int,file.readline().split()))
                        requests.append(Request(arrived_at, (time_to_process)))
                    self.test_files.append(TestInput(buffer_size, requests))

    def test_provided_inputs(self):
        i = 0
        for testdata in self.test_files:
            
            buffer_size = testdata.buffer_size
            buffer = Buffer(buffer_size)
            requests = testdata.requests
            responses = []
            for response in process_requests(requests, buffer):
                responses.append(response.started_at if not response.was_dropped else -1)
            #print(f"{i+1}.) Buffer Size: {buffer_size} Requests: {requests}")
            self.assertEqual(responses, self.answer_files[i])
            i += 1

if __name__ == "__main__":
    unittest.main()