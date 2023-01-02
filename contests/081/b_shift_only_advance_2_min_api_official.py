# P94 textbook

def how_many_times(num):
  count = 0

  while num % 2 == 0:
    count += 1
    num //= 2

  return count

INF = 2 ** 30
result = INF
N = int(input())
A = list(map(int, input().split()))

for a in A:
  # 配列全件の2で割った時の回数を求める
  cnt = how_many_times(a)
  # resultよりcntの方が小さい場合は更新する
  result = min(result, cnt)

print(result)