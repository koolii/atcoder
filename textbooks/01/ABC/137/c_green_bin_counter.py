from collections import Counter

N = int(input())
S = ["".join(sorted(input())) for i in range(N)]

# Counterでヒストグラムを作成
num = Counter(S)

# 各文字列の個数をnとして、nC2を足していく
print(sum(n * (n - 1) // 2 for n in num.values()))