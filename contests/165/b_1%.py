X = int(input())
yen = 100
years = 0

while X > yen:
    years += 1
    # yen += int(yen * 0.01) after_contestsでWrongAnswerになる
    yen = (yen * 101) // 100  # 小数点計算を回避し、101倍後に100で割る

print(years)
