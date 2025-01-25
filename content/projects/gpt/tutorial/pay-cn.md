---
title: "Pay"
url: "/projects/gpt/pay/cn"
bookhidden: true
---

(page_gpt_pay_cn)=

## Introduction

_[(👉 English)](@page_gpt_pay)_

免费用户只能使用有限的模型和功能，通过在我的 One-API 平台上充值成为付费用户，可以解锁所有支持的模型和功能，具体的购买方式和支持的模型列表请继续阅读下文。

有任何问题请使用邮件联系我：`chat@laisky.com`.

更新信息会发布在 Telegram Channel: <https://t.me/laisky_oai>

[[]点击查阅目前支持的模型和费率](@gpt_chat_support_models)

## 充值方式

### 声明

这是一个非盈利项目，我不赚取任何手续费和差价，汇率统一按照 8 计算。因为众所周知的原因，OpenAI/Anthropic 的跨境支付很困难，所以汇率成本较高，不是我收的劳务费。

因为发现有第三方渠道以次充好，拉低了模型质量。所以虽然很多第三方能够给出很低的价格，但是我还是决定不再接入第三方渠道了，只提供 OpenAI、Azure、Groq、Anthropic、Google、AWS、Cloudflare、DeepSeek、Replicate 的官方渠道。

**本站保证所有内容都来自于上面列举的官方接口，不接入任何其他第三方渠道**

### 注册账户

首先在 <https://oneapi.laisky.com/register> 注册一个账户。

### 购买充值码

可以通过 支付宝/微信/OKX/BINANCE/BYBIT 的形式给我转账，然后给我发送邮件（`chat@laisky.com`）告知转账金额和账单信息，我会尽快处理并给你回复充值码。

支付宝的人民币转账按前文所述的汇率换算为 USD。crypto 只接受 USDT/USDC/FDUSD/DAI 等主流稳定币，和 USD 按照 1:1 兑换。

- [支付宝](https://s3.laisky.com/uploads/2025/01/pay_ali.JPG)
- [微信](https://s3.laisky.com/uploads/2025/01/pay_wechat.JPG)
- OKX UID: `573443235054776568`
- BINANCE UID: `570130488`
- BYBIT UID: `262385596`

如果需要其他链上汇款方式，请直接联系我。

### 使用充值码

在 <https://oneapi.laisky.com/topup> 输入我提供的充值码，然后点击 **Redeem** 即可。

## 退款方式

请邮件联系，按照充值时的市价退还。

## LLM 使用方式

### 获取 token

<https://oneapi.laisky.com/token>

![](https://s3.laisky.com/uploads/2024/03/create-token.png?v=3)

### 网页使用

最简单的方式就是在 <https://chat.laisky.com/> 右上角填入你的 apikey 使用。

填入你的 apikey 后刷新页面，即可解锁所有功能。

![](https://s3.laisky.com/uploads/2023/12/apitoken.png)

### 第三方使用

你必须通过我的网关来转发请求，而不能直接向 openai 发起请求。当你使用第三方 App 时，则必须在第三方 App 上同时设置 `API_BASE` 和 `API_KEY`。将 `API_BASE` 设置为我的网关地址 `https://oneapi.laisky.com` 或 `https://oneapi.laisky.com/v1`，`API_KEY` 则填入你的 token。

注意 `API_BASE` 的 URL PATH 部分，没有统一公认的标准，不同的产品有不同的要求，有的需要填写 `v1`，有的则不需要，还有些需要填写完整的 `/v1/chat/completions`。请认真阅读你所使用产品的文档，确认正确的格式。

一些第三方产品的示例:

#### Cursor

<https://www.cursor.com/>

![](https://s3.laisky.com/uploads/2024/09/cursor.png)

#### OpenAI translator

[https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc](https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc)

![](https://s3.laisky.com/uploads/2023/12/openai-translator.png)

#### Immersive Translate

[https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh](https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)

![](https://s3.laisky.com/uploads/2023/12/immersive-translate.png)

#### GPTCommit

[https://github.com/zurawiki/gptcommit](https://github.com/zurawiki/gptcommit)

![](https://s3.laisky.com/uploads/2023/12/gpt-commit.png)

## Permanent storage on Arweave

使用本站的 API-KEY，也可以调用我的 Arweave 文件上传接口，可以通过 GraphQL/Telegram Bot 等方式将文件上传至 Arweave 永久存储，具体方法可见 <https://blog.laisky.com/p/arweave/>。

![](https://s3.laisky.com/uploads/2025/01/ar-upload-demo.png)

## 免责声明

这不是商业项目，是非营利性的，我不收取任何费用，只是提供一个使用渠道。不保证任何服务质量。

内容都来自用户或 AI，我也不对任何输出负责。

遇到任何问题可以随时联系我，我会力所能及的尽快解决。退款也请邮件联系。
