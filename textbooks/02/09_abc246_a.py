# link: https://atcoder.jp/contests/abc246/tasks/abc246_a
# problem: Four Points

from collections import defaultdict

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x_points = defaultdict(int)
y_points = defaultdict(int)

x_points[x1] += 1
x_points[x2] += 1
x_points[x3] += 1
y_points[y1] += 1
y_points[y2] += 1
y_points[y3] += 1

x = x1
x = x2 if x_points[x2] == 1 else x
x = x3 if x_points[x3] == 1 else x
y = y1
y = y2 if y_points[y2] == 1 else y
y = y3 if y_points[y3] == 1 else y

print(x, y)