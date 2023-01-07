# n = n * 10 + 7の法則性はある

# https://qiita.com/puple_cat/items/2e89b54cee25837b4e1e
# 割り切れない場合の判定が分からなかった。
# これは、余りの法則があり、実際に試しで計算すると分かるが、余りがあるところを境に繰り返すことになる
# そのある値ががKになる

K = int(input())

# 1の位が 偶数・5の時は割り切れない
if K % 2 == 0 or K % 5 == 0:
  print(-1)
  exit()

num = 0
result = -1

for i in range(K):
  num = num * 10 + 7
  if num % K == 0:
    result = i + 1
    break

print(result)