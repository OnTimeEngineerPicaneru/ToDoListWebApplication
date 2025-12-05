from flask import (
    request,
    redirect,
    render_template,
    url_for,
    flash,
    current_app,
)
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Todo
from app import app
from datetime import datetime


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template(
            "login.html", messages="IDとパスワードを入力してください"
        )
    else:
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        if user_id == "test" and password == "test":
            return redirect(url_for("home"))
        else:
            return render_template("login.html")


# タスクの一覧を取得して表示させる
@app.route("/home", methods=["GET"])
def home():
    incomplete_tasks = Todo.query.filter_by(status=False).all()
    completed_tasks = Todo.query.filter_by(status=True).all()
    return render_template(
        "home.html", incomplete_tasks=incomplete_tasks, completed_tasks=completed_tasks
    )


# 新規タスクの追加
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "GET":
        return render_template("add_task.html")
    else:
        # フォームから日付の文字列を取得
        due_date_str = request.form.get("due_date")

        # 日付文字列が空でないことを確認
        if due_date_str:
            # 文字列をdatetimeオブジェクトに変換し、さらにdateオブジェクトに変換
            due_date_obj = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        else:
            # 日付が選択されなかった場合の処理（エラーにするか、デフォルト値を入れるかなど）
            flash("期限が入力されていません。", category="error")
            return render_template("add_task.html")

        try:
            insert_data = Todo(
                title=request.form.get("title"),
                description=request.form.get("description"),
                due_date=due_date_obj,  # 変換したdateオブジェクトを渡す
                priority=request.form.get("priority"),
            )

            db.session.add(insert_data)
            db.session.commit()
            flash("タスクを追加しました。", category="success")

        except:
            flash("タスクの追加に失敗しました。", category="error")

        # 成功後は一覧ページなどにリダイレクトするのが一般的です
        return redirect(url_for("add_task"))


# 完了未完了
@app.route("/change_status", methods=["GET"])
def change_status():
    task_id = request.args.get("id")
    task_data = Todo.query.filter_by(id=task_id).first()

    task_data.status = False if task_data.status else True
    db.session.commit()

    return redirect(url_for("home"))


# ユーザー設定
@app.route("/config_user", methods=["GET"])
def config_user():
    return render_template("user_list.html")


# ユーザの追加
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    else:
        user_name = request.form.get("username")
        password = request.form.get("password")

        # DBに追加
        new_data = {user_name: user_name, password: password}

        try:
            flash("ユーザーを追加しました。", category="success")
        except:
            flash("ユーザーを追加できませんでした。", category="error")

        return render_template("add_user.html")
