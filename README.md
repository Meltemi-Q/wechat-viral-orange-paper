# 🍊 微信公众号爆文创作 AI Skill 橙皮书
### The Orange Paper of WeChat Content Creation Skill: Open Source Agent Workflows & Engineering Manual

<div align="center">

<p align="center">
  <img src="cover.png" alt="微信公众号爆文创作 AI Skill 橙皮书封面" width="480" style="border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />
</p>

[![PDF Release](https://img.shields.io/badge/PDF%20电子书-下载精装完整版(1.2MB)-orange?style=for-the-badge&logo=adobeacrobatreader)](wechat-viral-orange-paper.pdf)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Meltemi-Q/wechat-viral-orange-paper?style=for-the-badge&logo=github)](https://github.com/Meltemi-Q/wechat-viral-orange-paper)

</div>

> **本手册是一套专注于 AI Agent 时代“微信公众号爆文创作”的标准化开源 Skill 规范与实战橙皮书。**  
> 拒绝假大空套话与 AI 直出垃圾，深度解构选题炼金炉、标题工程学、14 维文风画像、去 AI 味反蒸馏清洗，以及直通微信官方草稿箱的自动化流水线。

---

## 🌟 开源社区 WeChat 创作 Skill 生态对照

在开源社区中，针对微信公众号内容创作与排版发布的优质开源项目百花齐放，本橙皮书与业界主流实现全面对标：

| 开源项目 | 核心定位与特色 | 与本仓库 Skill 矩阵的协同 |
| :--- | :--- | :--- |
| **[jiji262/wechat-publisher](https://github.com/jiji262/wechat-publisher)** | 全能型发布工具：素材搜集、AI去痕、精美排版、草稿箱推送 | 对标本库全链路闭环，提供自动化管道参考 |
| **[xiaohuailabs/xiaohu-wechat-format](https://github.com/xiaohuailabs/xiaohu-wechat-format)** | 85+ 主题排版，Markdown 转微信内联样式，直通草稿箱 | 对标本库排版规范与样式适配 |
| **[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)** | 专为 Claude Code / AI Agent 打造的高颜值公众号排版 Skill | 对标本库 Agent Prompt 设计与交互协议 |
| **[imraywang/wewrite](https://github.com/imraywang/wewrite)** | 热点选题雷达与 AI 工业化流水线写作管道 | 对标本库选题炼金炉与大纲架构 |
| **[chouheiwa/wechat-studio](https://github.com/chouheiwa/wechat-studio)** | 纯粹架构：排版渲染与 Skill 解耦 | 对标本库模块化 CLI 脚本分离架构 |

---

## 📑 橙皮书核心导读 (The Orange Paper)

你可以直接阅读 **[📄 docs/orange-paper.md (单文件精编完整版)](docs/orange-paper.md)** 或下载 **[📕 PDF 精装版](wechat-viral-orange-paper.pdf)**：

- **[卷一：底层哲学与分工 —— 为什么 AI 直出必死？](docs/01-architecture-philosophy.md)**  
  平台算法消重机制解析、“AI 搭骨架，真人填血肉”的工业化分工范式。
- **[卷二：选题工程 —— 10w+ 爆款选题炼金炉 (Viral Topic Forge)](docs/02-viral-topic-forge.md)**  
  爆款四基因（情绪/信息差/身份/行动）、12 心法预筛红线、8 维量化打分卡（≥30分立项）。
- **[卷三：标题工程学 —— 8 选 1 严选机制与 12 大爆款公式](docs/03-title-engineering.md)**  
  公域分发标签前置、四类标题覆盖、严禁冒号破折号引号等四大硬性拦截规则。
- **[卷四：文风 DNA 建模 —— 告别千篇一律的机器腔](docs/04-style-dna-profiler.md)**  
  14 维文风画像模型、标点与段落配方（1~3句/段）、口语断句与真实感注入。
- **[卷五：去 AI 味与反蒸馏工程 (Anti-Distill & Humanizer)](docs/05-anti-distill-humanizer.md)**  
  38 类 AI 典型套路词清洗黑名单、真实细节注入技巧、Python 自动化打分自检。
- **[卷六：工具链与 CLI 实践 —— 微信爆文全自动工程化](docs/06-tools-and-automation.md)**  
  搜狗微信文章检索爬虫、文风提取器、高点击封面视觉规范、微信官方草稿箱 API 闭环。

---

## 🛠️ 仓库资产概览 (Repository Assets)

```
wechat-viral-orange-paper/
├── docs/                               # 🍊 橙皮书核心理论与实操全集
│   ├── orange-paper.md                 # 单文件完整版（纯净规范版）
│   ├── cover.html                      # 纯亮橙印刷级封面源文件
│   ├── orange-paper.html               # 出版级排版 HTML 模板
│   ├── 01-architecture-philosophy.md   # 卷一：底层哲学与分工
│   ├── 02-viral-topic-forge.md         # 卷二：选题工程
│   ├── 03-title-engineering.md         # 卷三：标题工程学
│   ├── 04-style-dna-profiler.md        # 卷四：文风 DNA 建模
│   ├── 05-anti-distill-humanizer.md    # 卷五：去 AI 味与反蒸馏
│   └── 06-tools-and-automation.md      # 卷六：工具链与自动化
├── skills/                             # 🧩 标准 Agent 技能包定义
│   ├── wechat-official-account-expert/ # 微信公众号写作 Skill 矩阵 (8 大核心子 Skill)
│   ├── viral-topic-master/             # 爆款选题打分过滤卡
│   └── daily-post-controller/          # 标准日更总控流程
├── scripts/                            # 💻 开箱即用的 CLI 命令行工具箱
│   ├── search_wechat.js                # 搜狗微信文章爬虫工具 (Node.js)
│   ├── build_style_profile.py          # 14 维文风 DNA 提取工具 (Python)
│   └── check_ai_taste.py               # 38 类 AI 味套路词质检脚本 (Python)
└── templates/                          # 📝 结构化模版与打分卡
    ├── title-rubric.md                 # 标题 8 选 1 评审卡
    ├── scoring-card.md                 # 选题 8 维打分卡
    ├── title-formulas.md               # 标题 12 大公式清单
    └── style-14d-framework.md          # 14 维风格画像框架定义
```

---

## 🚀 快速上手核心 Skill (CLI)

```bash
# 1. 安装文章检索依赖并搜索对标爆款
cd scripts
npm install cheerio
node search_wechat.js "副业 搞钱" -n 10

# 2. 提取原创文风 DNA
python build_style_profile.py --input-dir ../your_past_articles/

# 3. 发布前执行 AI 套路词清洗质检
python check_ai_taste.py "path/to/your_draft.md"
```

---

## ⚖️ 开源协议

本项目基于 [Apache License 2.0](LICENSE) 开源。
