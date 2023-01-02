# P95 textbook

def how_many_times(num):
    count = 0

    while num % 2 == 0:
        count += 1
        num //= 2

    return count


N = int(input())
A = list(map(int, input().split()))

# javascriptで言うところの.map()関数と同じ
counts = map(how_many_times, A)
# 配列の中から最小値を取得する
result = min(counts)

print(result)
