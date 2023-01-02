N = int(input())
A = list(map(int, input().split()))

ok = True
count = 0

while True:
    for i in range(N):
        # if A[i] % (2 + (count + 1)) == 1: はTLEが起きた
        if A[i] % 2 == 1:
            ok = False

    if not ok:
        break

    for i in range(N):
        A[i] //= 2

    count += 1

print(count)
