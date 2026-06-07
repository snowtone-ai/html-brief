# html-brief

## 概要

AIエージェントが生成した長大な計画・比較・レビュー結果を、ブラウザで読める単一HTMLファイルに変換するスキル（拡張機能）です。400行にわたるテキストをスキャンしやすい構造・図・インタラクティブなコントロールを含む1ページのHTMLに整形し、「Copy as Prompt」ボタンで意思決定内容をそのまま次のAIセッションに返送できます。Claude Code・Codex CLI・Gemini CLI・Cursorで利用できます。

---

## 主な機能

- 実装計画・マイグレーション・RFC（技術仕様書）を視覚的なHTMLブリーフに変換できる
- 選択肢の比較・トレードオフ分析をカード形式と評価マトリクスで表示できる
- コードレビュー結果を重要度別に整理して表示できる
- インシデントレポートや調査結果をエグゼクティブサマリー付きで出力できる
- 「Copy as Prompt / JSON / Markdown」ボタンで決定内容をAIエージェントに返送できる（ラウンドトリップ）

---

## 技術スタック

フロントエンド：HTML・CSS・バニラJavaScript（依存パッケージなし・ビルドステップなし）
AI・外部API：Claude Code、Codex CLI、Gemini CLI、Cursorのスキル機構を利用（エージェント非依存のMarkdownベース定義）

---

## アーキテクチャの特徴

- 出力ファイルはCSSとJavaScriptをすべてインラインに含む単一HTMLファイルで、ブラウザさえあればどこでも開ける設計
- スキル定義（`SKILL.md`）がエージェント非依存のMarkdown形式で書かれており、複数のAIツールから共通利用できる

---

## 開発環境のセットアップ

依存パッケージなし・ビルドステップなし。

```bash
git clone https://github.com/YOUR_USERNAME/html-brief.git
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
