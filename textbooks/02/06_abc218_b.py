# link: https://atcoder.jp/contests/abc218/tasks/abc218_b
# problem: qwerty

# ascii code
# a = 97
# ...
# z = 122

# 自己実装
p = list(map(int, input().split()))
res = [chr(i + 96) for i in p]
print(*res, sep="")

# 模範解答
# ans=""
# for i in range(26):
#   ans += chr(p[i] + 96)
# print(ans)
