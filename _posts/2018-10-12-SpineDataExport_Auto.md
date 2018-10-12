---
layout: post
comments: true
title:  "spine의 export를 자동화시키자"
date:   2018-10-12 18:23:00 +0900
author: PJH
categories: "Spine"
tags: "Spine"
cover:
---

<h1>
spine의 export를 자동화시키자
</h1>

Mac용의 자동 export 툴을 만드는 방법을 기재해두고자 한다.

### 우선 필요한 것

1. [이전의 포스트]({{ site.baseurl }}{% link _posts/2018-08-29-SpineDataExport.md %})에서 만든 「해당 spine 파일을 export 하는데 필요한 옵션」의 json 파일
1. spine 파일을 export한 결과물을 보존할 폴더

### 만드는 방법

- Automator를 실행한다.
- 「어플리케이션」을 선택한다.
- 「셸 스크립트를 실행」을 워크 플로우에 넣는다.
- 셸은 「/bin/bash」를 선택한다.
- 입력 방법에 대해서는 「인수로써」를 선택
- 이하의 내용을 텍스트 에디터로 편집한다.

```
for f in "$@"
do
echo $f;

/Applications/Spine/Spine.app/Contents/MacOS/Spine --input $f --output "./export_folder" --export "./spine_export_option.json" ;

done
```

    「./export_folder」를 자신에게 맞는 path로 수정한다.
    「./spine_export_option.json」을 자신에게 맞는 path로 수정한다.

- 수정한 내용을 셸 스크립트에 붙여넣는다.
- save한다.
- spine 파일을 세이브해서 생긴 툴에 drag & drop한다.
- 지정한 export 폴더에 제대로 파일 들이 저장되는지 확인한다.


잘되면 성공이다. 이것으로 쓸데없는 휴먼 에러를 줄일 수 있다.

{% include_relative includes/spine/include_spine_list.md %}
