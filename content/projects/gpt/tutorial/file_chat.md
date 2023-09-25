---
title: "FileChat/Q&A"
url: "/projects/gpt/file-chat"
---

(page_file_chat)=

## Concept

<https://chat.laisky.com>

This is a web application based on openai chatgpt embeddings,
you can trainning your own chat model based on your own files.

All files you uploaded, and all data related to your files will be encrypted by your own password,
the server will not save your password, so please remember your password.

Current support file types: .md, .doc, .docx, .pdf, .ppt, .pptx.

<video src="https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4" controls width="800">
  <p>Your browser does not support the video tag</p>
  <p>open <a href="https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4">https://s3.laisky.com/uploads/2023/07/private-knowledge-base.mp4</a></p>
</video>

## Build Chatbot

Steps:

1. Please make sure you have generated a unique token that belongs only to you. If you haven't, please delete the entire token field and refresh the page.

   ![token](https://s3.laisky.com/uploads/2023/07/wiki-filechat-token.png)

2. Upload your files, and wait for the processing to complete.

   ![upload](https://s3.laisky.com/uploads/2023/07/wiki-filechat-upload.png)

3. After the processing is completed, you can list all the datasets you have uploaded.

   ![list](https://s3.laisky.com/uploads/2023/07/wiki-filechat-list-datasets.png)

4. Select any number of datasets to train your own chat model.

   ![train](https://s3.laisky.com/uploads/2023/07/wiki-filechat-build-bot.png)

5. Named your chat model, and click `Chatbot -> Build` button.
   You can change the chatbot later by clicking `Chatbot -> List` button.

   ![build](https://s3.laisky.com/uploads/2023/07/wiki-filechat-build-bot-2.png)

All files uploaded by the user, as well as all datasets generated from the files,
are encrypted using the user's password with AES-256 encryption.
**The server does not store the user's API token and password**.

When using the chatbot, the user must ensure that they have correctly entered the same password used when building the chatbot.
The password used when uploading files must be the same as the password used when building the chatbot.

{{< hint warning >}}
If the user forgets their password, they will no longer be able to use their previous datasets and chatbot.
{{</ hint >}}

## Share Chatbot

Users can generate a shareable link for the chatbot and share it with others.
People who receive the link can use the chatbot directly without entering any API token or password.

{{< hint warning >}}
Sharing the chatbot will unlock all data files related to this chatbot except for the original file,
including all training datasets and the chatbot itself.
{{</ hint >}}

The original file uploaded by the user will always be encrypted.
Although people who receive the link can chat with the chatbot,
they cannot access the reference materials of the original file.
To access these materials, they still need to enter the password set by the user when uploading the file.
You can consider whether or not to tell others your password.

Steps:

1. Click `Chatbot -> List` button, enable the chatbot you want to share, and click `Share` button.

   ![list](https://s3.laisky.com/uploads/2023/07/wiki-filechat-share-bot.png)

2. Copy the link and share it with others.

   ![share](https://s3.laisky.com/uploads/2023/07/wiki-filechat-share-bot-2.png)
