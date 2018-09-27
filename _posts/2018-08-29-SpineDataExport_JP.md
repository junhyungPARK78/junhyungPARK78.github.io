---
layout: post
comments: true
title: "spineのexportの設定"
date:   2018-09-27 23:19:00 +0900
author: PJH
categories: "Spine"
tags: "spine export setting 設定 설정"
---

<h1>
spineのデータをexportする方法
</h1>

spine作業の後、実際のゲームで使うためにはexportをする必要がある。
だがチーム作業中誰かがexportのオプションを間違えて意図していない不具合がでる経験をたくさんした。
それを防ぐために「だれが」作業しても同じオプションでexportできるようにしなきゃならない。
その方法で「オプションの内容をファイル化してspine作業者が共有する」のがあると思うが、その間に苦労した記憶があったのでここで共有しようかと思う。

1. exportのオプションは２つがある。
   1. イメージをatlas化する際に必要なオプション
![イメージをatlas化する際に必要なオプション](/assets/post_img/2018-08-29-1624/texturepacker.png)
ここからsaveするjsonファイル
   2. spineファイルをexportする際に必要なオプション
![spineファイルをexportする際に必要なオプション](/assets/post_img/2018-08-29-1624/export.png)
ここからsaveするjsonファイル
1. この中で作業者が共有するオプションは「spineファイルをexportする際に必要なオプション」の方。

もちろんこのオプションをロードするときにも合うポップアップからロードする必要がある。
ここもチェックしよう。

だが、exportするたびにオプションのjsonファイルをロードするのもヒューマンエラーの可能性がすごく高い。
その点で今後「drag & dropだけで自動的にexportする方法」に関してまた書こうかなと思う。

{% include include_spine_list_JP.html %}
