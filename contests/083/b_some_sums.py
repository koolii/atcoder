# https://atcoder.jp/contests/abc083/submissions/37623695

N, A, B = map(int, input().split())
sum = 0

for i in range(1, N + 1):
    digit = 0
    num = i

    while i > 0:
        digit += i % 10
        i //= 10

    if A <= digit <= B:
        sum += num

print(sum)
