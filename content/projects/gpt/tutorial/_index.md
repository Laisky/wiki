---
title: "Tutorial"
url: "/projects/gpt/tutorial"
bookToC: true
---

(page_gptchat_tutorial)=

## Introduction

<https://chat.laisky.com>

Welcome to the web application based on OpenAI ChatGPT! This application allows you to engage in casual chat using the powerful GPT-3.5/4 language model, as well as conduct file-based chats using your own files. If you have any questions or need assistance, feel free to reach out to me at <chatgpt@laisky.com>.

## Features

This application offers several exciting features:

- [Casual Chat](@page_casual_chat): Engage in casual conversations using GPT-3.5/4.
- [File Chat / Q&amp;A](@page_file_chat): Have file-based chats and ask questions.
- [Text to Image](@page_file_image): Convert text into images.

## Models

(gpt_chat_support_models)=

API Base: `https://oneapi.laisky.com`

Support Models:

_On the left is the value of the model in the request parameters, and on the right is the actual model that will be invoked by the backend._

| Model Name                | Actual Model             | Input Price | Output Price |
| ------------------------- | ------------------------ | ----------- | ------------ |
| gpt-3.5-turbo             | gpt-3.5-turbo-0125       |             |              |
| gpt-3.5-turbo-1106        |                          | 1           | 2            |
| gpt-3.5-turbo-0125        |                          | 0.5         | 1.5          |
| gpt-3.5-turbo-16k         | gpt-3.5-turbo-0125       |             |              |
| gpt-4o-2024-05-13         |                          | 5           | 15           |
| gpt-4o                    | gpt-4o-2024-05-13        |             |              |
| gpt-4-turbo-preview       | gpt-4-turbo-2024-04-09   |             |              |
| gpt-4-turbo               | gpt-4-turbo-2024-04-09   |             |              |
| gpt-4-turbo-2024-04-09    |                          | 10          | 30           |
| gpt-4-1106-preview        |                          | 10          | 30           |
| gpt-4-0125-preview        |                          | 10          | 30           |
| gpt-4-vision-preview      | gpt-4-turbo-2024-04-09   |             |              |
| gpt-4-1106-vision-preview |                          | 10          | 30           |
| gpt-4                     | gpt-4-turbo-2024-04-09   |             |              |
| gpt-4-32k                 | gpt-4-turbo-2024-04-09   |             |              |
| deepseek-chat             |                          | 0.14        | 0.28         |
| claude-1                  | claude-instant-1.2       |             |              |
| claude-2                  | claude-2.1               |             |              |
| claude-3                  | claude-3-haiku-20240307  |             |              |
| claude-instant-1          | claude-instant-1.2       |             |              |
| claude-instant-1.2        |                          | 0.8         | 2.4          |
| claude-2.1                |                          | 8           | 24           |
| claude-3-opus             | claude-3-opus-20240229   |             |              |
| claude-3-sonnet           | claude-3-sonnet-20240229 |             |              |
| claude-3-haiku            | claude-3-haiku-20240307  |             |              |
| claude-3-opus-20240229    |                          | 15          | 45           |
| claude-3-sonnet-20240229  |                          | 3           | 12           |
| claude-3-haiku-20240307   |                          | 0.25        | 1.25         |
| gemma-7b-it               |                          | FREE        |              |
| llama3-8b-8192            |                          | FREE        |              |
| llama3-70b-8192           |                          | FREE        |              |
| gemini-pro                |                          | FREE        |              |
| gemini-pro-vision         |                          | FREE        |              |
| gpt-3.5-turbo-0301        | gemini-pro               |             |              |
| gpt-3.5-turbo-16k-0613    | gemini-pro               |             |              |
| dall-e-2                  |                          | 0.02/pic    |              |
| dall-e-3                  |                          | 0.04/pic    |              |
| sdxl-turbo                |                          | FREE        |              |
| tts-1                     |                          | 15          |              |
| tts-1-hd                  |                          | 30          |              |
| whisper-1                 |                          | 0.006/min   |              |
| test-embedding-ada-002    |                          | 0.1         |              |
| text-embedding-3-small    |                          | 0.02        |              |
| text-embedding-3-large    |                          | 0.13        |              |

_the unit of input/output price is USD per million tokens_

### Pricing

<https://openai.com/pricing>

## Free User

As a new user, you will automatically receive a unique token for free. This token allows you to chat with GPT-3.5-turbo.

![free token](https://s3.laisky.com/uploads/2023/09/free-token.png)

There are three types of tokens you can use:

1. `FREETIER-*`: Free token with rate limits.
2. Your own OpenAI token: Unlimited usage.
3. Paid token: Unlimited usage.
