# python3


def build_heap_(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def build_heap(data: list[int]) -> list[tuple[int,int]]:
    """
    Convert an array of integers into a 0-indexed min-heap
    
    Args:
        data (list[int]): the array of integers to be sorted
    Returns:
    l   list[tuple[int,int]]: A list of tuples containing indices for each pair of elements to be swapped
    """
    swaps = []
    # functions for getting parents and children
    def get_parent(i: int) -> int:
        """
        Helper function that returns the parent of node i

        Args:
            i (int): index of node
        Returns:
            int: the index of the parent of node i
        """
        return i // 2
    
    def get_left_child(i: int) -> int:
        """
        Helper function that returns the left child of node i

        Args:
            i (int): index of node
        Returns:
            int: the index of the left child of node i
        """
        return (i * 2) + 1
    
    def get_right_child(i: int) -> int:
        """
        Helper function that returns the right child of node i

        Args:
            i (int): index of node
        Returns:
            int: the index of the right child of node i
        """
        return (i * 2) + 2
    
    # sift down function
    def siftdown(i: int) -> None:
        """
        Moves node down a binary heap if its value is larger than it's children

        Args:
            i (int): the node to consider sifting down

        Returns:
            None
        """
        # keep track of the smallest element
        minIndex = i
        left = get_left_child(i)
        # if there is a left child and it is 
        if left < len(data) and data[left] < data[minIndex]:
            minIndex = left
        right = get_right_child(i)
        if right < len(data) and data[right] < data[minIndex]:
            minIndex = right
        if i != minIndex:
            swaps.append((i, minIndex))
            data[minIndex], data[i] = data[i], data[minIndex]
            siftdown(minIndex)
    # iterate sift down on the first half of data starting from the furtherst right
    i = len(data) // 2
    while i >= 0:
        siftdown(i)
        i -= 1
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
