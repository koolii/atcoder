# link: https://atcoder.jp/contests/abc234/tasks/abc234_b
# problem: Longest Segment

from math import sqrt

N = int(input())
points = [list(map(int, input().split())) for i in range(N)]
ans = 0

for i in range(N-1): # for i in range(N) と
  for j in range(1, N-i): # for j in range(1+i, N) でもOK
    dx = abs(points[i][0] - points[i+j][0])
    dy = abs(points[i][1] - points[i+j][1])
    # print(points[i], points[i + j], dx, dy, sqrt(dx + dy))
    ans = max(ans, sqrt(dx ** 2 + dy ** 2))

print(ans)

