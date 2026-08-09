# 一个极简的 Token -> Embedding 演示

# 真实模型中这里是巨大矩阵
embedding_table = {
    101: [0.2, 0.5, -0.1],  # 我
    203: [0.8, -0.3, 0.4],   # 喜欢
    305: [-0.4, 0.7, 0.9],   # 苹果
}

sentence = [101, 203, 305]

print("Token IDs:")
print(sentence)

print("\nEmbedding vectors:")
for token_id in sentence:
    print(token_id, "->", embedding_table[token_id])

print("\nTransformer 后续处理的是这些向量，而不是原来的数字 ID。")
