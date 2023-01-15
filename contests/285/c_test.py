S = input()
l = len(S)

ans = 0

for i in range(l):

  # (len - i - 1) ケタの文字
  char = S[i]
  # print(char, ord(char))
  # print(char, ord(char), ord(char) - 64)
  # print(l , i, 1)
  print((10 ** (l - i - 2) * 26))
  print(ord(char) - 64)
  print(ans)
  print("next")


  ans += (10 ** (l - i -1) * 26) + ord(char) - 64

print(ans)