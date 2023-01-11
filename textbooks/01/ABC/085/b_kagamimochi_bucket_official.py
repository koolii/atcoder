# バケットのサイズ
M = 101
# バケット(全体を0で初期化)
exist = [0] * M

N = int(input())

for i in range(N):
  d = int(input())

  exist[d] = 1

# existの総和を求めて出力する
print(sum(exist))