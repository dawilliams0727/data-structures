# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_brackets_index = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_brackets_index.append(i)
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return str(i+1)
            # check if popped matches the current characters compliment
            if not are_matching(opening_brackets_stack[-1], next):
                return str(i+1)
            else:
                opening_brackets_stack.pop()
                opening_brackets_index.pop()
            
    return "Success" if len(opening_brackets_stack) == 0 else str(opening_brackets_index[-1] + 1)

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
