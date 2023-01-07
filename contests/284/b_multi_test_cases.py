T = int(input())

for _ in range(T):
  N = int(input())
  nums = list(map(int, input().split()))

  cnt = 0

  for i in range(N):
    if nums[i] % 2 == 1:
      cnt += 1

  print(cnt)

