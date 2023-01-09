S = input()
N = len(S)
i = 0
words = []

while i < N:
  # iと同じ場所だと必ず大文字になるため、1文字分後ろからチェックする
  j = i + 1

  while j < N and S[j].islower():
    j += 1

  # 大文字になったら、その地点までで1単語として登録する必要がある
  end = j + 1

  words.append(S[i:end])

  i = end

# wordsの各単語を「大文字を全て小文字にした状態での辞書順比較する」
# Python3では、keyを用いることで、ソートする時の比較の規則を指定できる
words.sort(key=str.lower)

print("".join(words))