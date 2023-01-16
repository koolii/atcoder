# link: https://atcoder.jp/contests/abc201/tasks/abc201_b
# problem: do you know the second highest mountain?

N = int(input())
list = []

for i in range(N):
  si, ti = map(str, input().split())
  ti = int(ti)
  list.append([ti, si])

# sort()する時は、配列先頭の要素をソートすることになる為
# 今回は高さTを配列の先頭にすることで、ソートができることになる
list.sort(reverse=True)

print(list[1][1])