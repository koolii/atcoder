# link: https://atcoder.jp/contests/abc234/tasks/abc234_a

t = int(input())

def f(x):
  return x*x + 2*x + 3

print(f(f(f(t) + t) + f(f(t))))