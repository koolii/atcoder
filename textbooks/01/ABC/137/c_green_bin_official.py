from collections import defaultdict

# 入力のサイズ
N = int(input())

# num[s] 文字列sが何個あるか度数分布
num = defaultdict(int)

for i in range (N):
  # 入力の文字列をソートする
  s = "".join(sorted(input()))

  # インクリメント
  num[s] += 1

# 集計
result = 0

for s in num:
  # 文字列sがn個ある
  n = num[s]

  # nC2を足していく
  result += n * (n - 1) // 2

# 出力
print(result)