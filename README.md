# TFT Set 16 Multilingual Glossary

A glossary for the [Immersive Translate](https://immersivetranslate.com/) browser extension. Automatically translates TFT champion names, traits, augments, and items while browsing.

## Quick Start

### 1. Install Extension
Get [Immersive Translate](https://immersivetranslate.com/) for Chrome / Firefox / Edge / Safari.

### 2. Import Glossary
1. Open extension settings → Glossary
2. Select "Import from URL"
3. Paste:
```
https://raw.githubusercontent.com/XWang20/tft-glossary/main/meta/tft.json
```
4. Done

### 3. Use It
Browse any TFT website (tactics.tools, lolchess.gg, leagueoflegends.com, etc.) and the extension will automatically translate matched terms.

Works with English, Chinese, and Japanese source pages.

## Coverage

| Category | Count | Example |
|----------|-------|---------|
| Champions | 105 | Aatrox → 亚托克斯 / 아트록스 / アトロックス |
| Traits | 53 | Slayer → 杀戮者 / 학살자 / スレイヤー |
| Augments | 177 | Placebo → 安慰剂 / 플라시보 / プラシーボ |
| Items | 150 | Deathcap → 灭世者的帽子 |
| **Total** | **485** | |

## Multi-Source Language Support

Each target language CSV includes mappings from **3 source languages**:

- **English → target** (browsing English pages)
- **Chinese → target** (browsing Chinese pages)
- **Japanese → target** (browsing Japanese pages)

### 23 Target Languages

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

## Data Source

All translations sourced from [CommunityDragon](https://raw.communitydragon.org/pbe/) PBE data (official Riot in-game translations).

## License

MIT
