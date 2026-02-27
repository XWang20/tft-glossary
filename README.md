# TFT S16 多语言术语表 / TFT Set 16 Multilingual Glossary

为 [immersive-translate](https://immersivetranslate.com/) 沉浸式翻译插件制作的云顶之弈 S16 术语表。

支持 **3 种源语言**（英文、中文、日文）→ **23 种目标语言** 的双向翻译。

## 使用方法

### 1. 安装沉浸式翻译插件
- Chrome: [Chrome 商店](https://chrome.google.com/webstore/detail/immersive-translate/bpoadfkcbjbfhfodiogcnhhhpibjhbnh)
- Firefox/Edge/Safari: 见 [官网](https://immersivetranslate.com/)

### 2. 导入术语表
1. 打开插件设置 → 术语表
2. 选择「从 URL 导入」
3. 粘贴:
```
https://raw.githubusercontent.com/XWang20/tft-glossary/main/meta/tft.json
```
4. 完成

### 3. 开始使用
浏览任何 TFT 相关网页（Riot 官网、tactics.tools、lolchess.gg 等），插件会自动翻译匹配的术语。

## 内容覆盖

| 类别 | 数量 | 示例 |
|------|------|------|
| 棋子 | 105 | Aatrox/亚托克斯, Mel/梅尔 |
| 羁绊 | 53 | Slayer/杀戮者, Yordle/约德尔人 |
| 强化符文 | 177 | Placebo/安慰剂 |
| 装备 | 150 | Deathcap/灭世者的帽子 |
| **总计** | **485** | |

## 源语言 × 目标语言

每个目标语言 CSV 同时包含 3 种源语言的映射:

- **英文 → 目标语言** (浏览英文网页时)
- **中文 → 目标语言** (浏览中文网页时)
- **日文 → 目标语言** (浏览日文网页时)

### 支持的目标语言 (23 种)

| 代码 | 语言 | 代码 | 语言 |
|------|------|------|------|
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

## 文件结构

```
├── meta/tft.json              # 元数据
└── glossaries/
    ├── tft_zh-CN.csv          # → 简体中文 (966 条)
    ├── tft_ja.csv             # → 日文 (966 条)
    ├── tft_ko.csv             # → 韩文 (1447 条)
    ├── tft_de.csv             # → 德文 (1446 条)
    └── ... (共 23 个文件)
```

CSV 格式: `source,target,tgt_lng`

```csv
Aatrox,亚托克斯,zh-CN
エイトロックス,亚托克斯,zh-CN
아트록스,亚托克斯,zh-CN
```

## 数据来源

术语数据抓取自 [CommunityDragon](https://raw.communitydragon.org/pbe/) PBE 数据，包含 S16 赛季全部官方翻译。

## 许可

MIT
