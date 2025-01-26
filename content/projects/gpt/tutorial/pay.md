---
title: "Pay"
url: "/projects/gpt/pay"
---

(page_gpt_pay)=

## Introduction 🎉

_[(👉 中文版)](@page_gpt_pay_cn)_

Free users can only access a limited set of models and features. To unlock all supported models and features, simply add credits on my One-API platform to become a paid user. Read on for purchase details and a list of supported models.

If you have any questions, feel free to email me at `chat@laisky.com`.

Updates are posted on my Telegram Channel: <https://t.me/laisky_oai>

[Check supported models and rates](@gpt_chat_support_models)

## Purchase

### Disclaimer

This is a non-profit project. I don’t charge any handling fees or markups, and I use a standard exchange rate of 8:1 for USD:RMB. Because cross-border payments for OpenAI/Anthropic can be challenging, the exchange costs are higher—these are not service fees I collect.

I’ve noticed some third-party channels provide poor-quality solutions at cheaper prices, so I’ve decided not to integrate any third-party channels. I only use official channels for OpenAI, Azure, Groq, Anthropic, Google, AWS, Cloudflare, DeepSeek, and Replicate.

**Everything here comes straight from the official interfaces.**

### Register an Account

Sign up at <https://oneapi.laisky.com/register>.

### Purchase Recharge Code

You can send payments through Alipay, WeChat, OKX, BINANCE, or BYBIT. After transferring, please email me (`chat@laisky.com`) the transaction amount so I can process it promptly and send you a recharge code.

For RMB via Alipay/Wechat, I’ll convert your transfer to USD at the mentioned rate. For crypto, I only accept stablecoins like USDT/USDC/FDUSD/DAI at a 1:1 rate with USD.

- [Alipay](https://s3.laisky.com/uploads/2025/01/pay_ali.JPG)
- [WeChat](https://s3.laisky.com/uploads/2025/01/pay_wechat.JPG)
- OKX UID: `573443235054776568`
- BINANCE UID: `570130488`
- BYBIT UID: `262385596`

If you need other on-chain payment address, please contact me directly.

### Using the Recharge Code

Go to <https://oneapi.laisky.com/topup>, enter the recharge code I provided, then click **Redeem**.

## Refunds

If you need a refund, just email me. We'll calculate the refund based on the market price when you added the funds. 📈

## How to Use LLM Services

### Getting Your API Token

Visit <https://oneapi.laisky.com/token> to create your token.

![](https://s3.laisky.com/uploads/2024/03/create-token.png?v=3)

### Web Interface

The easiest way to start is to enter your API key in the top right corner at <https://chat.laisky.com/>.

Simply refresh the page after entering your API key to unlock all features.

![](https://s3.laisky.com/uploads/2023/12/apitoken.png)

### Using Third-Party Apps

Important: All requests must go through our gateway instead of directly to OpenAI. When setting up third-party apps, you'll need to configure both the `API_BASE` and `API_KEY`:

- Set `API_BASE` to: `https://oneapi.laisky.com` or `https://oneapi.laisky.com/v1`
- Set `API_KEY` to your personal token

Note: The `API_BASE` URL format varies between apps. Some need just `v1`, others don't, and some require the full path `/v1/chat/completions`. Be sure to check your app's documentation for the correct format.

Here are some popular apps you can use:

#### Cursor

<https://www.cursor.com/>

![](https://s3.laisky.com/uploads/2024/09/cursor.png)

#### OpenAI Translator

[Chrome Web Store - OpenAI Translator](https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc)

![](https://s3.laisky.com/uploads/2023/12/openai-translator.png)

#### Immersive Translate

[Chrome Web Store - Immersive Translate](https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)

![](https://s3.laisky.com/uploads/2023/12/immersive-translate.png)

#### GPTCommit

[GitHub - GPTCommit](https://github.com/zurawiki/gptcommit)

![](https://s3.laisky.com/uploads/2023/12/gpt-commit.png)

## Permanent Storage on Arweave

Your API key also grants access to our Arweave file storage service. Upload files for permanent storage using our GraphQL API or Telegram Bot. For detailed documentation, visit <https://blog.laisky.com/p/arweave/>.

### Telegram Bot Integration

[Add our Bot](https://t.me/laisky_alert_bot) on Telegram. After linking your account as shown below, you can directly send files for permanent storage on Arweave.

![](https://s3.laisky.com/uploads/2025/01/arweave-bot.jpeg)

### GraphQL API Integration

Endpoint: `https://gq.laisky.com/query/`

To upload files, convert them to base64 format and call the `ArweaveUpload` endpoint with the `fileB64` parameter:

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

## Disclaimer

This is a non-profit project - I don't charge any service fees and simply provide access to these services. While I can't guarantee service quality, I'm here to help if you run into any issues.

All content is generated by users or AI - I'm not responsible for any outputs.

If you encounter any problems or need a refund, just drop me an email. I'll do my best to help quickly!
```
