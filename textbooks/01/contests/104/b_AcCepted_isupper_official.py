def isAC(S):
  if S[0] != "A":
    return False

  if S[2:-1].count("C") != 1:
    return False

  # "str.isupper" で関数を指定できる
  # map()関数はlist型だけでなく、str型変数の各要素に対しても指定した処理を適用できる
  # "map(str.isupper, S)" で文字列Sの各文字に対して大文字かどうか判定している
  # "sum(map(str.isupper, S))" で文字列Sの大文字の個数をチェック
  if sum(map(str.isupper, S)) != 2:
    return False

  return True

print("AC" if isAC(input()) else "WA")