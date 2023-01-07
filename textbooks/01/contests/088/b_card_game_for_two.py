# by myself
N = int(input())
A = list(map(int, input().split()))
AA = sorted(A, reverse=True)
alice = 0
bob = 0

for i in range(len(AA)):
    if i % 2 == 0:
        alice += AA[i]
    else:
        bob += AA[i]

print(alice - bob)
