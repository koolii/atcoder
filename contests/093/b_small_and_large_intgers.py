# A, B, K = map(int, input().split())
# count = 0
# for i in range(A, B + 1):
#   if count < K:
#     print(i)
#     count += 1
#   elif B - i < count:
#     print(i)
#     count -= 1

# timeoutする
# A, B, K = map(int, input().split())
# for i in range(A, B + 1):
#   if i < A + K or B - K < i:
#     print(i)

# https://atcoder.jp/contests/abc093/submissions/37624246

A, B, K = map(int, input().split())

# A+Kの差分が終端(B)より小さいならば、数値が大量にある可能性がある
# そのため、A+Kまででループさせる
end = (A + K) if (A+K) < (B+1) else (B+1)
for i in range(A, end):
    print(i)

# A+Kの差分と終端からの差分(B-K+1)と比較する、より後ろからループを開始させる
start = (B-K+1) if (A+K) < (B-K+1) else (A+K)
for i in range(start, B + 1):
    print(i)
