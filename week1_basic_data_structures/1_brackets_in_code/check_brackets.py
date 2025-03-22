# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> str:
    """
    Checks for the first mismatched or unmatched bracket in a string.

    Args:
        text (str): The input string containing brackets.

    Returns:
        str: The 1-based index of the first mismatch or "Success" if all brackets are balanced.
    """
    opening_brackets_stack: list[str] = []
    opening_brackets_index: list[int] = []

    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket
            opening_brackets_stack.append(char)
            opening_brackets_index.append(i)
        elif char in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return str(i + 1)
            if not are_matching(opening_brackets_stack[-1], char):
                return str(i + 1)
            opening_brackets_stack.pop()
            opening_brackets_index.pop()

    return "Success" if not opening_brackets_stack else str(opening_brackets_index[-1] + 1)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
