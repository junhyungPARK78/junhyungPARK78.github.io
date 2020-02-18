---
layout: post
comments: true
title: unity → script에서 inspector에 문자열 입력하도록 조정하기
date:   2018-08-13 14:13:00 +0900
author: PJH
categories: "Unity"
tags: "unity script"
cover:
---

<h1>
unity script에서 inspector에 문자열 입력하게 만들기
</h1>

일단 스크립트 내용 :

<script src="https://gist.github.com/junhyungPARK78/76bd80087c5a95e59aa2a3d6728cadf5.js"></script>

```public string SceneName;```
부분이 인스펙터에 글자 입력하는 옵션이 나오도록 하는 부분.



```SceneManager.LoadScene(SceneName);```
부분에서 입력받은 이름의 씬으로 이동하도록 되어 있다.



추가로 더 알고 싶은 사항 :

- 그냥 텍스트로 입력하게 해 두었는데, 씬을 선택할 수 있도록 해 주는 방법은 없을까?
