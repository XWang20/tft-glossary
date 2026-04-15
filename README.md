**[English](#tft-set-16-multilingual-glossary)** | **[中文](README_ZH.md)**

# TFT Set 16 Multilingual Glossary

A glossary for the [Immersive Translate](https://immersivetranslate.com/) browser extension. Automatically translates TFT champion names, traits, augments, items, and community slang while browsing.

## Quick Start

### 1. Install Extension
Get [Immersive Translate](https://immersivetranslate.com/) for Chrome / Firefox / Edge / Safari.

⚠️ **Important:** Use an AI translation engine (e.g. SiliconFlow, GLM-4 Flash — both free). Google/Microsoft Translate do **not** support glossary term replacement.

### 2. Import Glossary
1. Open extension settings → Glossary
2. Import CSV — download your language file from the table below
3. Done

**Chinese users:**
```
https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_zh-CN.csv
```

### 3. Use It
Browse any TFT website (tactics.tools, lolchess.gg, op.gg/tft, YouTube subtitles, etc.) and the extension will automatically translate matched terms.

Works with **any of 23 languages as source** — English, Chinese, Korean, Japanese, French, German, and more.

## Coverage

| Category | Count | Example |
|----------|-------|---------|
| Champions | 115 | Aatrox → 亚托克斯 / 아트록스 / アトロックス |
| Traits | 53 | Slayer → 杀戮者 / 학살자 / スレイヤー |
| Augments | 1,200+ | Placebo → 安慰剂, Celestial Blessing → 星界祝福 |
| Items | 150+ | Deathcap → 灭世者的帽子 |
| Abbreviations | 70+ | IE → Infinity Edge, ASol → Aurelion Sol, bilge → Bilgewater |
| Community slang | 200+ | slam → 合装备, highroll → 运气好, BIS → 神装 |
| Chinese slang | 130+ | 偷偷 → TG, 青龙刀 → Shojin, 半空城 → open fort |
| **Total per CSV** | **~45,000** | 23 languages × bidirectional |

## Full Cross-Language Support

Every CSV accepts source text in **all 23 supported languages**. No matter which CSV you import:

- English → your language ✅
- Korean → your language ✅
- Chinese → your language ✅
- French → your language ✅
- Any of 23 languages → your language ✅

### 23 Supported Languages

| Code | Language | Download |
|------|----------|----------|
| ar | العربية | [tft_ar.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_ar.csv) |
| cs | Čeština | [tft_cs.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_cs.csv) |
| de | Deutsch | [tft_de.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_de.csv) |
| el | Ελληνικά | [tft_el.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_el.csv) |
| es-AR | Español (AR) | [tft_es-AR.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_es-AR.csv) |
| es-ES | Español (ES) | [tft_es-ES.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_es-ES.csv) |
| es-MX | Español (MX) | [tft_es-MX.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_es-MX.csv) |
| fr | Français | [tft_fr.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_fr.csv) |
| hu | Magyar | [tft_hu.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_hu.csv) |
| id | Bahasa Indonesia | [tft_id.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_id.csv) |
| it | Italiano | [tft_it.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_it.csv) |
| ja | 日本語 | [tft_ja.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_ja.csv) |
| ko | 한국어 | [tft_ko.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_ko.csv) |
| pl | Polski | [tft_pl.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_pl.csv) |
| pt-BR | Português (BR) | [tft_pt-BR.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_pt-BR.csv) |
| ro | Română | [tft_ro.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_ro.csv) |
| ru | Русский | [tft_ru.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_ru.csv) |
| th | ไทย | [tft_th.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_th.csv) |
| tr | Türkçe | [tft_tr.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_tr.csv) |
| vi | Tiếng Việt | [tft_vi.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_vi.csv) |
| zh-CN | 简体中文 | [tft_zh-CN.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_zh-CN.csv) |
| zh-MY | 中文 (马来) | [tft_zh-MY.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_zh-MY.csv) |
| zh-TW | 繁體中文 | [tft_zh-TW.csv](https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_zh-TW.csv) |

## File Structure

```
├── meta/tft.json              # Metadata
└── glossaries/
    ├── tft_zh-CN.csv          # → Simplified Chinese (~45,000 rows)
    ├── tft_ja.csv             # → Japanese (~45,000 rows)
    ├── tft_ko.csv             # → Korean (~45,000 rows)
    └── ... (23 files total)
```

CSV format: `source,target,tgt_lng`

## Data Sources

- **Official translations:** [CommunityDragon](https://raw.communitydragon.org/pbe/) PBE data (Riot's in-game translations for all 29 locales)
- **Community slang & abbreviations:** Sourced from YouTube/Bilibili TFT streamers (Subzeroark, Broseph, leduck, 手刃猫咪, 云顶CPU, 云顶小温柔, etc.)
- **Human-reviewed:** Verified by TFT community players

Built and maintained by an AI agent trained by [@XWang20](https://github.com/XWang20).

## License

MIT
