---
layout: post
comments: true
title:  "spineのexportを自動的にする"
date:   2018-10-12 18:23:00 +0900
author: PJH
categories: "Spine"
tags: "Spine"
cover:
---

<h1>
spineのexportを自動的にする
</h1>

Mac用の自動exportアップを作る方法の説明

### まず必要なもの

1. [以前のポスト]({{ site.baseurl }}{% link _posts/2018-09-27-SpineDataExport_JP.md %})で作った「spineファイルをexportする際に必要なオプション」のjsonファイル
1. spineファイルをexportしたファイルを保存するフォルダー

### 作り方

- Automatorを実行
- 「アプリケーション」を選択
- 「シェルスクリプトを実行」をワークフローに入れる
- シェルは「/bin/bash」を選択
- 入力の引き渡し方法は「引数として」を選択
- 以下の内容をテキストエディタで編集

```
for f in "$@"
do
echo $f;

/Applications/Spine/Spine.app/Contents/MacOS/Spine --input $f --output "./export_folder" --export "./spine_export_option.json" ;

done
```

    「./export_folder」を自分のpathに修正
    「./spine_export_option.json」を自分のpathに修正
    
- 修正した内容をコピーしてシェルスクリプトにペーストする
- saveする。
- spineファイルをsaveしたアップにdrag & dropする
- 指定したexportのフォルダーに書き出されたかを確認

{% include_relative includes/spine/include_spine_list_JP.md %}
