---
layout: post
comments: true
title:  "GitHub Actions를 이용할 때 숨겨야하는 정보를 숨기기"
date:   2020-10-05 15:55:00 +0900
author: PJH
categories: [Programming, Github]
tags: [Programming, Github]
cover: "/assets/coverImage_Programing.png"
---

# GitHub Actions를 이용할 때 숨겨야하는 정보를 숨기기

![title](/assets/post_img/2020-10-05-1555/watchAndProgrammingAndSecurity.png)

일전에 소개한 
[「GitHub Actions을 이용해서 시간 베이스로 자동 실행시키기」]({{ site.baseurl }}{% link _posts/2020-10-02-timeBasedAutomationPythonScriptWithGitAction.md %})
를 만들다보면, GitHub에 올려야하는 내용이 공개되게 되는데, 그 안에 key 값을 그대로 넣어놓거나 하면, 보안 상으로 문제가 있게 된다.

![title](/assets/post_img/2020-10-05-1555/flow01.png)

이 부분을 해결하기 위해서, 다음의 조건을 만족하는 방법을 찾아보았고,
- 외부에서는 특정한 값이 전혀 보이지 않는다.
- 써야할 때는 상수로 가져다 쓸 수 있도록 한다.

이래저래 적용해보면서 어떻게 하면 되는지 감잡을 수 있었다.
삽질했던 내용을 여기 정리해 둔다.

---














## 소제목 1

-------->
일단 여기 그림 넣기
<--------

-------->
소제목에 대한 설명하기
<--------

---

## 그 다음 소제목

---

## 정리
-------->
전체적인 설명, 정리하기
<--------

---

## 참고 기능

### 【이미지 등록방법】
#### 「기본」
![title](/assets/post_img/myComputer.jpg)

#### 「리사이즈」
![title](/assets/post_img/myComputer.jpg){: width="100px" height="100px"}
![title](/assets/post_img/myComputer.jpg){: width="100px"}
    └비율 유지하면서 리사이즈

### 【code 관련】

#### 「간단한 인라인 코드」

asdf`asdf`asdf

#### 「복수 줄의 코드」
```
asas
asas
asasdf
```
