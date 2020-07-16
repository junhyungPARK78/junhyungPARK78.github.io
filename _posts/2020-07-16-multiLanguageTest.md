---
layout: post
comments: true
title: "python에서 다국어 지원을 할 때의 아이디어"
date: 2020-07-16 18:59:00 +0900
author: PJH
categories: "Programming"
tags: "Programming"
cover:
---

<h1>
python에서 다국어 지원을 할 때의 아이디어
</h1>

### 문제

미리 csv 파일로 다국어 파일을 만들어 놓고 옵션 등으로 보여지는 언어를 결정하고 싶었다.

### 해결

다음 코드 방식으로 해결.

<script src="https://gist.github.com/junhyungPARK78/960c9b335042d8ac949dbd7ebd70989f.js"></script>

- csv 형식으로 키, 각 언어의 번역을 작성한다.
- 딕셔너리 형식으로 키와 해당 언어의 번역본을 짜맞춘다.
- 코드 내에서는 해당 키로만 불러들여서 어떤 언어로 설정되어 있더라도 제대로 보이게 만든다.