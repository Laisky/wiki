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

*On the left is the value of the model in the request parameters, and on the right is the actual model that will be invoked by the backend.*

- `gpt-3.5-turbo-1106`
- `gpt-3.5-turbo-0125`
- `gpt-3.5-turbo` -> `gpt-3.5-turbo-0125`
- `gpt-3.5-turbo-16k` -> `gpt-3.5-turbo-0125`
- `gpt-4-1106-preview`
- `gpt-4-0125-preview`
- `gpt-4-vision-preview`
- `gpt-4-turbo-preview` -> `gpt-4-0125-preview`
- `gpt-4` -> `gpt-4-0125-preview`
- `gpt-4-32k` -> `gpt-4-0125-preview`
- `claude-instant-1`
- `claude-2`
- `claude-3-opus`
- `claude-3-sonnet`
- `llama2-70b-4096`
- `mixtral-8x7b-32768`
- `gemini-pro`
- `gemini-pro-vision`
- `gpt-3.5-turbo-0301` -> `gemini-pro`
- `gpt-3.5-turbo-16k-0613` -> `gemini-pro`
- `text-davinci-003`
- `dall-e-2`
- `dall-e-3`
- `sdxl-turbo`
- `tts-1`
- `tts-1-hd`
- `whisper-1`
- `test-embedding-ada-002`
- `text-embedding-3-small`
- `text-embedding-3-large`

### Pricing

<https://openai.com/pricing>

## Free User

As a new user, you will automatically receive a unique token for free. This token allows you to chat with GPT-3.5-turbo.

![free token](https://s3.laisky.com/uploads/2023/09/free-token.png)

There are three types of tokens you can use:

1. `FREETIER-*`: Free token with rate limits.
2. Your own OpenAI token: Unlimited usage.
3. Paid token: Unlimited usage.
