---
layout:     post
comments:   true
title:      "spineのデータをexportする方法"
date:       2018-09-27 +0900
author:     PJH
# categories: [Dummy]
tags:       [spine, export]
---

spine作業の後、実際のゲームで使うためにはexportをする必要がある。
だがチーム作業中誰かがexportのオプションを間違えて意図していない不具合がでる経験をたくさんした。
それを防ぐために「だれが」作業しても同じオプションでexportできるようにしなきゃならない。
その方法で「オプションの内容をファイル化してspine作業者が共有する」のがあると思うが、その間に苦労した記憶があったのでここで共有しようかと思う。

1. exportのオプションは２つがある。
1. イメージをatlas化する際に必要なオプション
  [![](https://www.dropbox.com/s/symkj51r2p78afr/texturepacker.png?raw=1)](https://www.dropbox.com/s/symkj51r2p78afr/texturepacker.png?raw=1)

1. spineファイルをexportする際に必要なオプション
  [![](https://www.dropbox.com/s/kdsiwjibr6vtmt2/export.png?raw=1)](https://www.dropbox.com/s/kdsiwjibr6vtmt2/export.png?raw=1)

1. この中で作業者が共有するオプションは「spineファイルをexportする際に必要なオプション」の方。

もちろんこのオプションをロードするときにも合うポップアップからロードする必要がある。
ここもチェックしよう。

だが、exportするたびにオプションのjsonファイルをロードするのもヒューマンエラーの可能性がすごく高い。
その点で今後「drag & dropだけで自動的にexportする方法」に関してまた書こうかなと思う。

{% include_relative includes/spine/include_spine_list_JP.md %}
