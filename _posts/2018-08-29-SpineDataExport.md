---
layout: post
comments: true
title: "spine의 export 설정"
date:   2018-08-29 16:24:00 +0900
author: PJH
categories: "Spine"
tags: "spine export setting 設定 설정"
---

<h1>
spine 데이터를 export하는 방법
</h1>

spine으로 작업한 후 실제 게임에서 사용하기 위해서는 export를 할 필요가 있다.
그런데 팀 작업 중 누군가가 export 옵션을 실수해서 unity에 넣었을 때 의도하지 않은 오류를 뿜어내는 경험을 많이 했다.
그것을 방지하기 위해서 '누가' 작업하더라도 동일한 옵션 내역으로 export 해 줄 수 있게 할 필요성이 있다.
해결 방법으로 '옵션을 파일화해서 spine 작업자끼리 공유한다'가 있을 수 있는데, 여기서 꽤 삽질을 했던 기억이 있어서 그 사항을 공유할까 한다.

1. export 옵션은 두가지 종류가 있다.
   1. 이미지를 아틀라스 화 하는데 필요한 옵션
![이미지를 아틀라스 화 하는데 필요한 옵션](/assets/post_img/2018-08-29-1624/texturepacker.png)
이곳에서 save 하는 json 파일
   2. 해당 spine 파일을 export 하는데 필요한 옵션
![해당 spine 파일을 export 하는데 필요한 옵션](/assets/post_img/2018-08-29-1624/export.png)
이곳에서 save 하는 json 파일
1. 이 중 공유해야하는 옵션은 「해당 spine 파일을 export 하는데 필요한 옵션」쪽이다.

물론 이 옵션을 불러들일 때도 해당하는 팝업창에서 불러들일 필요가 있다.
이 부분도 확실히 체크해두도록 하자.

사실 export 할 때마다 옵션 json 파일을 불러들이는 것도 꽤 큰 수고가 된다.
추후 'drag & drop 만으로 자동으로 export 해주는 방법'에 대해서 다시 한번 포스팅을 만들어볼까 생각한다.

{% include include_spine_list.html %}
