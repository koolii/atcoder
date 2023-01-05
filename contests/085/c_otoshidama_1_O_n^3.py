# これはforループを3重に行っているため、O(N^3)となり、かなりの計算量になってしまい、結果TLEになってしまう
# `c_otoshidama_2_O_n^2.py` でO(N^2)になるように改善したプログラムを作成する

N, Y = map(int, input().split())

ra, rb, rc = -1, -1, -1

for a in range(N + 1):
  for b in range(N + 1):
    for c in range(N + 1):
      price = 10000 * a + 5000 * b + 1000 * c
      bill = a + b + c
      if bill == N and price == Y:
        ra, rb, rc = a, b, c

print(ra, rb, rc)
