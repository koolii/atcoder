# link: https://atcoder.jp/contests/abc205/tasks/abc205_c
# problem: POW

# こっちだとTLEになった
A, B, C = map(int, input().split())
a = A ** C
b = B ** C
if a < b:
  print("<")
elif a > b:
  print(">")
else:
  print("=")

# AC
# C乗になるのはAもBも同じなので、
# 何回階乗するかで、負の数の場合に調整さえすれば良いと判断した
A, B, C = map(int, input().split())
A = abs(A) if C % 2 == 0 else A
B = abs(B) if C % 2 == 0 else B
if A < B:
  print("<")
elif A > B:
  print(">")
else:
  print("=")