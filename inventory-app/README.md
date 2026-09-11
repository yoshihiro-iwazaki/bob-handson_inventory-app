# 在庫管理システム

ハンズオン用に作成したシンプルな在庫管理アプリケーションです。

## 📋 目次

- [機能概要](#機能概要)
- [技術スタック](#技術スタック)
- [セットアップ手順](#セットアップ手順)
- [使い方](#使い方)
- [プロジェクト構造](#プロジェクト構造)

## 🎯 機能概要

### 実装済みの機能

1. **ダッシュボード**
   - 在庫サマリー表示（総商品数、総在庫数、総在庫額、カテゴリ数）
   - 最近の入出庫履歴表示
   - クイックアクション

2. **商品管理**
   - 商品一覧表示
   - 商品の新規登録
   - 在庫の入庫・出庫処理
   - 商品検索（商品名・カテゴリ）

3. **履歴管理**
   - 全入出庫履歴の表示
   - 商品別履歴の表示
   - 統計情報の表示

## 🛠 技術スタック

- **バックエンド**: Python 3.12 / 3.13 / 3.14（動作確認済み）
- **Webフレームワーク**: Flask 3.0.0
- **データ処理**: pandas 2.3.3
- **データ保存**: CSV形式（SQLite不使用）
- **フロントエンド**: HTML5, Bootstrap 5.3, Bootstrap Icons

## 🚀 セットアップ手順

### 1. 前提条件

- Python 3.12 / 3.13 / 3.14 のいずれかがインストールされていること
- pandas 2.3.3 のビルド済みパッケージが提供されているバージョンです。他のバージョンではインストールに失敗する場合があります
- pipが利用可能であること

### 2. インストール

```bash
# プロジェクトディレクトリに移動
cd inventory-app

# 仮想環境の作成（推奨）
# Windowsで python が反応しない場合は py -m venv venv
python -m venv venv

# 仮想環境の有効化
# Windows (コマンドプロンプト):
venv\Scripts\activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 依存パッケージのインストール
pip install -r requirements.txt
```

### 3. アプリケーションの起動

```bash
# Flaskアプリケーションの起動
python app.py
```

ブラウザで `http://localhost:5001` にアクセスしてください。

## 📖 使い方

### 商品の追加
1. 「商品管理」ページに移動
2. 「商品追加」ボタンをクリック
3. 商品情報を入力して「追加」

### 在庫の更新
1. 「商品管理」ページで対象商品の「更新」ボタンをクリック
2. 「入庫」または「出庫」を選択
3. 数量を入力して「更新」

## 📁 プロジェクト構造

```
inventory-app/
├── data
│   ├── history.csv
│   └── products.csv
├── doc
│   └── requirements-specification.md  #要件定義書
├── static
│   └── style.css
├── templates
│   ├── base.html
│   ├── history.html
│   ├── index.html
│   └── products.html
├── .bobignore                            #Bobがアクセスしないファイルの指定
├── .gitignore
├── app.py                                #アプリのメインファイル
├── data_manager.py
├── python-coding-rules.txt               #コーディング規約
├── README.md
└── requirements.txt
```
