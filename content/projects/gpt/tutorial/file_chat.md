---
title: "FileChat/Q&A"
url: "/projects/gpt/file-chat"
---

(page_file_chat)=

## Concept

<https://chat.laisky.com>

Welcome to the FileChat web app, where creating a chatbot from your documents is made simple and secure! With FileChat, you can infuse your own chatbot with wisdom from your select files.

Relax in knowing your uploads and all related data gets the VIP treatment – encrypted with a password that only you know. Remember! The server won't store your password, so keep it safe in your mind's vault.

Currently, we embrace file types like: .md, .doc, .docx, .pdf, .ppt, and .pptx.

<video src="https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4" controls width="800">
  <p>Looks like your browser is not a fan of videos. Fret not! You can click <a href="https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4">here</a> to watch it directly.</p>
</video>

_Don’t see the video? [Click here to watch it](https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4)_

## Building Your Chatbot

Follow these steps to get chatting:

1. First, snag a unique token that's all yours. No token yet? Wipe the token field clean and refresh to conjure one up.

   ![token](https://s3.laisky.com/uploads/2023/07/wiki-filechat-token.png)

2. Pop your files into the upload area, then hang tight while they're being processed.

   ![upload](https://s3.laisky.com/uploads/2023/07/wiki-filechat-upload.png)

3. Once the magic happens, feel free to peruse your uploaded dataset collection.

   ![list](https://s3.laisky.com/uploads/2023/07/wiki-filechat-list-datasets.png)

4. Pick and choose datasets to tutor your very own chat model.

   ![train](https://s3.laisky.com/uploads/2023/07/wiki-filechat-build-bot.png)

5. Give your chat model a zippy name and hit the `Chatbot -> Build` button. Fancy a change? Click `Chatbot -> List` to switch it up later.

   ![build](https://s3.laisky.com/uploads/2023/07/wiki-filechat-build-bot-2.png)

Your documents are tucked away safely, encrypted with AES-256 thanks to your password. **We've got no eyes on your API token or password**.

To chat away, make sure you wield the same password you used during your chatbot's construction. It's key for both file uploads and chatbot building.

{{< hint warning >}}
A word to the wise: forget your password and you're locked out of your previous datasets and chatbot, forever. So remember it well!
{{< hint >}}

## Sharing Your Chatbot

Fancy letting others chat with your bot? Generate a shareable link and spread the joy. Receivers can use the chatbot with no need for any token or password.

{{< hint warning >}}
Heads up! Sharing blows the doors open to all the bot's related data files, sparing only the original file. That means all training datasets and the chat model are out in the open.
{{< hint >}}

Your original file remains your encrypted secret. Link bearers can chat with your bot but won't see the source material. Want them to peek behind the curtain? That's where your password comes into play – share at your discretion.

Sharing steps:

1. Hit `Chatbot -> List`, activate your chosen chatbot, and press `Share`.

   ![list](https://s3.laisky.com/uploads/2023/07/wiki-filechat-share-bot.png)

2. Grab the link that appears and share it like there's no tomorrow.

   ![share](https://s3.laisky.com/uploads/2023/07/wiki-filechat-share-bot-2.png)
