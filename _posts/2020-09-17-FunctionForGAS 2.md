---
layout: post
comments: true
title: "GAS에서 함수 사용하기"
date: 2020-09-17 14:47:00 +0900
author: PJH
categories: [Programming]
tags: [Programming]
cover:
---

<h1>
Google Apps Script에서 함수를 사용하는 방법
</h1>

### 문제

- 조금만 코드가 길어지면 가독성이 팍팍 떨어진다.
- 그에 따라 함수 별로 파일을 나눈다거나 하는 관리 기법이 필요해지는데, Google Apps script에서는 어떻게 해야하는지를 알아본다.

### 해결

설명하고 자시고도 없다. Google Apps Script 에서는 프로젝트 별로 관리가 되기 때문에, 파일이 다르더라도 ```함수명(인수)```의 방식으로 그대로 사용해주면 된다.

### 주의점

- 함수 명 그대로 쓰기 때문에, 반대로 얘기하자면 함수 명 겹치지 않게 조심해야한다.