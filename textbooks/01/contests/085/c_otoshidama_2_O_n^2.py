# 変数を3つ同時に動かすのではなく、1つか2つのみ動かして考える
# 今回は、3つの変数a,b,cの内a,bのみを動かしてみる
# a + b + c = Nという制約のため、 c = N - a - bが成立する
# これを使うと、 for c in range(N + 1)のループを消せる
# 最終的に O(N^3) => O(N^2) になる

# 上記を素にプログラムを作成してみた

N, Y = map(int, input().split())

ares, bres, cres = -1, -1, -1

for a in range(N + 1):
  for b in range(N + 1):
    c = N - a - b
    # (反省点)cを算出する時に、billが必ずNが成立することが前提となるため、bill変数はもう必要なかった
    bill = a + b + c
    price = 10000 * a + 5000 * b + 1000 * c

    # a, bが N+1回ループすることで負の値になることがある
    if c < 0:
      continue

    if bill == N and price == Y:
      ares, bres, cres = a, b, c

print(ares, bres, cres)


# 改良版

N, Y = map(int, input().split())

ares, bres, cres = -1, -1, -1

for a in range(N + 1):
  for b in range(N + 1):
    c = N - a - b
    price = 10000 * a + 5000 * b + 1000 * c

    if c >= 0 and price == Y:
      ares, bres, cres = a, b, c

print(ares, bres, cres)