# python3

import sys
from collections import namedtuple
from random import randint

Answer = namedtuple('answer_type', 'i j len')

def solve_(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

class Substring:
	def __init__(self, base_hashes: list[list[int]], base_powers: list[list[int]], index:int, k:int,
			  primes: list[int], x: int):
		self.index: int = index
		self.length: int = k
		self.hashes = self.computeHashes(base_hashes, base_powers, primes)

	def computeHashes(self, base_hashes: list[list[int]], base_powers: list[list[int]], primes: list[int]):
		result: list[int] = []
		a, l= self.index, self.length
		for i, hashes in enumerate(base_hashes):
			X = base_powers[i]
			p = primes[i]
			result.append(
				(((hashes[a+l] - X[l] * hashes[a]) % p) + p) % p
			)
		return tuple(result)

	@staticmethod
	def compute_string_hash_prefixes(s: str, primes: list[int], x:int):
		# Compute the hashes and prefix sum of the string along with powers of x for the hashing function
		result: set[list[int]] = []
		powers: list[int] = []
		for p in primes:
			hashes: list[int] = [0] * (len(s) + 1)
			powersModP = [1] * (len(s) + 1)
			for i in range(1,len(s)+1):
				powersModP[i]= (powersModP[i-1] * x) % p
			for i in range(len(s)):
				hashes[i+1] = (hashes[i]*x + ord(s[i])) % p
			powers.append(powersModP)
			result.append(hashes)

		return result, powers

	
	def __hash__(self):
		return hash(self.hashes)
	def __eq__(self, other):
		return isinstance(other, Substring) and self.hashes == other.hashes
	
			
def solve(s,t):
	ans: Answer = Answer(0,0,0)
	left, right = 0, len(t)
	primes: list[int] = [10**9 + 7, 10**9 + 9]
	x: int = randint(1, 10 ** 9)
	sPrefixes, sPowers = Substring.compute_string_hash_prefixes(s, primes, x)
	tPrefixes, tPowers = Substring.compute_string_hash_prefixes(t, primes, x)
	while left <= right:
		k = (left + right) // 2
		s_substring_hashes: set[Substring] = set()
		for i in range(len(s) - k + 1):
			s_substring_hashes.add(
				Substring(sPrefixes, sPowers, i, k, primes, x )
			)
		found = False
		for i in range(len(t) - k + 1):
			candidate: Substring = Substring(tPrefixes, tPowers, i, k, primes, x)
			if candidate in s_substring_hashes:
				left = k + 1
				for ss in s_substring_hashes:
					if candidate == ss:
						found = True
						ans = Answer(ss.index, candidate.index, candidate.length)
						break
				if found: break
		if not found: right = k - 1
	
	return ans


if __name__ == "__main__":
	for line in sys.stdin.readlines():
		s, t = line.split()
		ans = solve(s, t)
		print(ans.i, ans.j, ans.len)