---
layout: post
comments: true
title: "GitHub Actions을 이용해서 시간 베이스로 자동 실행시키기"
date: 2020-10-02 11:09:00 +0900
author: PJH
categories: [Programming, Github]
tags: [Programming, Github]
cover: "/assets/coverImage_Programing.png"
---

# GitHub Actions을 이용해서 시간 베이스로 자동 실행시키기

![title](/assets/post_img/2020-10-02-1109/watchAndProgramming.png)

어떤 프로그램을 작성해서, 일정한 시간에 자동으로 실행하게 만들기 위해서는 여러가지 방법이 있었다.

1. google apps script를 이용해서 실행하기
1. 집에 서버 설치해서 서버에서 일정 시간 받아와서 그 시간이 되면 지정된 프로그램을 실행하게 만들기

google apps script 를 사용하려면 아무래도 주로 사용하는 언어도 아니다보니 이래저래 제한이 생기고, 서버를 따로 설치한다는 건 지금으로는 관심도 별로 없는 쪽까지 손을 대야하니 너무 과도한 느낌이 있다.

그러던 중에 아주 우연히 GitHub의 Actions 기능을 이용하면 GitHub에 올라가있는 코드를 일정한 규칙에 의해서 실행시킬 수 있다는 것을 알게 되었다.

이걸 이용하면 주로 사용하는 언어를 사용할 수 있으면서도, 따로 서버를 설치한다거나 할 필요도 없어진다.

---

## 주의점

- GitHub Actions에는 여러가지 실행 방식이 존재하지만, 여기서는 다음 조건에 대해서만 한해서 설명한다.
    - Python 스크립트
    - 시간 기준 실행

---

## 작업 순서 (1)

### GitHub에 프로그램 푸쉬

GitHub을 이용한 서비스이므로 사용할 프로그램은 GitHub에 푸시하자.
프로그램의 폴더 계층은 일단 최상층으로 한다.

### Action 만들기

1. GitHub의 레포지토리 페이지에 있는 메뉴중 「Actions」를 선택한다.
![title](/assets/post_img/2020-10-02-1109/flow01.png){: width="300px"}

1. 파이썬 스크립트 하나를 실행시키는 정도라면, 위 스크린샷의 「Python application」으로 충분하다.
이걸 선택.
![title](/assets/post_img/2020-10-02-1109/flow02.png){: width="300px"}

### yml 파일

1. 버튼을 누르면 텍스트 에디터가 나타난다. 다음 내용을 붙여넣는다.
<script src="https://gist.github.com/junhyungPARK78/d7331a783720f3bb9cf42328b5c6c6d5.js"></script>

1. 일단 Start commit 버튼을
![title](/assets/post_img/2020-10-02-1109/flow03.png)
누른다.

### yml 파일 수정

8행 : `- cron: "* 10 1 11 *"`

크론 표현식으로 어떤 일정으로 파이썬 스크립트를 실행시킬지 지정한다.

문법을 외우다기보다는 [crontab.guru](https://crontab.guru/)
에서 조정하는 것이 훨씬 편했다.

32행 : `pip install bs4 requests`

파이썬 스크립트에서 사용한 모듈 중에서 인스톨이 필요한 모듈을 지정한다.

33행 : `- run: python sendCWMessage.py`

실행하려는 파이썬 스크립트를 지정한다.

---

## 정리

간단한 스크립트의 실행만이라면, 몇가지의 수정만으로 편하게 시간 지정해서 실행이 가능해진다.
이런 건 적극적으로 써 줘야지.

![title](/assets/postEnd.png){: width="300px"}
