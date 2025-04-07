# python3

import sys
from random import randint

class Solver:
	def __init__(self, s):
		self.s = s
		self.m1: int = 10**9 + 7
		self.m2: int = 10**9 + 9
		self.x: int = randint(1, 10**9)
		self.h1: list[int] = [0] * (len(s)+1)
		self.h2: list[int] = [0] * (len(s)+1)
		self.pows1: list[int] = [1] * (len(s))
		self.pows2: list[int] = [1] * (len(s))
		for i in range(1,len(s)):
			self.pows1[i] =(self.pows1[i-1] * self.x) % self.m1
			self.pows2[i] =(self.pows2[i-1] * self.x) % self.m2
		for i in range(len(s)):
			self.h1[i+1] = ((self.x * self.h1[i]) + ord(self.s[i])) % self.m1
			self.h2[i+1] = ((self.x * self.h2[i]) + ord(self.s[i])) % self.m2

	def ask(self, a, b, l):
		hashA1: int = ((((self.h1[a+l] - self.pows1[l] * self.h1[a]) % self.m1) + self.m1) % self.m1)
		hashB1: int = ((((self.h1[b+l] - self.pows1[l] * self.h1[b]) % self.m1) + self.m1) % self.m1)
		hashA2: int = ((((self.h2[a+l] - self.pows2[l] * self.h2[a]) % self.m2) + self.m2) % self.m2)
		hashB2: int = ((((self.h2[b+l] - self.pows2[l] * self.h2[b]) % self.m2) + self.m2) % self.m2)
		return hashA1 == hashB1 and hashA2 == hashB2

if __name__ == "__main__":
	s = sys.stdin.readline()
	q = int(sys.stdin.readline())
	solver = Solver(s)
	for i in range(q):
		a, b, l = map(int, sys.stdin.readline().split())
		print("Yes" if solver.ask(a, b, l) else "No")
