# link: https://atcoder.jp/contests/abc232/tasks/abc232_a
# problem: QQ solver

S = str(input())
index = S.find("x")
a, b = int(S[0:index]), int(S[index+1:])
print(a*b)