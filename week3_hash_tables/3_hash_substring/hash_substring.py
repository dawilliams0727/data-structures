# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]
def polyHash(S: str, p: int, x: int):
    """
        Compute Hash of string using function from Polynomial Hash Family

        Args:
            S (str): the string to calculate hash value of
            p (int): a large prime number greater than the cardinality of the hashing function
            x (int): a prime number less than p
        
        
        Returns:
            int: the hash value of the input string
    """
    hash: int = 0
    i = len(S) - 1
    while i >= 0:
        hash = ((hash * x) + ord(S[i])) % p
        i -= 1
    return hash

def precomputeHash(T: str, P: str, p:int, x:int):
    """
        Precompute hashes H of each substring equal to the length of pattern P in text S using recurrence relation
        between H(i) and H(i+1)

        Args:
            T (str): the text to precompute the hashes for
            P (str): the pattern that is being searched for
            p (int): a prime number larger than the cardinatlity of the hashing table used
            x (int): a prime number less than p

        Returns:
            list[int]: list of hashses for each substring equal to the length of the pattern P 
    """    
    lenT, lenP = len(T), len(P)
    H: list[int] = [-1] * (lenT - lenP + 1)
    S: str = T[lenT-lenP: lenT]
    H[lenT-lenP] = polyHash(S,p,x)
    y: int = 1
    for _ in range(1, lenP+1):
        y = (y*x)%p
    for i in range(lenT-lenP-1, -1, -1):
        H[i] = ((x*H[i+1]) + ord(T[i]) - (y * ord(T[i + lenP]))) % p
    return H

def get_occurrences(pattern, text):
    """
        Use Rabin Karp algorithm to search for a pattern in some text

        Args:
            pattern (str): the pattern to search for in the text
            text (str): the text to search for
        Returns:
            list[int]: starting indices of each occurrence of the pattern in the text
    """
    p: int = 1000000007
    x: int = 263
    pHash: int = polyHash(pattern, p, x)
    hashes: list[int] = precomputeHash(text, pattern, p, x)
    positions: list[int] = []
    for i in range(len(text)-len(pattern)+1):
        if pHash != hashes[i]:
            continue
        check: str = text[i: i+len(pattern)]
        if pattern == check:
            positions.append(i)
    return positions

    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

