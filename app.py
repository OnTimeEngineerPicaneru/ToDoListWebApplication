# ===================================================
# メインファイル
# ===================================================

# 起動ファイル
from flask import Flask
from flask_migrate import Migrate
from models import db, User, Todo
from flask_login import LoginManager
from markupsafe import Markup
from datetime import datetime


# ===================================================
# インスタンス生成
# ===================================================
app = Flask(__name__)

# ===================================================
# 設定ファイルの読み込み
# ===================================================
app.config.from_object("config.Config")


# ===================================================
# データベース
# ===================================================
db.init_app(app)
migrate = Migrate(app, db)


# ===================================================
# FlaskとLoginの紐づけ
# ===================================================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# ユーザIDを引数としてそのIDに対するユーザ情報をデータベースから取得する
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===================================================
# 表示処理
# ===================================================
# 改行処理　{{quiz.more | cr}}
@app.template_filter("cr")
def cr(args):
    return Markup(str(args).replace("\r\n", "<br>"))


# ===================================================
# エラー設定（未定義）
# ===================================================


# ===================================================
# メイン処理
# ===================================================
from views import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
