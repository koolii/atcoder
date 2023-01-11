N, Q = map(int, input().split())
S = input()

cs = [0] * (N+1)

# 累積和を求める
for i in range(1, N + 1):
  if i == N + 1:
    # 最後の要素は S[i+1] を算出できないため、そのままの値を継承する
    cs[i] = cs[i - 1]
  else:
    cs[i] = cs[i - 1] + (S[i-1:i+1] == "AC")

# print(S, cs)

for q in range(Q):
  l, r = map(int, input().split())
  # 0ベースに揃える
  print(cs[r - 1] - cs[l - 1])