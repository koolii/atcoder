# DXとDYでX軸・Y軸を別々の配列にしているところに注目
# 複数のリストの要素をまとめて取得できる zip()関数 を使って別々で配列を定義することを可能にしている
# 0:下, 1:右, 2:上, 3:左, 4:右下, 5:右上, 6:左上, 7:左下
DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

# Input
H, W = map(int, input().split())
S = [input() for _ in range(H)]

# Python3では str型変数の各文字の書き換えはできない
# 別途回答用を用意する('.'のところは先んじて "0" とする)
# 各行を各文字ずつ繰り返す
result = [[0 if v == "." else "#" for v in row] for row in S]

# 各マス(i,j)を順に処理
for i in range(H):
  for j in range(W):
    # 空きマス以外はそのままにする
    if S[i][j] != ".":
      continue

    # 周囲8マスの "#" の個数を数える
    for dx, dy in zip(DX, DY):
      # マス(i,j)の周囲のマスを(ni, nj)とする
      ni, nj = i + dx, j + dy

      # マス(ni,nj)が盤面外の場合はスキップ
      if (ni < 0 or ni >= H) or (nj < 0 or nj >= W):
        continue

      # "#"であれば1増やす
      if S[ni][nj] == "#":
        result[i][j] += 1

# 出力形式に合わせて出力
# row変数はlist型(resultは二次元配列)になり、そのまま出力するとlist型としての出力になる
# そこでアスタリスク "*" を用いることで、listの各要素を個別に取り出してprint()関数に渡すことができます
# ただし、print(*row)と書くと、変数rowの各文字毎に空白文字が挿入されてしまう
# print(*row, sep="")と書くことで、空白文字もなくすことができる
for row in result:
  print(*row, sep="")