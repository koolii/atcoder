# 6-2 なんかWAになる。中身理解が出来ない
# link: https://qiita.com/u2dayo/items/386142030a70d2db4e58
# 入力
N, M, Q = map(int, input().split())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for q in range(Q):
  a[q], b[q], c[q], d[q] = map(int, input().split())

  # 数列Aの添字 a[q], b[q] を0始まりにする
  a[q] = -1
  b[q] = -1

# 数列Aのスコアを計算する関数
def calc_score(A):
  score = 0
  for ai, bi, ci, di in zip(a, b, c, d):
    if A[bi] - A[ai] == ci:
      score += di
    return score

# 数列Aを全列挙してスコアの最大値を求める再帰関数
def rec(A):
  # 終了条件
  if len(A) == N:
    return calc_score(A)

  # 最大値
  result = 0

  # 数列Aの前回の要素を取得
  prev_last = A[-1] if A else 1

  # 数列Aが単調増加になるように末尾に要素を追加
  for add in range(prev_last, M + 1):
    # 数列Aに要素追加
    A.append(add)

    # 再帰呼び出しをしながら、スコア最大値を更新
    result = max(result, rec(A))

    # 数列Aの末尾を削除してもとに戻す
    A.pop()

  #最大値を返す
  return result

# 数列Aを全列挙して調べる
A = []
print(rec(A))