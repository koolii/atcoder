a, b = map(int, input().split())
print("Yes" if 0 <= (b - (a * 2)) <= 1 else "No")