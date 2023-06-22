---
title: "需求"
url: "/projects/gpt/requirements"
---

## 概述

核心目标：打造小而美的围绕 openai、stable diffusion、开源 LLM 的实用小工具。

## Casual Chat

核心功能

1. 和 AI 的聊天
2. 自选 AI 模型
3. 自定义聊天参数
4. 聊天记录的持久化
5. 用户自定义 token
6. 聊天记录的可编辑（编辑、删除）和重载
7. 自定义 system prompt
8. system prompt 的保存、编辑
9. system prompt 模版列表

后期功能：

1. 聊天记录的多端同步
2. 导入、导出聊天记录
3. 多模态聊天（语音、图片）

## QA Chat

支持自定义资料集，进行预训练的 QA Chat Bot。现阶段使用 embeddings 进行实现。

核心功能：

1. 用户自定义资料集
   1. 上传 PDF
   2. PDF 的端对端加密
2. 用户自选资料集，构建 chat bot
3. chat bot 持久化
4. 和 chat bot 的聊天，chat bot 答复并提供参考资料集
5. 参考资料集的在线预览

## Whisper

1. 语音转文字

## Stable Diffsion

基于 txt2img 和 img2img 做一系列工具集
