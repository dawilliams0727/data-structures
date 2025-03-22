# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_windows_dequeue(sequence: list[int], m: int) -> list[int]:
    """
    Computes the maximum value in every sliding window of size m using a deque.

    Args:
        sequence (list[int]): The input list of integers.
        m (int): The size of the sliding window.

    Returns:
        list[int]: List of maximum values for each window.
    """
    if not sequence or m == 0:
        return []

    left: int = 0
    right: int = 0
    max_deque: deque[int] = deque()  # Stores indices of elements in decreasing order
    result: list[int] = []

    while right < len(sequence):
        # Remove elements from back that are smaller than the current element
        while max_deque and sequence[max_deque[-1]] <= sequence[right]:
            max_deque.pop()

        max_deque.append(right)

        # Remove elements from front if they are out of the current window
        if max_deque[0] < left:
            max_deque.popleft()

        # Record the max value once the window reaches size m
        if right >= m - 1:
            result.append(sequence[max_deque[0]])
            left += 1  # Slide the window

        right += 1

    return result

def max_sliding_windows_stacks(sequence: list[int], n: int) -> list[int]:
    """
    Computes the maximum in every sliding window of size `n` using a two-stack queue method.

    Args:
        sequence (list[int]): The input sequence of integers.
        n (int): The size of the sliding window.

    Returns:
        list[int]: A list of the maximums for each window.
    """
    stack1: list[int] = []
    stack1_max: list[int] = []
    stack2: list[int] = []
    stack2_max: list[int] = []
    result: list[int] = []

    for item in sequence:
        # Maintain window size by shifting elements from stack1 to stack2 if needed
        if len(stack1) >= n:
            while stack1:
                popped = stack1.pop()
                if stack1_max and popped == stack1_max[-1]:
                    stack1_max.pop()
                stack2.append(popped)
                if not stack2_max or popped >= stack2_max[-1]:
                    stack2_max.append(popped)

        # Remove one from stack2 if total elements exceed window size
        if stack2 and len(stack1) + len(stack2) >= n:
            popped = stack2.pop()
            if stack2_max and popped == stack2_max[-1]:
                stack2_max.pop()

        # Push new item into stack1 and update max
        stack1.append(item)
        if not stack1_max or item >= stack1_max[-1]:
            stack1_max.append(item)

        # Compute window max
        if len(stack1) + len(stack2) >= n:
            max1 = stack1_max[-1] if stack1_max else float("-inf")
            max2 = stack2_max[-1] if stack2_max else float("-inf")
            result.append(max(max1, max2))

    return result


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_windows_dequeue(input_sequence, window_size))
    print(*max_sliding_windows_stacks(input_sequence, window_size))

