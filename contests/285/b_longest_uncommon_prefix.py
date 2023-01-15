# Result: TLE
# N = int(input())
# S = input()
# for i in range(1, N):
#   l = 0
#   for j in range(N - i):
#     # print("case", "left", j, "right", j + i, S[j], S[j + i])
#     if S[j] == S[j + i]:
#       l = j
#       break
#     elif S[j] != S[j + i]:
#       l = j + 1
#   print(l)

# Result: AC
N = int(input())
S = input()
for i in range(1, N):
  l = N - i
  for j in range(N - i):
    if S[j] == S[j + i]:
      l = min(l, j)
      break
  print(l)