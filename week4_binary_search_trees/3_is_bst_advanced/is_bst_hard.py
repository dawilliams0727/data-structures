#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if not tree:
    return True
  # Implement correct algorithm here
  def recursive(index, tMin, tMax):
    if index == -1:
      return True
    key, left, right = tree[index]
    if not (tMin <= key < tMax):
      return False
    return recursive(left, tMin, key) and recursive(right, key, tMax)
  
  return recursive(0, float("-inf"), float("inf"))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

