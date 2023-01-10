N, M, Q = map(int, input().split())

# 頂点(問題的には1から始まっている)
G = [[] for i in range(N)]

for i in range(M):
  u, v = map(int, input().split())

  # 問題的に1スタートな為、0スタートに治す
  u -= 1
  v -= 1

  # グラフに辺を追加
  G[u].append(v)
  G[v].append(u)

# 各頂点の色を取得
colors = list(map(int, input().split()))

for i in range(Q):
  # tは 1 or 2
  # yは値が存在する、しないが存在する
  t, x, *y = map(int, input().split())

  # ValueError: not enough values to unpack (expected 3, got 2)
  # t, x, y = map(int, input().split())

  # 問題的に1スタートな為、0スタートに治す
  x -= 1

  # i番目のクエリーを実行する時の、現在地の色を出力させる
  print(colors[x])

  if t == 1:
    for v in G[x]:
      colors[v] = colors[x]
  else:
    colors[x] = y[0]
