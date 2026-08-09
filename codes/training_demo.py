"""
Hello LLM - Training Demo

用一个极小例子展示：
Forward -> Loss -> Gradient -> Update

目标：学习 y = 2x
模型：y_hat = w*x
"""

samples = [(1, 2), (2, 4), (3, 6)]

w = 0.0
learning_rate = 0.1

for step in range(20):
    total_loss = 0
    gradient = 0

    for x, y in samples:
        prediction = w * x
        error = prediction - y

        # 平方误差
        total_loss += error ** 2

        # d((wx-y)^2)/dw 的简化形式
        gradient += 2 * error * x

    gradient /= len(samples)
    total_loss /= len(samples)

    # 更新参数
    w = w - learning_rate * gradient

    print(
        f"step={step:02d}, "
        f"loss={total_loss:.4f}, "
        f"w={w:.4f}"
    )

print("learned w:", w)
