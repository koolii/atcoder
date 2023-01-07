H, W = map(int, input().split())
S = [input() for _ in range(H)]
Rounds = [
  # 左、上、右、下
  [-1, 0], [0, -1], [1, 0], [0, 1],
  # 左上、右上、右下、左下
  [-1, -1], [1, -1], [1, 1], [-1, 1]
]

def find_bomb(point, diff):
  x = point[0] - diff[0]
  y = point[1] - diff[1]
  if x < 0 or x >= H:
    return False
  if y < 0 or y >= W:
    return False
  return S[x][y] == "#"

for i in range(len(S)):
  new_row = ""
  for j in range(len(S[i])):
    if S[i][j] == ".":
      new_row += str(sum([find_bomb([i, j], r) for r in Rounds]))
      # cnt = 0
      # for r in Rounds:
      #   if find_bomb([i, j], r):
      #     cnt += 1
      # new_row += str(cnt)
    else:
      new_row += "#"

  S[i] = new_row

for s in S:
  print(s)