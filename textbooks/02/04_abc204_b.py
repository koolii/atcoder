# link: https://atcoder.jp/contests/abc204/tasks/abc204_b

N = int(input())
A = list(map(int, input().split()))
cnt = 0

for i in range(N):
  left = A[i] - 10
  if left > 0:
    cnt += left

print(cnt)