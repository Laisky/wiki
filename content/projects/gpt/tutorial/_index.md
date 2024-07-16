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

_`Request Model` is the value of the model in the user's request parameters, and `Actual Model` is the actual model that will be sent by the backend to upstream._

| Request Model                                 | Actual Model               | Input Price | Output Price |
| --------------------------------------------- | -------------------------- | ----------- | ------------ |
| gpt-3.5-turbo                                 | gpt-3.5-turbo-0125         | 0.5         | 1.5          |
| gpt-3.5-turbo-1106                            |                            | 1           | 2            |
| gpt-3.5-turbo-0125                            |                            | 0.5         | 1.5          |
| gpt-3.5-turbo-16k                             | gpt-3.5-turbo-0125         | 0.5         | 1.5          |
| gpt-4o-2024-05-13                             |                            | 5           | 15           |
| gpt-4o                                        | gpt-4o-2024-05-13          | 5           | 15           |
| gpt-4-turbo-preview                           | gpt-4-turbo-2024-04-09     | 10          | 30           |
| gpt-4-turbo                                   | gpt-4-turbo-2024-04-09     | 10          | 30           |
| gpt-4-turbo-2024-04-09                        |                            | 10          | 30           |
| gpt-4-1106-preview                            |                            | 10          | 30           |
| gpt-4-0125-preview                            |                            | 10          | 30           |
| gpt-4-vision-preview                          | gpt-4-turbo-2024-04-09     | 10          | 30           |
| gpt-4-1106-vision-preview                     |                            | 10          | 30           |
| gpt-4                                         | gpt-4-turbo-2024-04-09     | 10          | 30           |
| gpt-4-32k                                     | gpt-4-turbo-2024-04-09     | 10          | 30           |
| deepseek-chat                                 |                            | 0.14        | 0.28         |
| deepseek-coder                                |                            | 0.14        | 0.28         |
| claude-1                                      | claude-instant-1.2         | 0.8         | 2.4          |
| claude-2                                      | claude-2.1                 | 8           | 24           |
| claude-3                                      | claude-3-haiku-20240307    | 0.25        | 1.25         |
| claude-instant-1                              | claude-instant-1.2         | 0.8         | 2.4          |
| claude-instant-1.2                            |                            | 0.8         | 2.4          |
| claude-2.1                                    |                            | 8           | 24           |
| claude-3-opus                                 | claude-3-opus-20240229     | 15          | 75           |
| claude-3-sonnet                               | claude-3-sonnet-20240229   | 3           | 15           |
| claude-3-haiku                                | claude-3-haiku-20240307    | 0.25        | 1.25         |
| claude-3-opus-20240229                        |                            | 15          | 75           |
| claude-3-sonnet-20240229                      |                            | 3           | 15           |
| claude-3-haiku-20240307                       |                            | 0.25        | 1.25         |
| claude-3.5-sonnet                             | claude-3-5-sonnet-20240620 | 3           | 15           |
| claude-3.5-sonnet-8k                          | claude-3-5-sonnet-20240620 | 3           | 15           |
| claude-3-5-sonnet-20240620                    |                            | 3           | 15           |
| gemma-7b-it                                   |                            | FREE        |              |
| llama3-8b-8192                                |                            | FREE        |              |
| llama3-70b-8192                               |                            | FREE        |              |
| mixtral-8x7b-32768                            |                            | FREE        |              |
| gemini-pro                                    |                            | FREE        |              |
| gemini-pro-vision                             |                            | FREE        |              |
| gpt-3.5-turbo-0301                            | gemini-pro                 | FREE        |              |
| gpt-3.5-turbo-16k-0613                        | gemini-pro                 | FREE        |              |
| dall-e-2                                      |                            | 0.02/pic    |              |
| dall-e-3                                      |                            | 0.04/pic    |              |
| sdxl-turbo                                    |                            | FREE        |              |
| tts-1                                         |                            | 15          |              |
| tts-1-hd                                      |                            | 30          |              |
| whisper-1                                     |                            | 0.006/min   |              |
| test-embedding-ada-002                        |                            | 0.1         |              |
| text-embedding-3-small                        |                            | 0.02        |              |
| text-embedding-3-large                        |                            | 0.13        |              |
| @cf/meta/llama-2-7b-chat-fp16                 |                            | FREE        |              |
| @cf/meta/llama-2-7b-chat-int8                 |                            | FREE        |              |
| @cf/mistral/mistral-7b-instruct-v0.1          |                            | FREE        |              |
| @hf/thebloke/deepseek-coder-6.7b-base-awq     |                            | FREE        |              |
| @hf/thebloke/deepseek-coder-6.7b-instruct-awq |                            | FREE        |              |
| @cf/deepseek-ai/deepseek-math-7b-base         |                            | FREE        |              |
| @cf/deepseek-ai/deepseek-math-7b-instruct     |                            | FREE        |              |
| @cf/thebloke/discolm-german-7b-v1-awq         |                            | FREE        |              |
| @cf/tiiuae/falcon-7b-instruct                 |                            | FREE        |              |
| @cf/google/gemma-2b-it-lora                   |                            | FREE        |              |
| @hf/google/gemma-7b-it                        |                            | FREE        |              |
| @cf/google/gemma-7b-it-lora                   |                            | FREE        |              |
| @hf/nousresearch/hermes-2-pro-mistral-7b      |                            | FREE        |              |
| @hf/thebloke/llama-2-13b-chat-awq             |                            | FREE        |              |
| @cf/meta-llama/llama-2-7b-chat-hf-lora        |                            | FREE        |              |
| @cf/meta/llama-3-8b-instruct                  |                            | FREE        |              |
| @hf/thebloke/llamaguard-7b-awq                |                            | FREE        |              |
| @hf/thebloke/mistral-7b-instruct-v0.1-awq     |                            | FREE        |              |
| @hf/mistralai/mistral-7b-instruct-v0.2        |                            | FREE        |              |
| @cf/mistral/mistral-7b-instruct-v0.2-lora     |                            | FREE        |              |
| @hf/thebloke/neural-chat-7b-v3-1-awq          |                            | FREE        |              |
| @cf/openchat/openchat-3.5-0106                |                            | FREE        |              |
| @hf/thebloke/openhermes-2.5-mistral-7b-awq    |                            | FREE        |              |
| @cf/microsoft/phi-2                           |                            | FREE        |              |
| @cf/qwen/qwen1.5-0.5b-chat                    |                            | FREE        |              |
| @cf/qwen/qwen1.5-1.8b-chat                    |                            | FREE        |              |
| @cf/qwen/qwen1.5-14b-chat-awq                 |                            | FREE        |              |
| @cf/qwen/qwen1.5-7b-chat-awq                  |                            | FREE        |              |
| @cf/defog/sqlcoder-7b-2                       |                            | FREE        |              |
| @hf/nexusflow/starling-lm-7b-beta             |                            | FREE        |              |
| @cf/tinyllama/tinyllama-1.1b-chat-v1.0        |                            | FREE        |              |
| @hf/thebloke/zephyr-7b-beta-awq               |                            | FREE        |              |

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
