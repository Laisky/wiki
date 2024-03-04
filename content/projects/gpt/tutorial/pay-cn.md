---
title: "Pay"
url: "/projects/gpt/pay/cn"
bookhidden: true
---

(page_gpt_pay_cn)=

## Introduction

_[(👉 English)](@page_gpt_pay)_

有两种方式可以解锁所有的功能：

1. 使用自己的 openai apikey
2. 从我这购买专用的 apikey

请使用邮件联系我：`chat@laisky.com`.

## 购买方式

先在 <https://oneapi.laisky.com/register> 注册一个账户，然后把账户名给我，就可以充值使用了，充值方式可以 微信/支付宝/Paypal 转账。目前没有接入任何充值渠道，所以采取邮件联系 + 转账的方式。

这是一个非盈利项目，我不赚取任何手续费和差价，汇率统一按照 8 计算。因为众所周知的原因，OpenAI 的跨境支付很困难，所以汇率成本较高，不是我收的劳务费。

Ps. 实际使用时，不同的 LLM 渠道可能会存在不同的折扣，个别渠道甚至可能会免费。我会自动选择当时折扣最高的渠道，具体用量请参考系统日志。

![](https://s3.laisky.com/uploads/2024/03/oneapi-charge.png)

## 退款方式

请邮件联系，按照充值时的市价退还。

## 使用方式

### 获取 token

![](https://s3.laisky.com/uploads/2024/03/create-token.png)

### 网页使用

最简单的方式就是在 <https://chat.laisky.com/> 右上角填入你的 apikey 使用。

填入你的 apikey 后刷新页面，即可解锁所有功能。

![](https://s3.laisky.com/uploads/2023/12/apitoken.png)

### 第三方使用

你必须通过我的网关来转发请求，而不能直接向 openai 发起请求。当你使用第三方 App 时，则必须在第三方 App 上同时设置 `API_BASE` 和 `API_KEY`。将 `API_BASE` 设置为我的网关地址 `https://oneapi.laisky.com`，API_KEY ` 则填入你的 token。

（[点击查阅目前支持的模型](@gpt_chat_support_models)）

一些第三方产品的示例:

#### OpenAI translator

[https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc](https://chromewebstore.google.com/detail/openai-translator/ogjibjphoadhljaoicdnjnmgokohngcc)

![](https://s3.laisky.com/uploads/2023/12/openai-translator.png)

#### Immersive Translate

[https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh](https://chromewebstore.google.com/detail/immersive-translate-web-p/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)

![](https://s3.laisky.com/uploads/2023/12/immersive-translate.png)

#### GPTCommit

[https://github.com/zurawiki/gptcommit](https://github.com/zurawiki/gptcommit)

![](https://s3.laisky.com/uploads/2023/12/gpt-commit.png)

## 免责声明

这不是商业项目，是非营利性的，我不收取任何费用，只是提供一个使用渠道。不保证任何服务质量。

内容都来自用户或 AI，我也不对任何输出负责。

遇到任何问题可以随时联系我，我会力所能及的尽快解决。退款也请邮件联系。
