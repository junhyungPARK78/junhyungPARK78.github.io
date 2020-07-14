---
layout: post
comments: true
title:  "python에서 외부 파일을 사용하고 있을 때 주의점"
date:   2020-07-14 14:46:00 +0900
author: PJH
categories: "Programming"
tags: "Programming", "python"
cover:
---

<h1>
python에서 외부 파일을 사용하고 있을 때 주의점
</h1>

### 문제
보통 메인 py 파일과 다른 폴더를 만들어 그 안에 다른 py 파일이라든지, 세이브 파일 등을 집어넣게 될 것이다.
```
mainScript.py
  └resources
    └subScript.py
    └saveFile.txt
```

위와 같은 구조로 py 스크립트를 잘 만들고 나서, pyinstaller를 이용해서 exe 파일로 뽑아내고
( 사용한 명령어 : ```pyinstaller -F mainScript.py``` )
나니 세이브 파일이 없다는 오류가 나왔다.

### 해결
여러가지 조사한 결과, 만들어 낸 실행 파일 뿐 아니라 resources 폴더와 그 안의 saveFile.txt 파일도 필요하다는 것을 알게 되었다.
단순히 놓아두는 것 만으로 잘 돌아가게 되었다.

### 추가 정보
상대 경로보다는 절대 경로가 안전하긴 하다. 그러나 만약 코드 안에 박혀있게 되면 유연한 대응이 불가능하게 된다.
알아보는 과정에서, 파일을 실행하는 위치를 동적으로 받아올 수 있는 코드가 있었다.
```os.path.abspath(path)```
지금 구조라면 resources 폴더의 절대경로를 얻으려면 단순히
```os.path.abspath("resources")``` 라고 하면 된다.

### 추가 정보 2
경로 중 디렉토리 명만 얻는 방법이 있는데,
```os.path.dir(path)```
주의할 점으로는 마지막에 ```/```가 있는지에 따라 마지막 부분까지 삭제해버리거나, 남겨두거나 한다는 점이다.
따라서 해당 path가 파일인지 아닌지를 먼저 확인
```os.path.isfile(path)```
해주고 path를 조정할지 어떻게 할지를 고려해야할 것이다.
