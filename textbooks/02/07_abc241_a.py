# link: https://atcoder.jp/contests/abc241/tasks/abc241_a
# problem: digit machine

a = list(map(int, input().split()))
k = 0

for cnt in range(3):
  k = a[k]

print(k)
