from collections import defaultdict

N = int(input())

words = []

for i in range (N):
  S = defaultdict(int)

  # 度数分布を作成
  chars = list(input())
  for c in chars:
    S[c] += 1

  for j in range(N - i - 1):


for _ in range(N):
  words.append(input())

for w in words:
  for c in w:
    print(c)