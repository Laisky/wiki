---
title: "Pay"
url: "/projects/gpt/pay"
---

(page_gpt_pay)=

## Introduction 🎉

_[(👉 中文版)](@page_gpt_pay_cn)_

Free users can only access a limited set of models and features. By adding credit on the One‑API platform, you become a paid user and unlock all supported models and features. See the sections below for purchase methods and the list of supported models.

If you have any questions, email me at `chat@laisky.com`.

Updates are posted on the Telegram channel: <https://t.me/laisky_oai>

[View the current supported models and rates](https://oneapi.laisky.com/models)

The project source code is available on GitHub. If you encounter issues, you can open an Issue or submit a PR directly: <https://github.com/laisky/one-api>

## Top‑up Methods

### Statement

Because some third‑party channels provide low‑quality models, I have decided to stop using any third‑party providers. Only official channels from OpenAI, Azure, Groq, Anthropic, Google, AWS, Cloudflare, DeepSeek, and Replicate are supported.

**All content on this site comes exclusively from the official APIs listed above. No other third‑party channels are used.**

### Register an Account

First, create an account at <https://oneapi.laisky.com/register>.

### Purchase a Top‑up Code

Transfer funds via Alipay, WeChat, OKX, Binance, or Bybit, then email me (`chat@laisky.com`) with the transfer amount and transaction details. I will process the request quickly and send you a top‑up code.

Wechat/Alipay RMB transfers are converted to USD using the fixed exchange rate 8:1. Crypto payments accept major stablecoins such as USDT, USDC, FDUSD, DAI, and are exchanged 1:1 with USD.

- [Alipay](https://s3.laisky.com/uploads/2025/01/pay_ali.JPG)
- [WeChat](https://s3.laisky.com/uploads/2025/01/pay_wechat.JPG)
- [OKX](https://s3.laisky.com/uploads/2025/10/pay_okx.JPG)
- [BINANCE](https://s3.laisky.com/uploads/2025/10/pay_binance.PNG)
- Bybit UID: `262385596`

If you need other blockchain‑based payment methods, contact me directly.

### Use a Top‑up Code

Enter the code you received at <https://oneapi.laisky.com/topup> and click **Redeem**.

## Refund Policy

Email me for a refund; the amount will be returned at the market price at the time of the original top‑up.

## Using LLMs

### Get a Token

<https://oneapi.laisky.com/token>

![](https://s3.laisky.com/uploads/2024/03/create-token.png?v=3)

### Web Interface

The simplest way is to enter your API key in the upper‑right corner of <https://chat.laisky.com>.

After entering the API key, refresh the page to unlock all features.

![](https://s3.laisky.com/uploads/2023/12/apitoken.png)

## Third‑Party Integration

All requests must go through my gateway; direct calls to OpenAI are not allowed. When using a third‑party app, set both `API_BASE` and `API_KEY` in the app:

- `API_BASE` → `https://oneapi.laisky.com` or `https://oneapi.laisky.com/v1`
- `API_KEY` → your token

Be aware that the URL path for `API_BASE` varies by product. Some require `/v1`, others need the full path `/v1/chat/completions`. Consult the documentation of the tool you are using to determine the correct format.

Examples for third‑party products:

### Claude Code

```sh
export ANTHROPIC_MODEL="openai/gpt-oss-120b"
export ANTHROPIC_BASE_URL="https://oneapi.laisky.com/"
export ANTHROPIC_AUTH_TOKEN="sk-xxxxxxx"
```

### Codex Cli

```sh
# vi $HOME/.codex/config.toml

model = "gemini-2.5-flash"
model_provider = "laisky"

[model_providers.laisky]
# Name of the provider that will be displayed in the Codex UI.
name = "Laisky"
# The path `/chat/completions` will be amended to this URL to make the POST
# request for the chat completions.
base_url = "https://oneapi.laisky.com/v1"
# If `env_key` is set, identifies an environment variable that must be set when
# using Codex with this provider. The value of the environment variable must be
# non-empty and will be used in the `Bearer TOKEN` HTTP header for the POST request.
env_key = "sk-xxxxxxx"
# Valid values for wire_api are "chat" and "responses". Defaults to "chat" if omitted.
wire_api = "responses"
# If necessary, extra query params that need to be added to the URL.
# See the Azure example below.
query_params = {}
```

### Cursor

<https://www.cursor.com>

![](https://s3.laisky.com/uploads/2024/09/cursor.png)

### OpenAI Translator

[OpenAI Translator Extension](https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc)

![](https://s3.laisky.com/uploads/2023/12/openai-translator.png)

### Immersive Translate

[Immersive Translate Extension](https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)

![](https://s3.laisky.com/uploads/2023/12/immersive-translate.png)

### GPTCommit

[GPTCommit Repository](https://github.com/zurawiki/gptcommit)

![](https://s3.laisky.com/uploads/2023/12/gpt-commit.png)

## Permanent Storage on Arweave

With your API key you can also use the Arweave file‑upload API to store files permanently on Arweave via GraphQL, Telegram Bot, etc. See the blog for more details: <https://blog.laisky.com/p/arweave>.

### Telegram Bot

Add the bot on Telegram: [@laisky_alert_bot](https://t.me/laisky_alert_bot). After linking your account as shown below, you can send files directly to be stored on Arweave.

![](https://s3.laisky.com/uploads/2025/01/arweave-bot.jpeg)

### GraphQL API

- Endpoint: `https://gq.laisky.com/query/`
- Header: `Authorization: Bearer ${API_KEY}`

Convert the file to a base64 string and call the `ArweaveUpload` mutation with the `fileB64` argument.

```js
// request
mutation ar {
  ArweaveUpload(
    fileB64: "aGVsbG8="
  ) {
    file_id
  }
}

// response
{
    "data": {
        "ArweaveUpload": {
            "file_id": "TprLA3XlyRHlxb9jIG0TCV6v4rimGkMDReKyVMp_iMY"
        }
    }
}
```

Example with `curl`:

```sh
curl --location 'https://gq.laisky.com/query/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-xxxxxxx' \
--data '{"query":"mutation ar {\r\n  ArweaveUpload(\r\n    fileB64: \"aGVsbG8=\"\r\n  ) {\r\n    file_id\r\n  }\r\n}","variables":{}}'
```

## Disclaimer

This is not a commercial project; it is non‑profit and I do not charge any fees. I only provide a usage channel and make no guarantees about service quality.

All content originates from users or AI; I am not responsible for any output.

If you encounter any issues, feel free to contact me. I will address them as quickly as possible. Refund requests should also be made via email.
