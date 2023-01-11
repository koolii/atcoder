# 5-8
N = int(input())

def check():
  # 前回分の(Ti, Xi, Yi)
  pt, px, py = 0, 0, 0

  for i in range(N):
    # i番目の(Ti, Xi, Yi)
    t, x, y = map(int, input().split())

    # 原点からの移動として処理する
    # Ti - Ti-1, Xi - Xi-1, Yi - Yi-1
    T, X, Y = abs(t - pt), abs(x - px), abs(y - py)

    # 行動範囲的に移動距離と経過時間的に移動可能かチェック
    if T < X + Y:
      return False

    # パリティチェック
    # 経過時間Tが奇数の時、(X + Y)は必ず奇数になる、偶数も同じ
    if T % 2 != (X + Y) % 2:
      return False

    # 現在地を更新する
    pt, px, py = T, X, Y

  return True

print("Yes" if check() else "No")