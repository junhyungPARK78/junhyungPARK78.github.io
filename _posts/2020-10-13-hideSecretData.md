---
layout: post
comments: true
title:  "GitHub Actions를 이용할 때 숨겨야하는 정보를 숨기기"
date:   2020-10-13 16:09:00 +0900
author: PJH
categories: [Programming, Github]
tags: [Programming, Github]
cover: "/assets/coverImage_Programing.png"
---

# GitHub Actions를 이용할 때 숨겨야하는 정보를 숨기기

![title](/assets/post_img/2020-10-13-1609/watchAndProgrammingAndSecurity.png)

일전에 소개한 
[「GitHub Actions을 이용해서 시간 베이스로 자동 실행시키기」]({{ site.baseurl }}{% link _posts/2020-10-02-timeBasedAutomationPythonScriptWithGitAction.md %})
를 만들다보면, GitHub에 올려야하는 내용이 공개되게 되는데, 그 안에 key 값을 그대로 넣어놓거나 하면, 보안 상으로 문제가 있게 된다.

![title](/assets/post_img/2020-10-13-1609/flow01.png)

이 부분을 해결하기 위해서, 다음의 조건을 만족하는 방법을 찾아보았고,
- 외부에서는 특정한 값이 전혀 보이지 않는다.
- 써야할 때는 상수로 가져다 쓸 수 있도록 한다.

이래저래 적용해보면서 어떻게 하면 되는지 감잡을 수 있었다.
삽질했던 내용을 여기 정리해 둔다.

---

## 숨겨야할 상수 만들기

![title](/assets/post_img/2020-10-13-1609/flow02.png)

Actions를 작업하려는 레포지토리에서 Settings에 접속한다.

![title](/assets/post_img/2020-10-13-1609/flow03.png)

Secrets 선택하고 New secret 클릭한다.

![title](/assets/post_img/2020-10-13-1609/flow04.png)

상수명(Name)과 값(Value)을 집어넣고 Add Secret 버튼을 클릭한다.
참고로, 여기 입력한 값은 일단 결정하고 나면 자신도 볼 수 없게 된다.

![title](/assets/post_img/2020-10-13-1609/flow05.png)

여기까지 보이면 이 상수값을 Actions에서 가져다 쓸 수 있게 된다.

## 상수를 yml 파일에 등록하기

<script src="https://gist.github.com/junhyungPARK78/2690eec0e68ffc690ed2f000c04f6a90.js"></script>

35 라인의 형식으로 상수값을 추가해나간다.


## 등록되어 있는 상수를 python 파일에서 사용하기

<script src="https://gist.github.com/junhyungPARK78/9955b9b023ef6e4cb0e9fca92cf09ac8.js"></script>

10 라인의 형식으로 상수를 지정한다.
이때까지의 작업으로 python 스크립트에서 값이 숨겨져있는 상수를 사용할 수 있게 된다.

---

## 정리

![title](/assets/post_img/2020-10-13-1609/flow06.png)

안전하게 다루어야할 정보를 안전하게 사용할 수 있도록 하는 방법을 실행시키고, 그걸 정리할 수 있어서 기분이 좋다!
