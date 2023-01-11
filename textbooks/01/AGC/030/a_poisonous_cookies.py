A, B, C = map(int, input().split())

# Cを最後に1枚食べて、お腹を壊した状態で終了するため +1
# A:10, B:10, C:21 => 10 + 10 + 1, 21 => 31
if A + B + 1 <= C:
  print(2 * B + A + 1)
else:
  print(B + C)