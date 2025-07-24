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

| Request Model                                 | Actual Model                        | Input Price | Output Price                                                   |
| --------------------------------------------- | ----------------------------------- | ----------- | -------------------------------------------------------------- |
| gpt-3.5-turbo                                 | gpt-3.5-turbo-0125                  | 0.5         | 1.5                                                            |
| gpt-3.5-turbo-1106                            |                                     | 1           | 2                                                              |
| gpt-3.5-turbo-0125                            |                                     | 0.5         | 1.5                                                            |
| gpt-3.5-turbo-16k                             | gpt-3.5-turbo-0125                  | 0.5         | 1.5                                                            |
| o1-pro                                        |                                     | 150         | 600                                                            |
| o1-pro-2025-03-19                             |                                     | 150         | 600                                                            |
| o1                                            |                                     | 15          | 60                                                             |
| o1-2024-12-17                                 |                                     | 15          | 60                                                             |
| o1-preview                                    |                                     | 15          | 60                                                             |
| o1-preview-2024-09-12                         |                                     | 15          | 60                                                             |
| o1-mini                                       |                                     | 3           | 12                                                             |
| o1-mini-2024-09-12                            |                                     | 3           | 12                                                             |
| o3-mini                                       |                                     | 1.1         | 4.4                                                            |
| o3-mini-2025-01-31                            |                                     | 1.1         | 4.4                                                            |
| o3-mini                                       |                                     | 1.1         | 4.4                                                            |
| o3-mini-2025-01-31                            |                                     | 1.1         | 4.4                                                            |
| o3                                            |                                     | 2           | 8                                                              |
| o3-2025-04-16                                 |                                     | 2           | 8                                                              |
| o3-pro                                        |                                     | 20          | 80                                                             |
| o3-pro-2025-06-10                             |                                     | 20          | 80                                                             |
| o4-mini                                       |                                     | 1.1         | 4.4                                                            |
| o4-mini-2025-04-16                            |                                     | 1.1         | 4.4                                                            |
| gpt-4.1                                       |                                     | 2           | 8                                                              |
| gpt-4.1-2025-04-14                            |                                     | 2           | 8                                                              |
| gpt-4.1-mini                                  |                                     | 0.4         | 1.6                                                            |
| gpt-4.1-mini-2025-04-14                       |                                     | 0.4         | 1.6                                                            |
| gpt-4.1-nano                                  |                                     | 0.1         | 0.4                                                            |
| gpt-4.1-nano-2025-04-14                       |                                     | 0.1         | 0.4                                                            |
| gpt-4.5-preview                               |                                     | 75          | 150                                                            |
| gpt-4.5-preview-2025-02-27                    |                                     | 75          | 150                                                            |
| gpt-4o                                        | gpt-4o-2024-11-20                   | 2.5         | 10                                                             |
| chatgpt-4o-latest                             |                                     | 5           | 15                                                             |
| gpt-4o-2024-05-13                             |                                     | 5           | 15                                                             |
| gpt-4o-2024-08-06                             |                                     | 2.5         | 10                                                             |
| gpt-4o-2024-11-20                             |                                     | 2.5         | 10                                                             |
| gpt-4o-search-preview                         |                                     | 2.5         | 10                                                             |
| gpt-4o-search-preview-2025-03-11              |                                     | 2.5         | 10                                                             |
| gpt-4o-mini                                   |                                     | 0.15        | 0.6                                                            |
| gpt-4o-mini-2024-07-18                        |                                     | 0.15        | 0.6                                                            |
| gpt-4o-mini-search-preview                    |                                     | 0.15        | 0.6                                                            |
| gpt-4o-mini-search-preview-2025-03-11         |                                     | 0.15        | 0.6                                                            |
| gpt-4-turbo-preview                           | gpt-4-turbo-2024-04-09              | 10          | 30                                                             |
| gpt-4-turbo                                   | gpt-4-turbo-2024-04-09              | 10          | 30                                                             |
| gpt-4-turbo-2024-04-09                        |                                     | 10          | 30                                                             |
| gpt-4-1106-preview                            |                                     | 10          | 30                                                             |
| gpt-4-0125-preview                            |                                     | 10          | 30                                                             |
| gpt-4-vision-preview                          | gpt-4-turbo-2024-04-09              | 10          | 30                                                             |
| gpt-4-1106-vision-preview                     |                                     | 10          | 30                                                             |
| gpt-4                                         | gpt-4-turbo-2024-04-09              | 10          | 30                                                             |
| gpt-4-32k                                     | gpt-4-turbo-2024-04-09              | 10          | 30                                                             |
| deepseek-chat                                 |                                     | 0.14        | 0.28                                                           |
| deepseek-reasoner                             |                                     | 0.55        | 2.19                                                           |
| claude-3-opus                                 | claude-3-opus-20240229              | 15          | 75                                                             |
| claude-3-sonnet                               | claude-3-sonnet-latest              | 3           | 15                                                             |
| claude-3-haiku                                | claude-3-haiku-20240307             | 0.25        | 1.25                                                           |
| claude-3-opus-20240229                        |                                     | 15          | 75                                                             |
| claude-3-sonnet-20240229                      |                                     | 3           | 15                                                             |
| claude-3-haiku-20240307                       |                                     | 0.25        | 1.25                                                           |
| claude-3.5-haiku                              | claude-3-5-haiku-20241022           | 1           | 5                                                              |
| claude-3-5-haiku-20241022                     |                                     | 1           | 5                                                              |
| claude-3.5-sonnet                             | claude-3-5-sonnet-latest            | 3           | 15                                                             |
| claude-3.5-sonnet-8k                          | claude-3-5-sonnet-latest            | 3           | 15                                                             |
| claude-3-5-sonnet-latest                      |                                     | 3           | 15                                                             |
| claude-3-5-sonnet-20240620                    |                                     | 3           | 15                                                             |
| claude-3-5-sonnet-20241022                    |                                     | 3           | 15                                                             |
| claude-3.7-sonnet                             | claude-3-7-sonnet-latest            | 3           | 15                                                             |
| claude-3-7-sonnet-latest                      |                                     | 3           | 15                                                             |
| claude-3-7-sonnet-20250219                    |                                     | 3           | 15                                                             |
| claude-4-sonnet                               | claude-sonnet-4-20250514            | 3           | 15                                                             |
| claude-sonnet-4-20250514                      |                                     | 3           | 15                                                             |
| claude-4-opus                                 | claude-opus-4-20250514              | 15          | 75                                                             |
| claude-opus-4-20250514                        |                                     | 15          | 75                                                             |
| gemma2-9b-it                                  |                                     | FREE        | FREE                                                           |
| mixtral-8x7b-32768                            |                                     | FREE        | FREE                                                           |
| llama-guard-3-8b                              |                                     | FREE        | FREE                                                           |
| llama3-70b-8192                               |                                     | FREE        | FREE                                                           |
| llama3-8b-8192                                |                                     | FREE        | FREE                                                           |
| llama-3.1-8b-instant                          |                                     | FREE        | FREE                                                           |
| llama-3.1-70b-specdec                         |                                     | FREE        | FREE                                                           |
| llama-3.2-1b-preview                          |                                     | FREE        | FREE                                                           |
| llama-3.2-3b-preview                          |                                     | FREE        | FREE                                                           |
| llama-3.2-11b-vision-preview                  |                                     | FREE        | FREE                                                           |
| llama-3.2-90b-vision-preview                  |                                     | FREE        | FREE                                                           |
| llama-3.3-70b-versatile                       |                                     | FREE        | FREE                                                           |
| llama-3.3-70b-specdec                         |                                     | FREE        | FREE                                                           |
| meta-llama/llama-guard-4-12b                  |                                     | 0.2         | 1                                                              |
| meta-llama/llama-4-scout-17b-16e-instruct     |                                     | 0.11        | 0.34                                                           |
| moonshotai/kimi-k2-instruct                   |                                     | 1           | 3                                                              |
| qwen/qwen3-32b                                |                                     | 0.29        | 0.59                                                           |
| gemini-1.5-flash                              | gemini-1.5-flash-002                | 0.01875     | 0.075                                                          |
| gemini-1.5-flash-001                          |                                     | 0.01875     | 0.075                                                          |
| gemini-1.5-flash-002                          |                                     | 0.01875     | 0.075                                                          |
| gemini-2.0-flash                              |                                     | 0.15        | 0.4                                                            |
| gemini-2.0-flash-exp                          |                                     | 0.15        | 0.4                                                            |
| gemini-2.0-flash-001                          |                                     | 0.15        | 0.4                                                            |
| gemini-2.0-flash-lite-preview-02-05           |                                     | 0.075       | 0.3                                                            |
| gemini-2.0-flash-thinking                     | gemini-2.0-flash-thinking-exp-01-21 | 0.15        | 0.4                                                            |
| gemini-2.0-flash-thinking-exp-01-21           |                                     | 0.15        | 0.4                                                            |
| gemini-2.5-flash-preview-04-17                |                                     | 0.15        | 0.4                                                            |
| gemini-2.5-flash-preview-05-20                |                                     | 0.15        | 0.4                                                            |
| gemini-pro                                    |                                     | 0.5         | 1                                                              |
| gemini-pro-vision                             |                                     | 0.5         | 1                                                              |
| gemini-1.5-pro                                | gemini-1.5-pro-002                  | 1.25        | 5                                                              |
| gemini-1.5-pro-001                            |                                     | 1.25        | 5                                                              |
| gemini-1.5-pro-002                            |                                     | 1.25        | 5                                                              |
| gemini-1.5-pro-latest                         |                                     | 1.25        | 5                                                              |
| gemini-2.0-pro                                | gemini-2.0-pro-exp-02-05            | 1.25        | 5                                                              |
| gemini-2.0-pro-exp-02-05                      |                                     | 1.25        | 5                                                              |
| gemini-2.5-pro                                | gemini-2.5-pro-preview-06-05        | 1.25        | 10                                                             |
| gemini-2.5-pro-exp-03-25                      |                                     | 1.25        | 10                                                             |
| gemini-2.5-pro-preview-05-06                  |                                     | 1.25        | 10                                                             |
| gemini-2.5-pro-preview-06-05                  |                                     | 1.25        | 10                                                             |
| gpt-3.5-turbo-0301                            | gemini-pro                          | 0.5         | 1                                                              |
| gpt-3.5-turbo-16k-0613                        | gemini-pro                          | 0.5         | 1                                                              |
| dall-e-2                                      |                                     |             | 0.02/pic                                                       |
| dall-e-3                                      |                                     |             | 0.04/pic                                                       |
| gpt-image-1                                   |                                     |             | [pricing](https://platform.openai.com/docs/models/gpt-image-1) |
| flux-1.1-pro                                  |                                     |             | 0.04/pic                                                       |
| flux-1.1-pro-ultra                            |                                     |             | 0.06/pic                                                       |
| flux-dev                                      |                                     |             | 0.025/pic                                                      |
| flux-schnell                                  |                                     |             | 0.003/pic                                                      |
| sdxl-turbo                                    |                                     | FREE        |                                                                |
| imagen-3.0                                    | imagen-3.0-generate-002             |             | 0.04/pic                                                       |
| imagen-3.0-generate-001                       |                                     |             | 0.04/pic                                                       |
| imagen-3.0-generate-002                       |                                     |             | 0.04/pic                                                       |
| imagen-3.0-fast                               | imagen-3.0-fast-generate-001        |             | 0.02/pic                                                       |
| imagen-3.0-fast-generate-001                  |                                     |             | 0.02/pic                                                       |
| tts-1                                         |                                     | 15          |                                                                |
| tts-1-hd                                      |                                     | 30          |                                                                |
| whisper-1                                     |                                     | 0.006/min   |                                                                |
| whisper-large-v3                              |                                     | FREE        |                                                                |
| whisper-large-v3-turbo                        |                                     | FREE        |                                                                |
| test-embedding-ada-002                        |                                     | 0.1         |                                                                |
| text-embedding-3-small                        |                                     | 0.02        |                                                                |
| text-embedding-3-large                        |                                     | 0.13        |                                                                |
| @cf/meta/llama-2-7b-chat-fp16                 |                                     | FREE        |                                                                |
| @cf/meta/llama-2-7b-chat-int8                 |                                     | FREE        |                                                                |
| @cf/mistral/mistral-7b-instruct-v0.1          |                                     | FREE        |                                                                |
| @hf/thebloke/deepseek-coder-6.7b-base-awq     |                                     | FREE        |                                                                |
| @hf/thebloke/deepseek-coder-6.7b-instruct-awq |                                     | FREE        |                                                                |
| @cf/deepseek-ai/deepseek-math-7b-base         |                                     | FREE        |                                                                |
| @cf/deepseek-ai/deepseek-math-7b-instruct     |                                     | FREE        |                                                                |
| @cf/thebloke/discolm-german-7b-v1-awq         |                                     | FREE        |                                                                |
| @cf/tiiuae/falcon-7b-instruct                 |                                     | FREE        |                                                                |
| @cf/google/gemma-2b-it-lora                   |                                     | FREE        |                                                                |
| @hf/google/gemma-7b-it                        |                                     | FREE        |                                                                |
| @cf/google/gemma-7b-it-lora                   |                                     | FREE        |                                                                |
| @hf/nousresearch/hermes-2-pro-mistral-7b      |                                     | FREE        |                                                                |
| @hf/thebloke/llama-2-13b-chat-awq             |                                     | FREE        |                                                                |
| @cf/meta-llama/llama-2-7b-chat-hf-lora        |                                     | FREE        |                                                                |
| @cf/meta/llama-3-8b-instruct                  |                                     | FREE        |                                                                |
| @hf/thebloke/llamaguard-7b-awq                |                                     | FREE        |                                                                |
| @hf/thebloke/mistral-7b-instruct-v0.1-awq     |                                     | FREE        |                                                                |
| @hf/mistralai/mistral-7b-instruct-v0.2        |                                     | FREE        |                                                                |
| @cf/mistral/mistral-7b-instruct-v0.2-lora     |                                     | FREE        |                                                                |
| @hf/thebloke/neural-chat-7b-v3-1-awq          |                                     | FREE        |                                                                |
| @cf/openchat/openchat-3.5-0106                |                                     | FREE        |                                                                |
| @hf/thebloke/openhermes-2.5-mistral-7b-awq    |                                     | FREE        |                                                                |
| @cf/microsoft/phi-2                           |                                     | FREE        |                                                                |
| @cf/qwen/qwen1.5-0.5b-chat                    |                                     | FREE        |                                                                |
| @cf/qwen/qwen1.5-1.8b-chat                    |                                     | FREE        |                                                                |
| @cf/qwen/qwen1.5-14b-chat-awq                 |                                     | FREE        |                                                                |
| @cf/qwen/qwen1.5-7b-chat-awq                  |                                     | FREE        |                                                                |
| @cf/defog/sqlcoder-7b-2                       |                                     | FREE        |                                                                |
| @hf/nexusflow/starling-lm-7b-beta             |                                     | FREE        |                                                                |
| @cf/tinyllama/tinyllama-1.1b-chat-v1.0        |                                     | FREE        |                                                                |
| @hf/thebloke/zephyr-7b-beta-awq               |                                     | FREE        |                                                                |
| black-forest-labs/flux-1.1-pro                |                                     |             | 0.04/pic                                                       |
| black-forest-labs/flux-1.1-pro-ultra          |                                     |             | 0.06/pic                                                       |
| black-forest-labs/flux-canny-dev              |                                     |             | 0.025/pic                                                      |
| black-forest-labs/flux-canny-pro              |                                     |             | 0.05/pic                                                       |
| black-forest-labs/flux-depth-dev              |                                     |             | 0.025/pic                                                      |
| black-forest-labs/flux-depth-pro              |                                     |             | 0.05/pic                                                       |
| black-forest-labs/flux-dev                    |                                     |             | 0.025/pic                                                      |
| black-forest-labs/flux-dev-lora               |                                     |             | 0.032/pic                                                      |
| black-forest-labs/flux-fill-dev               |                                     |             | 0.04/pic                                                       |
| black-forest-labs/flux-fill-pro               |                                     |             | 0.05/pic                                                       |
| black-forest-labs/flux-pro                    |                                     |             | 0.055/pic                                                      |
| black-forest-labs/flux-redux-dev              |                                     |             | 0.025/pic                                                      |
| black-forest-labs/flux-redux-schnell          |                                     |             | 0.003/pic                                                      |
| black-forest-labs/flux-schnell                |                                     |             | 0.003/pic                                                      |
| black-forest-labs/flux-schnell-lora           |                                     |             | 0.02/pic                                                       |
| ideogram-ai/ideogram-v2                       |                                     |             | 0.08/pic                                                       |
| ideogram-ai/ideogram-v2-turbo                 |                                     |             | 0.05/pic                                                       |
| recraft-ai/recraft-v3                         |                                     |             | 0.04/pic                                                       |
| recraft-ai/recraft-v3-svg                     |                                     |             | 0.08/pic                                                       |
| stability-ai/stable-diffusion-3               |                                     |             | 0.035/pic                                                      |
| stability-ai/stable-diffusion-3.5-large       |                                     |             | 0.065/pic                                                      |
| stability-ai/stable-diffusion-3.5-large-turbo |                                     |             | 0.04/pic                                                       |
| stability-ai/stable-diffusion-3.5-medium      |                                     |             | 0.035/pic                                                      |
| ibm-granite/granite-20b-code-instruct-8k      |                                     | 0.100       | 0.500                                                          |
| ibm-granite/granite-3.0-2b-instruct           |                                     | 0.030       | 0.250                                                          |
| ibm-granite/granite-3.0-8b-instruct           |                                     | 0.050       | 0.250                                                          |
| ibm-granite/granite-3.1-2b-instruct           |                                     | 0.030       | 0.250                                                          |
| ibm-granite/granite-3.1-8b-instruct           |                                     | 0.030       | 0.250                                                          |
| ibm-granite/granite-8b-code-instruct-128k     |                                     | 0.050       | 0.250                                                          |
| meta/llama-2-13b                              |                                     | 0.100       | 0.500                                                          |
| meta/llama-2-13b-chat                         |                                     | 0.100       | 0.500                                                          |
| meta/llama-2-70b                              |                                     | 0.650       | 2.750                                                          |
| meta/llama-2-70b-chat                         |                                     | 0.650       | 2.750                                                          |
| meta/llama-2-7b                               |                                     | 0.050       | 0.250                                                          |
| meta/llama-2-7b-chat                          |                                     | 0.050       | 0.250                                                          |
| meta/meta-llama-3.1-405b-instruct             |                                     | 9.500       | 9.500                                                          |
| meta/meta-llama-3-70b                         |                                     | 0.650       | 2.750                                                          |
| meta/meta-llama-3-70b-instruct                |                                     | 0.650       | 2.750                                                          |
| meta/meta-llama-3-8b                          |                                     | 0.050       | 0.250                                                          |
| meta/meta-llama-3-8b-instruct                 |                                     | 0.050       | 0.250                                                          |
| mistralai/mistral-7b-instruct-v0.2            |                                     | 0.050       | 0.250                                                          |
| mistralai/mistral-7b-v0.1                     |                                     | 0.050       | 0.250                                                          |
| mistralai/mixtral-8x7b-instruct-v0.1          |                                     | 0.300       | 1.000                                                          |

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
