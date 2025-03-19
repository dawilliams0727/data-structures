# python3

import sys
import threading

class Node():
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent if parent != -1 else None
        self.children = []

def compute_height(n: int, parents: list[int]):
    nodes = [Node(i, parents[i]) for i in range(n)]
    root = None
    for node in nodes:
        if node.parent != None:
            nodes[node.parent].children.append(nodes[node.n])
        else:
            root = node

    def recursive(node):
        height = 0
        if len(node.children) == 0:
            return 1
        for child in node.children:
            height = max(height, recursive(child))
        return 1 + height
    
    return recursive(root)

def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

"""if __name__ == "__main__":
    main()"""