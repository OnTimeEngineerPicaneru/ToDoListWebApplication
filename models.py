from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# ==================================================
# データベースのインスタンス生成
# ==================================================
db = SQLAlchemy()


# ==================================================
# ユーザマスタ
# ==================================================
class User(UserMixin, db.Model):
    __tablename__ = "user_table"
    # DBのID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # ログインID
    login_id = db.Column(db.String(100), nullable=False, unique=True)
    # パスワード
    password = db.Column(db.String(10), nullable=False)


class Todo(db.Model):
    __tablename__ = "to_do_table"
    # DBのID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    description = db.Column(db.String(100), nullable=False, unique=False)
    due_date = db.Column(db.Date, nullable=False, unique=False)
    priority = db.Column(db.String(100), nullable=False, unique=False)
    status = db.Column(db.Boolean, nullable=False, unique=False, default=False)
