N = int(input())
dict = {};

for _ in range(N):
  dict[int(input())] = True

print(N)
print(len(dict.keys()))