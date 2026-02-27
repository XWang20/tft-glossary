**[English](README.md)** | **[中文](#tft-s16-多语言术语表)**

# TFT S16 多语言术语表

给 [沉浸式翻译](https://immersivetranslate.com/) 浏览器插件用的云顶之弈 S16 术语表。看外服 TFT 攻略时，自动翻译棋子名、羁绊、装备、海克斯和社区俚语。

## 使用方法

### 1. 装插件
安装 [沉浸式翻译](https://immersivetranslate.com/)（Chrome / Firefox / Edge / Safari 都有）

⚠️ **重要：** 翻译引擎必须选 AI 翻译（比如硅基流动、GLM-4 Flash，都免费）。Google/微软翻译**不支持**术语替换。

### 2. 导入术语表
1. 打开插件设置 → 术语表
2. 导入 CSV，下载对应语言文件

**中文用户：**
```
https://raw.githubusercontent.com/XWang20/tft-glossary/main/glossaries/tft_zh-CN.csv
```

### 3. 开始用
打开任何 TFT 网页（tactics.tools、lolchess.gg、op.gg/tft、YouTube 字幕等），插件会自动翻译术语。

支持 **23 种语言互译** — 英文、韩文、日文、法文、德文……任何语言的页面都能翻。

## 覆盖内容

| 类别 | 数量 | 举例 |
|------|------|------|
| 棋子 | 115 | Aatrox → 亚托克斯 |
| 羁绊 | 53 | Slayer → 杀戮者 |
| 海克斯 | 1,200+ | Placebo → 安慰剂, Celestial Blessing → 星界祝福 |
| 装备 | 150+ | Deathcap → 灭世者的帽子 |
| 英文缩写 | 70+ | IE → 无尽之刃, ASol → 奥瑞利安·索尔, bilge → 比尔吉沃特 |
| 英文俚语 | 200+ | slam → 合装备, highroll → 运气好, BIS → 神装 |
| 中文俚语 | 130+ | 偷偷 → TG, 青龙刀 → Shojin, 半空城 → open fort |
| **每个 CSV 总计** | **~48,000 条** | 23 种语言双向互译 |

## 全语言互译

每个 CSV 都包含 **23 种语言** 作为源语言。不管你下载哪个语言的文件：

- 英→你的语言 ✅
- 韩→你的语言 ✅
- 中→你的语言 ✅
- 法→你的语言 ✅
- 任意 23 种语言→你的语言 ✅

### 支持 23 种语言

| 代码 | 语言 | 代码 | 语言 |
|------|------|------|------|
| ar | 阿拉伯语 | ko | 韩语 |
| cs | 捷克语 | pl | 波兰语 |
| de | 德语 | pt-BR | 葡萄牙语（巴西） |
| el | 希腊语 | ro | 罗马尼亚语 |
| es-AR | 西班牙语（阿根廷） | ru | 俄语 |
| es-ES | 西班牙语（西班牙） | th | 泰语 |
| es-MX | 西班牙语（墨西哥） | tr | 土耳其语 |
| fr | 法语 | vi | 越南语 |
| hu | 匈牙利语 | zh-CN | 简体中文 |
| id | 印尼语 | zh-MY | 中文（马来） |
| it | 意大利语 | zh-TW | 繁體中文 |
| ja | 日语 | | |

## 文件结构

```
├── meta/tft.json              # 元数据
└── glossaries/
    ├── tft_zh-CN.csv          # → 简体中文（~48,000 条）
    ├── tft_ja.csv             # → 日文（~48,000 条）
    ├── tft_ko.csv             # → 韩文（~47,000 条）
    └── ...（共 23 个文件）
```

CSV 格式：`source,target,tgt_lng`

## 数据来源

- **官方翻译：** [CommunityDragon](https://raw.communitydragon.org/pbe/) PBE 数据（Riot 官方游戏内 29 个语言区的翻译）
- **社区俚语和缩写：** 来自 YouTube/B站 TFT 主播（Subzeroark、Broseph、leduck、手刃猫咪、云顶CPU、云顶小温柔等）
- **人工校对：** TFT 社区玩家验证

由 [@XWang20](https://github.com/XWang20) 训练的 AI agent 构建和维护。

## 许可

MIT
