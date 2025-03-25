import random
import os
import unittest
import merging_tables

class TestMergingTables(unittest.TestCase):
    def setUp(self):
        test_dir = os.path.join(os.path.dirname(__file__),'tests')
        self.test_files = [f for f in os.listdir(test_dir)]
        self.tables = [[1,1,1,1,1],
                    [10,0,5,0,3,3]
                    ]
        self.merges = [[(3,5),(2,4),(1,4),(5,4),(5,3)],
                    [(6,6),(6,5),(5,4),(4,3)]
                    ]
        self.maxes = [[2,2,3,5,5],
                    [10,10,10,11]
                    ]

        for file_name in self.test_files:
            with open(os.path.join(test_dir, file_name)) as file:
                lines = file.readlines()
                if file_name.endswith('.a') == False:
                    n, m = map(int, lines[0].split())
                    row_counts = list(map(int, lines[1].split()))
                    self.tables.append(row_counts)
                    merges = []
                    for i in range(2, 2+m):
                        dst, src = map(int, lines[i].split())
                        merges.append((dst, src))
                    self.merges.append(merges)
                else:
                    self.maxes.append([int(maxCount) for maxCount in lines])

    def test_merge_tables(self):
        for i in range(len(self.tables)):
            actual = []
            db = merging_tables.Database(self.tables[i])
            for j, merge in enumerate(self.merges[i]):
                db.merge(merge[0] - 1, merge[1] - 1)
                actual.append(db.max_row_count)
            self.assertEqual(actual, self.maxes[i])






if __name__ == '__main__':
    unittest.main()