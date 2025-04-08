# python3
from random import randint
import sys

def rollingPolyHash(s: str, x: int, p: int) -> list[int]:
    hashPrefixes: list[int] = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashPrefixes[i + 1] = (hashPrefixes[i] * x + ord(s[i])) % p
    return hashPrefixes

def substringHash(hashPrefixes, powers, startIndex, length, p):
    """Returns the hash of hashPrefixes substring [startIndex : startIndex+length)."""
    # substring is from startIndex to startIndex+length-1
    endIndex = startIndex + length  # non-inclusive
    beginningToEnd = hashPrefixes[endIndex]
    justBeginning = hashPrefixes[startIndex]
    xRaisedToLength = powers[length]
    return (beginningToEnd - xRaisedToLength * justBeginning) % p

def solve(k, text, pattern):
    ans = []
    if not pattern or k < 0:
        return ans

    prime = 10**9 + 7
    x = randint(1, 10**9)

    # Powers up to max possible length
    max_len = max(len(text), len(pattern))
    powers = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        powers[i] = (powers[i - 1] * x) % prime

    # Quick sanity test
    test1 = rollingPolyHash("abc", x, prime)
    test2 = rollingPolyHash("bc", x, prime)
    a = substringHash(test1, powers, 1, 2, prime)  # "bc"
    b = substringHash(test2, powers, 0, 2, prime)  # "bc"
    assert a == b

    textPrefixes = rollingPolyHash(text, x, prime)
    patternPrefixes = rollingPolyHash(pattern, x, prime)
    patLen = len(pattern)
    txtLen = len(text)

    # For each candidate position
    for i in range(txtLen - patLen + 1):
        mismatches = 0
        # We repeatedly try to find up to k mismatches
        # We'll "search" from l=0 to r=patLen-1
        l, r = 0, patLen - 1
        while l <= r and mismatches <= k:
            left, right = l, r
            mismatchPos = -1

            # Binary-search for next mismatch in [l..r]
            while left <= right:
                mid = (left + right) // 2
                length = (mid - l + 1)

                # Compare text[i + l .. i + mid] vs pattern[l .. mid]
                hashText = substringHash(textPrefixes, powers, i + l, length, prime)
                hashPat = substringHash(patternPrefixes, powers, l, length, prime)

                if hashText == hashPat:
                    # No mismatch in [l..mid], search [mid+1..r]
                    left = mid + 1
                else:
                    # Mismatch somewhere in [l..mid]; record position and shrink range
                    mismatchPos = mid
                    right = mid - 1

            if mismatchPos == -1:
                # Means we found no mismatch in [l..r], so we are done checking
                break

            # We found exactly one mismatch at mismatchPos
            mismatches += 1
            if mismatches > k:
                break

            # Next check the remainder beyond mismatchPos
            l = mismatchPos + 1  # skip the mismatch character

        if mismatches <= k:
            ans.append(i)

    return ans

if __name__ == "__main__":
    for line in sys.stdin:
        k, t, p = line.split()
        ans = solve(int(k), t, p)
        print(len(ans), *ans)
