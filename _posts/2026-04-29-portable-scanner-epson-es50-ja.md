---
layout:     post
comments:   true
title:      "ポータブルスキャナーを導入した"
date:       2026-04-29 +0900
author:     PJH
# categories: [Dummy]
tags:       [スキャナー, Epson, ガジェット, 購入]
---

Claudeを使いながらwikiを運用していたら、紙の書類をデジタル化する機会がぐっと増えた。
レシート、説明書、手書きのメモまで——スキャンして放り込んでおけば、後で探しやすい。

最初はスマホのカメラで撮って済ませていたが、問題が出てきた。
紙が少しでも折れていたり、照明が中途半端だとOCRの認識率がガクッと落ちるのだ。
ピントが合わなかったり影が入ったりするのも、それなりに発生した。

専用機を入れる頃合いだと判断した。

![スマホで書類を撮影](/assets/images/2026-04-29-portable-scanner-epson-es50/001.jpg){: width="300px"}

---

## 条件の整理

部屋にスペースがない。複合機みたいな大きいものは最初から除外だ。
携帯できるシートフィード型のスリムスキャナーに絞って探した。

Mac接続が必須なので、**Apple Silicon(M1 Max) + macOS Tahoe** 環境での互換性チェックも必要だった。
ドライバ非対応で動かないモデルがあれば、スペックがよくても意味がない。

---

## 候補3機種の比較

最終候補は3機種に絞られた。

**Canon imageFORMULA R10**はADF(自動送り)20枚・両面スキャン対応で魅力的なモデルだった。
ただ、M1向けの公式ドライバがない。Sequoiaも非対応の状況でTahoeで動くはずもなく、早々に脱落。

![Canon imageFORMULA R10](/assets/images/2026-04-29-portable-scanner-epson-es50/003.jpg){: width="300px"}

![Epson ES-60WB](/assets/images/2026-04-29-portable-scanner-epson-es50/002.png){: width="300px"}

**Epson ES-60WB**はWi-Fiと内蔵バッテリー(約300枚/充電)まで付いた上位モデルだ。
よく考えたら、どちらも特に必要ない。デスクで使うならUSB接続で十分だし、その差額で他のものを買った方がいい。

| 項目 | Epson ES-50 | Epson ES-60WB | Canon R10 |
|---|---|---|---|
| スキャン速度 | 10 ppm | 15 ppm | 12 ppm（モノクロ） |
| ADF | ❌ 1枚ずつ | ❌ 1枚ずつ | ✅ 20枚 |
| 両面スキャン | ❌ | ❌ | ✅ |
| Wi-Fi | ❌ | ✅ | ❌ |
| バッテリー | ❌ | ✅（約300枚） | ❌ |
| 重量 | 約270g | 約270g台 | 約900g |
| M1互換 | ⚠️ 条件付き | ⚠️ 条件付き | ❌ |
| 日本価格 | ¥10,000〜13,000 | 約¥21,674 | ¥17,000〜20,000 |

---

## 結論：Epson ES-50

余計なものを省いてスキャン機能に特化したモデル。価格も3つの中で一番安い。
270gならカバンに入れて持ち歩いても負担にならない。

![Epson ES-50](/assets/images/2026-04-29-portable-scanner-epson-es50/004.png){: width="300px"}

ひとつだけ注意点があった。
MacBook Pro 14"はUSB-Cポートしかないが、ES-50に付属しているケーブルは**Micro-USB → USB-A**だ。
つまりMacに直接挿せない。**Micro-USB → USB-Cケーブル**を別途用意する必要がある。

![Micro-USB to USB-Cケーブル](/assets/images/2026-04-29-portable-scanner-epson-es50/005.png){: width="300px"}

---

これからうまく活用してみよう。
