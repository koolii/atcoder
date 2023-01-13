# 6-2
# 素直に解こうとすると下記の様になるが、問題がある
# Nが大きくなると、レベルNバーガーを表す文字列の長さが非常に大きくなってしまう
# レベルが1上がるごとに、バーガーの長さがおおむね2倍になっていることから、
# レベルNバーガーの長さは2^N以上になることが分かる
# レベルNバーガーを表す文字列を直接生成する方法ではACが得られないことが分かる
N, X = map(int, input().split())
burger = "P"
for i in range(N):
  burger = "B" + burger + "P" + burger + "B"
print(burger[0:X].count("P"))

# 再帰関数
# レベルNバーガーがレベルN-1バーガーによって定義されている
# つまり、バーガーはバーガー自身によって再帰的に定義されていることから再帰関数が用いることができそう

# レベルNバーガーの長さ: Ln, レベルN-1バーガーの長さ: Ln-1
# レベルNバーガー全体に含まれるパティの個数: Sn, レベルN-1バーガー全体に含まれるパティの個数: Sn-1
# レベルNバーガーを表す文字列の先頭からX層に含まれるパティの個数について考える

# X=1の時、0個(パンしかありえない)
# X=2, ... Ln-1 + 1(これは、 「"B" + burger1 + "P" + burger2 + "B"」 のburger1の区間を指す)の時、「レベルN-1バーガーの先頭からX-1文字目の中に含まれる "P" の個数」
# X=Ln-1 + 2(これは中間地点の "P" を指す)の時、Sn-1 + 1
# X=Ln-1 + 3, ... 2Ln-1 + 2(これはburger2の区間を指す)の時、「レベルN-1バーガーの先頭から X - Ln-1 - 2文字の中に含まれる "P" の個数」 + Sn-1 + 1
# X=2Ln-1 + 3(最後の"B")の時、2Sn-1 + 1個
# 最初のB地点、B->burger1までの区間、中間P地点、P->burger2までの区間、最後のB地点の5つで区分する

# Ln = 2Ln-1 + 3 (L0=1 問題からレベル0で "P" の為)
# Sn = 2S-1 + 1 (S0=1 問題からレベル0で "P" の為)

# recursive function
def rec(N, X, L, S):
  if N == 0:
    return 1 # S0

  # Xの大きさに応じて場合分けする
  if X == 1:
    # B(first)
    return 0
  elif X <= L[N-1] + 1:
    # burger1
    return rec(N-1, X-1, L, S)
  elif X == L[N-1] + 2:
    # P
    return S[N-1] + 1
  elif X <= L[N-1] * 2 + 2:
    count = S[N-1] + 1 # B + burger + Pの個数
    # burger2
    return rec(N-1, X - L[N-1] - 2, L, S) + count
  else:
    # B(last)
    return S[N-1] * 2 + 1

N, X = map(int, input().split())
L = [1] * (N+1)
S = [1] * (N+1)

for n in range(1, N+1):
  L[n] = L[n-1] * 2 + 3
  S[n] = S[n-1] * 2 + 1

print(rec(N,X,L,S))