import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def softmax(values):
    exps = [math.exp(x) for x in values]
    total = sum(exps)
    return [x / total for x in exps]


# 三个 token，每个 token 两个维度
keys = [
    [1.0, 0.0],
    [0.8, 0.2],
    [0.0, 1.0],
]

values = [
    [10, 0],
    [8, 2],
    [0, 10],
]

# 当前 token 想寻找的信息方向
query = [1.0, 0.1]

scores = [dot(query, k) / math.sqrt(2) for k in keys]
weights = softmax(scores)

print("scores:")
for i, score in enumerate(scores):
    print(f"K{i}: {score:.3f}")

print("\nattention weights:")
for i, weight in enumerate(weights):
    print(f"K{i}: {weight:.3f}")

output = [
    sum(weights[i] * values[i][j] for i in range(len(values)))
    for j in range(len(values[0]))
]

print("\nweighted value:")
print(output)

print("\n这个输出就是 Attention 根据相关性混合出来的新表示。")
