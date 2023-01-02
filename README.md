# atcoder

## if 文を減らす

```cpp
result = min(result, counter);
```

```cpp
if (result > counter) {
  result = counter
}
```

一般にプログラム中の if 文が増えるとバグが生じやすい傾向にあります。
例えば if 文の条件式で不等号の向きを誤る可能性が考えられます。

if 文を減らす意識を持つことで、プログラムにバグを混入させる可能性を減らせます。

## ソート

競技プログラミングでは、ソートアルゴリズムを自前実装することはほとんどない

## スライス記法

文字列の部分文字列を取得する際に start,end を指定する記法を言う
start を省略した場合は、S の先頭の要素から取り出すことを表し、
end を省略した場合は、S の末尾の要素まで取り出すことを表す

```python
S = "AtCoder"

# 7
print(len(S))

# "AtCoderContest"
print(S + "Contest")

# "Cod"
print(S[2:5])

# "tCoder"
print(S[1:])

# "AtCod
print(S[:-2])
```
