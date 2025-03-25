# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src: int, dst: int):
        """
        Merge two tables into one using rank heuristic.
        
        Args:
            src (int): index of source table.
            dst (int): index of destination table

        """
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # Decide which parent becomes the new root.
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            new_root, old_root = src_parent, dst_parent
        else:
            self.parents[src_parent] = dst_parent
            new_root, old_root = dst_parent, src_parent

        # If ranks were equal, increment the new root’s rank
        if self.ranks[src_parent] == self.ranks[dst_parent]:
            self.ranks[new_root] += 1

        # Add the old_root’s row_count into the new_root
        self.row_counts[new_root] += self.row_counts[old_root]
        self.row_counts[old_root] = 0

        self.max_row_count = max(self.row_counts[new_root], self.max_row_count)

        return True

    def get_parent(self, table: int) -> int:
        """
        Get parent of a table. Uses path compression to optimize the time complexity.
        """
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
