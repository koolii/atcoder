# O(N^2)
INF = 2 ** 30

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

minimum_dist = INF

for i in range(N):
  for j in range(i + 1, N):
    # i番目の点とj番目の点の距離の二乗を求める
    # ※ 二乗にするからdx,dyが0以下になろうと関係ないと考えている
    dx, dy = x[i] - x[j], y[i] - y[j]
    dist = dx ** 2 + dy ** 2

    # 最小値を更新
    minimum_dist = min(minimum_dist, dist)

print(minimum_dist)