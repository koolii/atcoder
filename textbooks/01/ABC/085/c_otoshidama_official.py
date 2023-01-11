# textbook

N, Y = map(int, input().split())

ares, bres, cres = -1, -1, -1

# 全探索
for a in range(N + 1):
  for b in range(N + 1):
    # cの値が自動的に決定する
    c = N - a - b

    # cが0以上N以下でない場合はスキップ
    if c < 0 or c > N:
      continue

    # 残りの条件を満たすかを判定
    if 10000 * a + 5000 * b + c * 1000 == Y:
      ares, bres, cres = a, b, c

print(ares, bres, cres)