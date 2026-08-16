#!/usr/bin/env python3
"""
Obsidian General_wiki 의 게임 공략 노트를 jidae.com 고정 페이지(Jekyll)로 변환한다.

사용:
    python3 tools/wiki2page.py

하는 일:
  1. 위키 md 를 읽어 Jekyll front matter 를 붙인다
  2. Obsidian 임베드 `![[sources/.../도식/NAME.svg]]` → `![](/assets/images/games/<slug>/NAME.svg)`
     바로 다음 줄의 이탤릭 캡션은 그림 아래 설명으로 유지
  3. Obsidian 위키링크 `[[wiki/...|표시명]]` → 표시명 (사이트에는 대상 페이지가 없으므로 평문화)
  4. 로컬 sources/ 경로 언급은 공개용 문구로 치환
  5. 목차(kramdown TOC) 삽입

주의: 원본은 위키다. 이 스크립트는 단방향 생성만 하며 위키를 수정하지 않는다.
"""
import re
import sys
from pathlib import Path

WIKI = Path("/Volumes/NAS_PJH_Shared_Folder/200_PERSONAL/OBSIDIAN/General_wiki")
REPO = Path(__file__).resolve().parent.parent

# 위키의 도해 파일명(한국어)을 사이트용 영문 파일명으로 매핑한다.
# 레포 규칙: 파일명은 반드시 영어 (NAS 환경 인코딩 문제 회피)
ASSET_NAMES = {
    "01_성배일기-창힌트-판독법.svg": "01_grail-diary-window-hint.svg",
    "02_SCUMM-인터페이스.svg": "02_scumm-interface.svg",
    "03_카타콤-연결그래프.svg": "03_catacombs-graph.svg",
    "04_비문-성배판정표.svg": "04_inscription-grail-table.svg",
    "05_석상퍼즐-연동규칙.svg": "05_statue-puzzle-rules.svg",
    "06_해골오르간-악보변환.svg": "06_skull-organ-notes.svg",
    "07_그림보관실-금고접근.svg": "07_gallery-vault-access.svg",
    "08_성배그림-광채판정.svg": "08_grail-painting-glow.svg",
    "09_3층복도-문판별.svg": "09_third-floor-doors.svg",
    "10_의자탈출-카펫정렬.svg": "10_chair-escape-alignment.svg",
    "11_복엽기-조종석-시동8단계.svg": "11_biplane-cockpit-startup.svg",
    "12_2관문-글자타일-규칙.svg": "12_trial2-letter-tiles.svg",
    "13_3관문-보이지않는다리.svg": "13_trial3-invisible-bridge.svg",
    "14_성배의방-배치와절차.svg": "14_grail-chamber-layout.svg",
}

JOBS = [
    {
        "src": WIKI / "wiki/게임/titles/인디아나존스3-최후의성전.md",
        "out": REPO / "games/indiana-jones-3.md",
        "slug": "indiana-jones-3",
        "title": "인디아나 존스 3: 최후의 성전 — 공략",
        "permalink": "/games/indiana-jones-3/",
        "lead": (
            "1989년 LucasArts 그래픽 어드벤처 "
            "*Indiana Jones and the Last Crusade* 의 한국어 공략. "
            "그림은 전부 직접 그린 도해다."
        ),
    },
]


def convert(text: str, slug: str) -> str:
    # 1) 위키 전용 헤더 제거
    text = re.sub(r"^updated:.*\n", "", text)
    text = re.sub(r"^\[\[wiki/[^\]]+\]\]\s*\n", "", text, flags=re.M)

    # 2) 도식 임베드 → Jekyll 이미지 경로 (바로 다음 줄의 이탤릭 캡션을 alt 로 재사용)
    def img(m):
        name, caption = m.group(1), m.group(2)
        asset = ASSET_NAMES.get(name)
        if asset is None:
            raise SystemExit(f"[오류] 도해 파일명 매핑 없음: {name}  → ASSET_NAMES 에 추가할 것")
        alt = re.sub(r"[*`]", "", caption).strip()
        return f"![{alt}](/assets/images/games/{slug}/{asset})\n{caption}"

    text = re.sub(
        r"!\[\[[^\]]*?/도식/([^\]/]+\.svg)\]\]\n(\*[^\n]+\*)", img, text
    )

    # 3) 남은 위키링크 평문화
    text = re.sub(r"\[\[[^\]\|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # 4) 로컬 경로 언급을 공개용 문구로
    text = text.replace(
        "`sources/게임/game_인디아나존스3-최후의성전-공략_20260816/원본-국내공략_HWP2.0.hwp` 로 보존했고",
        "로컬 아카이브에 보존했고",
    )
    text = re.sub(
        r"^> \*\*그림 안내\*\*.*?\n(?:> .*\n)*",
        "> **그림 안내** — 이 페이지의 도해 14장은 전부 직접 그린 SVG다. 게임 화면을 옮겨 그린 것이 아니라 정보 구조만 재구성했다.\n"
        "> 2관문 타일 경로·석상 배치·비문 조합처럼 **플레이할 때마다 달라지는 것**은 남의 화면을 따라 하면 오히려 틀리므로, 규칙만 익히면 된다.\n",
        text,
        flags=re.M,
    )
    text = re.sub(
        r"^참고용 원본 193장은.*$",
        "참고용 원본 스크린샷은 개인 아카이브에만 두고 이 페이지에는 싣지 않는다.",
        text,
        flags=re.M,
    )
    text = re.sub(r"^출처: `sources/[^\n]*\n", "", text, flags=re.M)

    # 5) 남은 백틱 경로 정리
    text = text.replace("`도식/`", "직접 그린 도해").replace("`스샷/`", "개인 아카이브")
    text = text.replace(
        "이 과정에서 캡션 오류 1건 발견·수정 — `lastcrusade_183.jpg`는 \"벽감의 성배들\"이 아니라 "
        "**성배 동굴 진입 장면 + 성수 그릇**이다",
        "이 과정에서 캡션 오류 1건도 잡았다 — 성배의 방 스샷이라 알려진 화면은 실제로는 "
        "**성배 동굴 진입 장면 + 성수 그릇**이고 성배들은 찍혀 있지 않다",
    )

    # 6) 사이트에 없는 위키 내부 링크 모음은 통째로 제거
    text = re.sub(r"\n---\n\n## 관련 페이지\n(?:.*\n)*?(?=\n---|\Z)", "\n", text)

    # 7) 공개용 푸터
    text = text.rstrip().rstrip("-").rstrip() + (
        "\n\n---\n\n"
        "*본문은 위 「공략 사이트」의 자료를 종합해 한국어로 재구성한 것이고, "
        "도해 14장은 직접 그렸다. 원본 스크린샷은 게재하지 않는다.*\n"
    )

    return text.strip() + "\n"


def build(job) -> Path:
    src = Path(job["src"])
    body = convert(src.read_text(encoding="utf-8"), job["slug"])

    # 첫 H1 은 레이아웃이 title 로 출력하므로 제거
    body = re.sub(r"^#\s+[^\n]+\n+", "", body)

    fm = (
        "---\n"
        "layout: page\n"
        f'title: "{job["title"]}"\n'
        f'permalink: {job["permalink"]}\n'
        "noindex: true\n"
        "---\n\n"
        f'{job["lead"]}\n\n'
        "* TOC\n"
        "{:toc}\n\n"
    )
    out = Path(job["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fm + body, encoding="utf-8")
    return out


if __name__ == "__main__":
    for job in JOBS:
        p = build(job)
        n = len(p.read_text(encoding="utf-8").splitlines())
        print(f"생성: {p.relative_to(REPO)}  ({n}행)")
    sys.exit(0)
