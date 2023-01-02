N = int(input())
A = list(map(int, input().split()))
count = 0

# all()は組み込み関数
# all(a % 2 == 0 for a in A) は配列Aのすべての要素が2で割り切れるかどうかを判定する
# [a // 2 for a in A]は、配列Aの各要素を2で割った商からなる配列を生成する
while all(a % 2 == 0 for a in A):
    A = [a // 2 for a in A]
    count += 1

print(count)
