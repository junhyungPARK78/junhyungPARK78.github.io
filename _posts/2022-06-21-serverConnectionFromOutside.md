---
layout:     post
comments:   true
title:      "내 PC에서 돌리는 서버에 외부에서 접속 가능하게 하기"
date:       2022-06-21 +0900
author:     PJH
# categories: [Dummy]
tags:       [python, programming]
---

![title](/assets/images/2022-06-21-serverConnectionFromOutside_001.png){: width="125px"}

파이썬 공부하면서 flask로 가볍게 만들어 둔 서버로 외부에서 접속할 필요가 생겼다.
여러가지 방법이 있지만 그냥 간단하게 할 수 있는 **localtunnel** 서비스를 알게 되었다.
해보면서 알게된 순서를 정리한다.

---

## 우선, 전제

- localtunnel은 node.js로 만들어졌으니 npm [^1]으로 설치할 필요가 있다.
  - [Node.js 설치하기](https://nodejs.org/ko/)：가능하면 LTS버전으로 설치한다.
  - 설치 후 터미널에서 `node -v` 로 확인한다.
  - npm 설치도 확인한다. 터메널에서 `npm -v`

[^1]: **N**ode.js **P**ackage **M**anager

## 순서는...

- localtunnel 설치하기
  - `npm install -g localtunnel`
- localtunnel 실행하기
  - `lt --port [포트번호] -subdomain [도메인 이름] --print-requests`

---

## 출처 (참고문헌)
- [localtunnel（GITHUB）](https://github.com/localtunnel/localtunnel)
- [localtunnel（WEB）](https://localtunnel.github.io/www/)
  - [npm 설치 및 npm 설치 버전 확인 방법](https://joyfulhome.tistory.com/180)
  - https://kibua20.tistory.com/151
- [그 외의 방법으로 'ngrok'도 괜찮다.](https://ngrok.com/)

---

## 정리

flask 서버도 대응하고, 외부 도메인 연결도 가능해지니, 여러모로 할 수 있는 범위가 늘어났다!

![](https://www.dropbox.com/s/cbrqu33173gdbod/gutspose_man.png?raw=1){: width="200px"}
