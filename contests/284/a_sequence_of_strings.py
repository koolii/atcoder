N = int(input())

sentences = []

for _ in range(N):
  sentences.append(input())

for i in range(N):
  print(sentences[(i + 1) * -1])