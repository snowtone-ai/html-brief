# html-brief

![HTML5](https://img.shields.io/badge/HTML5-single_file-orange?logo=html5)
![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-yellow?logo=javascript)
![Claude Code](https://img.shields.io/badge/Claude_Code-skill-black?logo=anthropic)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> AIが生成した長い計画・分析・レビューを、ブラウザで読みやすい1ページのHTMLに変換するスキル

Status: 完成（保守のみ）

400行にわたるAIの出力をスキャンしやすい構造・図・インタラクティブなコントロールを含む単一HTMLファイルに整形します。Claude Code・Codex CLI・Gemini CLI・Cursorで利用でき、「Copy as Prompt」ボタンで決定内容を次のAIセッションにそのまま渡せます。

---

## 主な機能

- 実装計画・マイグレーション・RFCを視覚的なHTMLブリーフに変換できる
- 選択肢の比較・トレードオフ分析をカード形式と評価マトリクスで表示できる
- コードレビュー結果を重要度別に整理して表示できる
- インシデントレポートや調査結果をエグゼクティブサマリー付きで出力できる
- 「Copy as Prompt / JSON / Markdown」ボタンで決定内容をAIエージェントに返送できる

---

## 技術スタック

| カテゴリ | 技術 |
|---|---|
| フロントエンド | HTML, CSS, バニラJavaScript |
| AI対応 | Claude Code, Codex CLI, Gemini CLI, Cursor |

---

## 設計の工夫

- 出力ファイルはCSSとJavaScriptをすべてインラインに含む単一HTMLファイルで、ブラウザさえあればどこでも開ける設計
- スキル定義（`SKILL.md`）がエージェント非依存のMarkdown形式で書かれており、複数のAIツールから共通利用できる

---

## セットアップ

依存パッケージなし・ビルドステップなし。

```bash
git clone https://github.com/snowtone-ai/html-brief.git
cd html-brief
```

Claude Codeへのインストール例：

```bash
mkdir -p ~/.claude/skills
ln -sf "$(pwd)/skills/html-brief" ~/.claude/skills/html-brief
```

インストール後、Claude Code上で以下のように呼び出します。

```
/html-brief ゼロダウンタイムのPostgresマイグレーション計画を作成して
```

検証コマンド：

```bash
python scripts/validate.py
```

---

## ライセンス

MIT
