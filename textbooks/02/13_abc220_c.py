# link: https://atcoder.jp/contests/abc220/tasks/abc220_c
# problem: Long Sequence

N = int(input())
A = list(map(int, input().split()))
X = int(input())

# 一周分の合計(sum)を求めると、何回ループすれば一番Xに近いかわかる
# ループ数はXをsumで割った時の商の数でOK
sum = 0
for ai in A:
  sum += ai

count = (X // sum)
num = sum * count
ans = count * len(A)
# print("sum", sum, "count", count, len(A), ans)

# 次の商に行くまでにXの値を超えることはわかっているので、
# 最悪一周分ループを回して、項数を足し合わせながら進めていく
for ai in A:
  num += ai
  ans += 1
  if num > X:
    break

print(ans)
