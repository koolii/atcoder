S = "AAABBBBBCDD"
N = len(S)

# 長さNの文字列Sが与えられたとする
i = 0

while i < N:
  # S[j] != S[i]となる場所を探す(※連続した文字を想定している為)
  j = i

  while j < N and S[j] == S[i]:
    j += 1

    # 文字S[i]が j - i文字連続したことが分かる
    print(S[i], j - i)

    # i を終了地点j に更新して次の位置を設定する
    i = j