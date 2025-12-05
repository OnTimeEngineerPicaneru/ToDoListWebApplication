# ToDoアプリ

FlaskとSQLAlchemyを使用したシンプルなToDoリスト管理アプリケーションです。教育目的で作成されており、Webアプリケーション開発の基礎を学ぶことができます。

## 概要

このアプリケーションは、タスクの追加、完了/未完了の切り替え、期限や優先度の管理などの基本的なToDo管理機能を提供します。

## 主な機能

- タスクの追加（タイトル、説明、期限、優先度）
- タスクの完了/未完了の切り替え
- 完了タスクと未完了タスクの分類表示
- SQLiteデータベースによるデータ永続化

## 技術スタック

- **Backend**: Flask 3.1.2
- **Database**: SQLite + SQLAlchemy 2.0.43
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Migration**: Flask-Migrate 4.1.0, Alembic 1.16.5
- **Authentication**: Flask-Login 0.6.3（準備済み、未実装）
- **Template Engine**: Jinja2 3.1.6

## プロジェクト構造

```
ToDoアプリ/
├── app.py                 # メインアプリケーションファイル
├── models.py              # データベースモデル定義
├── views.py               # ルート定義とビュー処理
├── config.py              # アプリケーション設定
├── requirements.txt       # 依存パッケージ
├── TODO-APP.wsgi         # WSGI設定ファイル
└── templates/            # HTMLテンプレート
    ├── base.html         # ベーステンプレート
    ├── login.html        # ログイン画面
    ├── home.html         # ホーム画面（タスク一覧）
    ├── add_task.html     # タスク追加画面
    ├── add_user.html     # ユーザー追加画面
    └── user_list.html    # ユーザー一覧画面
```

## セットアップ

### 必要な環境

- Python 3.8以上
- pip

### インストール手順

1. リポジトリのクローン（またはダウンロード）

2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

3. データベースの初期化

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4. アプリケーションの起動

```bash
python app.py
```

5. ブラウザで以下のURLにアクセス

```
http://localhost:5000
```

## 使い方

### ログイン

現在はテスト用の認証のみ実装されています。
- ユーザーID: `test`
- パスワード: `test`

### タスクの追加

1. ログイン後、タスク追加画面に移動
2. 以下の情報を入力
   - タイトル
   - 説明
   - 期限
   - 優先度
3. 「追加」ボタンをクリック

### タスクの管理

- ホーム画面で未完了タスクと完了タスクを確認
- タスクをクリックして完了/未完了を切り替え

## データベースモデル

### User（ユーザーテーブル）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | Integer | 主キー |
| login_id | String(100) | ログインID（ユニーク） |
| password | String(10) | パスワード |

### Todo（ToDoテーブル）

| カラム名 | 型 | 説明 |
|---------|-----|------|
| id | Integer | 主キー |
| title | String(100) | タスクタイトル |
| description | String(100) | タスク説明 |
| due_date | Date | 期限 |
| priority | String(100) | 優先度 |
| status | Boolean | 完了状態（False: 未完了, True: 完了） |

## 設定

設定は [config.py](config.py) で管理されています。

- **DEBUG**: デバッグモード（デフォルト: True）
- **SQLALCHEMY_DATABASE_URI**: データベースのパス
- **SECRET_KEY**: セッション管理用のシークレットキー

## 既知の制限事項

- ユーザー認証機能は未実装（Flask-Loginの準備は完了）
- ユーザー追加機能は未完成
- パスワードは平文で保存（本番環境では暗号化が必要）
- タスクの編集・削除機能は未実装
- ユーザーごとのタスク管理は未実装

## 今後の改善予定

- [ ] 完全なユーザー認証機能の実装
- [ ] パスワードのハッシュ化（werkzeug.securityの使用）
- [ ] タスクの編集機能
- [ ] タスクの削除機能
- [ ] ユーザーごとのタスク管理
- [ ] タスクの検索・フィルタリング機能
- [ ] レスポンシブデザインの改善

## 本番環境へのデプロイ

本番環境にデプロイする際は、以下の点に注意してください。

1. **デバッグモードを無効化**
   - [config.py](config.py) の `DEBUG = False` に変更

2. **シークレットキーの変更**
   - `SECRET_KEY` を強力なランダム文字列に変更

3. **データベースの変更**
   - 本番環境では PostgreSQL や MySQL の使用を推奨

4. **WSGI設定**
   - [TODO-APP.wsgi](TODO-APP.wsgi) を使用してApacheやNginx + Gunicornでデプロイ

5. **環境変数の使用**
   - 機密情報は環境変数で管理

## ライセンス

このプロジェクトは非公開です。

## 作者

On Time Engineer

## 学習のポイント

このプロジェクトを通じて学べる内容：

- Flaskの基本的な使い方
- SQLAlchemyによるORM操作
- データベースマイグレーション
- Jinja2テンプレートエンジン
- MVCパターンの基礎
- フォームの処理
- セッション管理
- RESTfulなルーティング

## トラブルシューティング

### データベースエラー

データベースファイルが壊れた場合：

```bash
rm to_do_list.sqlite
flask db upgrade
```

### ポートが使用中

別のポートで起動する場合、[app.py](app.py) の最終行を変更：

```python
app.run(host="0.0.0.0", port=5001)  # ポート番号を変更
```

### パッケージのインポートエラー

依存パッケージを再インストール：

```bash
pip install -r requirements.txt --force-reinstall
```

## サポート

質問や問題がある場合は、プロジェクト管理者に連絡してください。
