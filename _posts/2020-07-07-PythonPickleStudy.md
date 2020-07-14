---
layout: post
comments: true
title:  "python의 파일 저장 방법 중 'pickle'에 대해서"
date:   2020-07-07 11:53:00 +0900
author: PJH
categories: "Programming"
tags: "Programming", "python"
cover:
---

<h1>
python에서 파일을 저장할 때 string 이외의 형식을 저장하는 방법을 알아본다.
</h1>

### 문제

기본적으로는 txt 파일로 저장할 때는 string 형식 이외에는 저장할 수가 없다.

나는 조그마한 프로그램을 만들면서 옵션 저장을 dictionary 형식으로 관리해보고 싶었기 때문에,
그 방법을 알아보니 'pickle' 이라는 방식을 알게 되었다.

### 사용 방법

<script src="https://gist.github.com/junhyungPARK78/db97c5494e0244a3225951bf42dd89d0.js"></script>

사용 방식은 위와 같다.

### 기타

- 저장할 때 덧붙여 쓰는 방식은 없다. 읽어들여서 편집한 후에, 다시 싹 다 세이브 하는 방법이 되어야할 듯.
- 저장 형식은 바이너리면가 된다. 용량이 어떻게 되는거지?
  - 키 1000개 짜리 딕셔너리로 저장해보았다.
  - 바이너리 : 5KB
  - 텍스트 : 29KB