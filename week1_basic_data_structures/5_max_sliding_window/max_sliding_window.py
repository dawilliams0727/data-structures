# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_windows_dequeue(sequence, m):
    if not sequence or m == 0:
        return []
    
    left, right = 0, 0
    # Stores indices of elements in decreasing order
    max_deque = deque()  
    result = []
    
    while right < len(sequence):
        # Remove elements from back that are smaller than the current element
        while max_deque and sequence[max_deque[-1]] <= sequence[right]:
            max_deque.pop()
        
        max_deque.append(right)
        
        # Remove elements from front if they are out of window
        if max_deque[0] < left:
            max_deque.popleft()
        



        # If the window has reached size m, record the maximum
        if right >= m - 1:
            result.append(sequence[max_deque[0]])  # Front of deque is max in window
            left += 1  # Move left pointer
        
        right += 1  # Move right pointer

    return result

def max_sliding_windows_stacks(sequence, n):
    stack1 = []
    stack1_max = []
    stack2 = []
    stack2_max = []
    result = []
    
    for item in sequence:
        if len(stack1) >= n:
            # move stack1 to stack2
            while stack1:
                popped = stack1.pop()
                if stack1_max and popped == stack1_max[-1]:
                    stack1_max.pop()
                stack2.append(popped)
                if stack2_max:
                    if stack2_max[-1] <= popped:
                        stack2_max.append(popped)
                else:
                    stack2_max.append(popped)
        if stack2: 
            popped = stack2.pop() # remove top element to make room for new item in stack 1
            if stack2_max and popped == stack2_max[-1]:
                stack2_max.pop() #remove maximum also
        stack1.append(item)# add to stack1
        if stack1_max:
            if stack1_max[-1] <= item:
                stack1_max.append(item) #update max
        else:
            stack1_max.append(item)
        max1 = stack1_max[-1] if stack1_max else float("-inf")
        max2 = stack2_max[-1] if stack2_max else float("-inf")
        if len(stack1) + len(stack2) >= n:
            result.append(max(max1, max2))

    return result

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_windows_dequeue(input_sequence, window_size))
    print(*max_sliding_windows_stacks(input_sequence, window_size))

