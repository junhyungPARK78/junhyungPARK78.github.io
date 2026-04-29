---
layout:     post
comments:   true
title:      "휴대용 스캐너를 들였다"
date:       2026-04-29 +0900
author:     PJH
# categories: [Dummy]
tags:       [스캐너, Epson, 장비, 구매]
---

Claude를 쓰면서 위키를 운용하다 보니 종이 문서를 디지털화할 일이 부쩍 늘었다.
영수증, 설명서, 손으로 적은 메모까지—스캔해서 집어넣으면 나중에 찾기 편하니까.

처음에는 핸드폰 카메라로 찍어서 쓰고 있었는데, 문제가 생겼다.
종이가 조금이라도 구겨져 있거나 조명이 애매하면 OCR 인식률이 뚝 떨어지는 것이다.
핀이 안 맞거나 그림자가 지는 것도 심심찮게 발생했다.

전용기를 들일 때가 됐다고 판단했다.

![핸드폰으로 서류 촬영](/assets/images/2026-04-29-portable-scanner-epson-es50/001.jpg){: width="300px"}

---

## 조건 정리

집에 공간이 별로 없다. 복합기 같은 덩치 큰 건 처음부터 제외였다.
휴대 가능한 시트피드 방식의 슬림 스캐너로 검색 범위를 좁혔다.

맥 연결이 필수라 **Apple Silicon(M1 Max) + macOS Tahoe** 환경에서의 호환성도 체크가 필요했다.
드라이버 미지원으로 아예 쓸 수 없는 모델이 있으면 제아무리 스펙이 좋아도 의미가 없다.

---

## 후보 3종 비교

최종 후보로 세 모델이 남았다.

**Canon imageFORMULA R10**은 ADF(자동 문서 공급) 20장에 양면 스캔까지 지원하는 매력적인 모델이었다.
그런데 M1용 공식 드라이버가 없다. Sequoia도 미지원인 상황인데 Tahoe에서 돌아갈 리 없으니 일찌감치 탈락.

![Canon imageFORMULA R10](/assets/images/2026-04-29-portable-scanner-epson-es50/003.jpg){: width="300px"}

![Epson ES-60WB](/assets/images/2026-04-29-portable-scanner-epson-es50/002.png){: width="300px"}

**Epson ES-60WB**는 Wi-Fi와 내장 배터리(약 300장/충전)까지 달린 고급 모델이다.
생각해보면 둘 다 딱히 필요하지 않다. 책상 위에서 쓸 건데 USB 연결이면 충분하고, 그 차액으로 다른 걸 사는 게 낫다.

| 항목 | Epson ES-50 | Epson ES-60WB | Canon R10 |
|---|---|---|---|
| 스캔 속도 | 10 ppm | 15 ppm | 12 ppm (흑백) |
| ADF | ❌ 낱장 | ❌ 낱장 | ✅ 20장 |
| 양면 스캔 | ❌ | ❌ | ✅ |
| Wi-Fi | ❌ | ✅ | ❌ |
| 배터리 | ❌ | ✅ (약 300장) | ❌ |
| 무게 | 약 270g | 약 270g대 | 약 900g |
| M1 호환 | ⚠️ 조건부 | ⚠️ 조건부 | ❌ |
| 일본 가격 | ¥10,000~13,000 | 약 ¥21,674 | ¥17,000~20,000 |

---

## 결론: Epson ES-50

군더더기 없이 스캔 기능에만 집중한 모델. 가격도 세 개 중 가장 저렴하다.
무게 270g이면 가방에 넣고 다녀도 부담이 없다.

![Epson ES-50](/assets/images/2026-04-29-portable-scanner-epson-es50/004.png){: width="300px"}

한 가지 주의할 점이 있었다.
MacBook Pro 14"는 USB-C 포트만 있는데, ES-50에 기본 동봉된 케이블이 **Micro-USB → USB-A**다.
그러니까 맥에 직접 꽂을 수가 없다. **Micro-USB → USB-C 케이블**을 따로 준비해야 한다.

![Micro-USB to USB-C 케이블](/assets/images/2026-04-29-portable-scanner-epson-es50/005.png){: width="300px"}

---

앞으로 잘 써먹어봐야지.
