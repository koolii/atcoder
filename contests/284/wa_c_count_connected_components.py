from collections import defaultdict

N, M = map(int, input().split())

# 各頂点の接続箇所をカウント?
S = defaultdict(int)

# 頂点が検索が終了しているかどうか
edge = []

# グラフの数
cnt = 0

# 頂点のリレーションを管理
dict = {}

for i in range(M):
  u, v = map(int, input().split())
  emin, emax = min(u, v), max(u, v)

  if min(u, v) in dict.keys():
    dict[emin].append(emax)
  else:
    dict[emin] = [emax]

print(dict)

for x in range(N):
  i = x + 1
  if i in dict.keys():
    if not i in edge:
      edge.append(i)
      cnt += 1

    arr = dict[i]

    for j in range(len(arr)):
      if not arr[j] in edge:
        edge.append(arr[j])
  elif i in edge:
    continue
  else:
    cnt += 1

print(cnt)