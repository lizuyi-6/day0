<div align="center">

# Hello LLM

### 用图解、直觉与最小代码，从零理解大语言模型

</div>

---

## 关于本项目

很多 LLM 教程从论文、公式或 API 开始，容易出现“会调用，但不知道为什么”的问题。

**Hello LLM** 希望像《Hello 算法》一样，建立一套 LLM 知识地图：先理解信息如何流动，再对应到真实工程实现。

参考《Hello 算法》的理念：动画图解、知识地图、最小实验、逐步建立直觉。fileciteturn1file0

## 学习路线

```
现实世界
   ↓
文字 / 图片 / 声音
   ↓
Token 与 Embedding
   ↓
Transformer
   ↓
Attention
   ↓
训练与参数形成
   ↓
多模态
   ↓
RAG / Memory
   ↓
Agent
```

## 章节规划

- 00 为什么需要 LLM：从传统程序到概率模型
- 01 Token：模型真正看到的是什么
- 02 Embedding：文字如何进入向量空间
- 03 Transformer：信息如何流动
- 04 Attention：模型如何动态寻找关联
- 05 Training：能力如何从参数中产生
- 06 Multimodal：Visual Token 为什么不是图片描述
- 07 Context、RAG 与长期记忆
- 08 Agent 与工具调用
- 09 本地模型、云端模型与混合 AI 架构

## 每章结构

1. 一句话直觉
2. 信息流图解
3. 技术原理
4. 最小代码实验

目标不是背诵术语，而是回答：

- 为什么 Transformer 可以处理语言？
- 为什么 Attention 不需要提前知道答案？
- 为什么视觉 Token 不等于 Caption？
- 为什么训练后模型会形成概念？

## 目录（建设中）

```
docs/
├── 00_start
├── 01_token_embedding
├── 02_transformer
├── 03_attention
├── 04_training
├── 05_multimodal
├── 06_memory_rag
└── 07_agent
```

## 原则

> 能画出来，才算开始理解。
>
> 能用最小代码复现，才算真正抓住结构。

持续更新中。