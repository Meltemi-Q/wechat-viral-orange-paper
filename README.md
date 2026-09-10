# 🍊 公众号爆文 AI 工业化生产橙皮书
### The Orange Paper of WeChat Viral Content Engineering: From WorkBuddy Expert System to 10w+ Pipeline

<div align="center">

<p align="center">
  <img src="cover.png" alt="公众号爆文AI工业化生产橙皮书封面" width="480" style="border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />
</p>

[![PDF Release](https://img.shields.io/badge/PDF%20电子书-下载精装完整版(1MB)-orange?style=for-the-badge&logo=adobeacrobatreader)](wechat-viral-orange-paper.pdf)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Meltemi-Q/wechat-viral-orange-paper?style=for-the-badge&logo=github)](https://github.com/Meltemi-Q/wechat-viral-orange-paper)

</div>

> **这是一套立足于第一性原理、彻底剔除假大空 AI 味，深度解构微信公众号 10w+ 爆文底层逻辑的实战技术手册、电子书与工业级工具库。**  
> 逆向解构自 WorkBuddy 官方核心专家矩阵（`wechat-official-account-expert`、`viral-topic-master` 等），结合真实商业号 548 篇沉淀数据与第一手踩坑经验编撰而成。
>
> 📖 **PDF 精装全彩版**：[`wechat-viral-orange-paper.pdf`](wechat-viral-orange-paper.pdf)（内置高保真封面、出版级中文字体排版，适合 iPad、Kindle 及打印精读）。

---

## 📑 橙皮书核心导读 (The Orange Paper)

你可以直接阅读 **[📄 docs/orange-paper.md (彻底去 AI 味·单文件精编完整版)](docs/orange-paper.md)** 或下载 **[📕 PDF 精装版](wechat-viral-orange-paper.pdf)**，亦可分章节深入研读：

- **[卷一：底层哲学与破局点 —— 为什么 AI 直出必死？](docs/01-architecture-philosophy.md)**  
  平台算法消重机制解析、“AI 搭骨架，真人填血肉”的工业化分工范式。
- **[卷二：选题工程 —— 10w+ 爆款选题炼金炉 (Viral Topic Forge)](docs/02-viral-topic-forge.md)**  
  爆款四基因（情绪/信息差/身份/行动）、12 心法预筛红线、8 维量化打分卡（≥30分立项）。
- **[卷三：标题工程学 —— 8 选 1 严选机制与 12 大爆款公式](docs/03-title-engineering.md)**  
  公域分发标签前置、四类标题覆盖、严禁冒号破折号引号等四大硬性拦截规则。
- **[卷四：文风 DNA 建模 —— 告别千篇一律的机器腔](docs/04-style-dna-profiler.md)**  
  14 维文风画像模型、标点与段落配方（1~3句/段）、口语断句与真人灵魂注入。
- **[卷五：去 AI 味与反蒸馏工程 (Anti-Distill & Humanizer)](docs/05-anti-distill-humanizer.md)**  
  38 类 AI 典型套路词清洗黑名单、真情实感瑕疵注入技巧、Python 自动化打分自检。
- **[卷六：工具链与 CLI 实践 —— 微信爆文全自动工程化](docs/06-tools-and-automation.md)**  
  搜狗微信文章检索爬虫、文风提取器、高点击封面视觉规范、微信官方草稿箱 API 闭环。

---

## 🛠️ 仓库资产概览 (Repository Assets)

```
wechat-viral-orange-paper/
├── docs/                               # 🍊 橙皮书核心理论与实操全集
│   ├── orange-paper.md                 # 单文件完整版（适合长文通读/打印）
│   ├── 01-architecture-philosophy.md   # 卷一：底层哲学与破局点
│   ├── 02-viral-topic-forge.md         # 卷二：选题工程
│   ├── 03-title-engineering.md         # 卷三：标题工程学
│   ├── 04-style-dna-profiler.md        # 卷四：文风 DNA 建模
│   ├── 05-anti-distill-humanizer.md    # 卷五：去 AI 味与反蒸馏
│   └── 06-tools-and-automation.md      # 卷六：工具链与自动化
├── skills/                             # 🧩 官方专家与技能包核心源码
│   ├── wechat-official-account-expert/ # 微信公众号运营专家完整体系 (8大核心Skill)
│   ├── viral-topic-master/             # 爆款选题策划专家与炼金炉
│   └── daily-post-controller/          # 商业号日更总控模板 (带真事库与质检)
├── scripts/                            # 💻 开箱即用的命令行 CLI 工具链
│   ├── search_wechat.js                # 微信公众号文章真实抓取爬虫 (Node.js)
│   ├── build_style_profile.py          # 14 维文风 DNA 量化提取器 (Python)
│   └── check_ai_taste.py               # AI 味道与套路词硬性质检脚本 (Python)
└── templates/                          # 📝 结构化模版与打分卡
    ├── title-rubric.md                 # 标题 8 选 1 评审卡
    ├── scoring-card.md                 # 选题 8 维打分卡
    ├── title-formulas.md               # 标题 12 大公式清单
    └── style-14d-framework.md          # 14 维风格画像框架定义
```

---

## 🚀 快速开始与实操指引

### 1. 抓取全网对标文章 (Node.js)
```bash
cd scripts
# 安装依赖
npm install cheerio

# 搜索特定赛道近期爆款文章（带结构化 JSON 输出）
node search_wechat.js "天道 存钱" -n 10
```

### 2. 提取你的专属文风 DNA (Python)
```bash
# 从你过去的 3~5 篇原创好文章中提炼量化风格
python scripts/build_style_profile.py --input-dir ../your_past_articles/
```

### 3. 发布前硬性去 AI 味检测 (Python)
```bash
# 检查拟发布的 Markdown 初稿，AI味指数超过 2.5 自动拦截
python scripts/check_ai_taste.py "path/to/your_draft.md"
```

---

## ⚖️ 开源协议与声明

本项目基于 [Apache License 2.0](LICENSE) 开源。  
所有代码与方法论仅供内容创作者学习、研究、探索 AI 辅助正向创作之用，请自觉遵守各大内容平台创作者守则与相关法律法规。
