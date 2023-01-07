S = input()

def isAC(str):
  # "A" が先頭である必要がある
  if str[0] != "A":
    return False

  # "C" は個数まで1つの制限がある
  if str.count("C", 2, -1) != 1:
    return False

  # アスキーコードで "A" "C" 以外の大文字が存在するかチェック
  for char in str:
    num = ord(char)
    if num != 65 and num != 67 and 65 <= num <= 90:
      return False

  return True

print("AC" if isAC(S) else "WA")