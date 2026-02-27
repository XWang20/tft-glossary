**[English](README.md)** | **[中文](#tft-s16-多语言术语表)**

# TFT S16 多语言术语表

给 [沉浸式翻译](https://immersivetranslate.com/) 浏览器插件用的云顶之弈 S16 术语表。看英文/日文 TFT 攻略时，自动翻译棋子名、羁绊、装备、强化符文。

## 使用方法

### 1. 装插件
安装 [沉浸式翻译](https://immersivetranslate.com/)（Chrome / Firefox / Edge / Safari 都有）

### 2. 导入术语表
1. 打开插件设置 → 术语表
2. 选「从 URL 导入」
3. 粘贴：
```
https://raw.githubusercontent.com/XWang20/tft-glossary/main/meta/tft.json
```
4. 搞定

### 3. 开始用
打开任何 TFT 英文网页（tactics.tools、lolchess.gg 等），插件会自动翻译术语。看日文攻略也能用。

## 内容

| 类别 | 数量 | 举例 |
|------|------|------|
| 棋子 | 105 | Aatrox → 亚托克斯 |
| 羁绊 | 53 | Slayer → 杀戮者 |
| 强化符文 | 177 | Placebo → 安慰剂 |
| 装备 | 150 | Deathcap → 灭世者的帽子 |
| **合计** | **485** | |

## 三语源

每个目标语言文件同时包含英文、中文、日文三种源语言的映射：

- 看英文页面 → 翻译成你的语言
- 看中文页面 → 翻译成你的语言
- 看日文页面 → 翻译成你的语言

### 支持 23 种目标语言

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
    ├── tft_zh-CN.csv          # → 简体中文（966 条）
    ├── tft_ja.csv             # → 日文（966 条）
    ├── tft_ko.csv             # → 韩文（1447 条）
    └── ...（共 23 个文件）
```

CSV 格式：`source,target,tgt_lng`

## 数据来源

所有翻译来自 [CommunityDragon](https://raw.communitydragon.org/pbe/) PBE 数据，即 Riot 官方游戏内翻译。

## 许可

MIT
