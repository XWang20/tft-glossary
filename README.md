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
| **Total per CSV** | **~48,000** | 23 languages × bidirectional |

## Full Cross-Language Support

Every CSV accepts source text in **all 23 supported languages**. No matter which CSV you import:

- English → your language ✅
- Korean → your language ✅
- Chinese → your language ✅
- French → your language ✅
- Any of 23 languages → your language ✅

### 23 Supported Languages

| Code | Language | Code | Language |
|------|----------|------|----------|
| ar | العربية | ko | 한국어 |
| cs | Čeština | pl | Polski |
| de | Deutsch | pt-BR | Português (BR) |
| el | Ελληνικά | ro | Română |
| es-AR | Español (AR) | ru | Русский |
| es-ES | Español (ES) | th | ไทย |
| es-MX | Español (MX) | tr | Türkçe |
| fr | Français | vi | Tiếng Việt |
| hu | Magyar | zh-CN | 简体中文 |
| id | Bahasa Indonesia | zh-MY | 中文 (马来) |
| it | Italiano | zh-TW | 繁體中文 |
| ja | 日本語 | | |

## File Structure

```
├── meta/tft.json              # Metadata
└── glossaries/
    ├── tft_zh-CN.csv          # → Simplified Chinese (~48,000 rows)
    ├── tft_ja.csv             # → Japanese (~48,000 rows)
    ├── tft_ko.csv             # → Korean (~47,000 rows)
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
