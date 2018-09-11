---
layout: post
comments: true
title: "jekyll blog 내용을 Mac local에서 확인하기"
date:   2018-9-11 00:00:00
author: PJH
categories: "Blog"
tags: "Blog"
---

<h1>
jekyll blog 내용을 Mac local에서 확인하기

</h1>

블로그를 업데이트 하거나 포스트를 업로드할 때 반복해서 확인해야 할 때가 있다.
그럴 때 평소대로 GIT에 올리면 실제로 적용될 때까지 적지 않게 기다려야한다.

그나마 포스트를 쓴다면 작성해서 올리고 잊어버리면 되겠지만 사이트 수정을 해야할 때는 그렇게 하기엔 수정 내용을 확인할 때까지 너무 시간이 많이 걸리게 된다.

그래서 검색해보고 낸 결론이 로컬에서 돌아가게 만들어서 바로바로 확인이 가능하게 만드는 방법이었다.
방법은 다음과 같다.

1. 터미널에서
```
gem install bundler
bundle install
```

1. 자기 블로그가 설치되어 있는 폴더로 이동해서
```
bundle exec jekyll serve
```
을 입력하면 로컬에서 서버가 작동하게 된다.

1. 이후에는 사용하는 웹 브라우저에서
```
http://localhost:4000/
```
로 접속하면 자신의 블로그를 확인 가능하다.

[추가]
그런데 이렇게 하는 것도 한두번이지 매번 확인해야 할 때마다 서버를 켜주는 명령어를 입력하는 것도 정말 귀찮아지더라.
그래서 맥의 automator로 서버 실행과 웹 브라우저로 로컬 서버에 접속하는 것까지 자동 실행하는 플로우를 만들었다.

내용은 다음과 같다.

1. automator 실행
1. "apple script 실행"을 찾아서 창에 떨궈준다.
1. 다음 내용을 기입한다.

```
tell application "Terminal"
	do script "cd // ; cd /자기 블로그가 설치되어 있는 폴더/ ; bundle exec jekyll serve"
end tell

tell application "Google Chrome"
	open location "http://localhost:4000/"
end tell
```
