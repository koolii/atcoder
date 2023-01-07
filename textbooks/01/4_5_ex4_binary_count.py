# ２進数の求め方が余りわかっていない
# http://www.it-license.com/cardinal_number/DecimalToBinary.html#:~:text=%E6%95%B4%E6%95%B0%E3%81%AE10%E9%80%B2%E6%95%B0%E3%82%922%E9%80%B2%E6%95%B0%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%99%E3%82%8B,%E3%81%AE%E5%A4%89%E6%8F%9B%E7%B5%90%E6%9E%9C%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82
def bit_count(N):
  sum_digit = 0
  while N > 0:
    sum_digit += N % 2
    N //= 2

  return sum_digit

def binary_num(N):
  num_str = ""
  while N > 0:
    num_str += str(N % 2)
    N //= 2

  # [::-1] で逆順にできるらしい
  binary = str(num_str)[::-1]

  return int(binary)

N = 65536 # 10000000000000000

print(bit_count(N), binary_num(N))