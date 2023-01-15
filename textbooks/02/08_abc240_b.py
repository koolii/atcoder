# link: https://atcoder.jp/contests/abc240/tasks/abc240_b
# count distinct integers

from collections import defaultdict

# 自己実装
N = int(input())
a = list(map(int, input().split()))

num = defaultdict(int)

for i in range(N):
  num[a[i]] += 1

print(len(num))

# 模範解答(Setを使っている)
# N = int(input())
# a = list(map(int, input().split()))
# aSet = set(a)
# print(len(aSet))
