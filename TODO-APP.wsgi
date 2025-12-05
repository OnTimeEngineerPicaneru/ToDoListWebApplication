import sys

# プロジェクトのルートパスをシステムパスに追加
sys.path.insert(0, '/home/*****/www/TODO-APP')

# app.pyファイルから'app'という名前のFlaskインスタンスをインポート
# 'application'という名前で参照できるようにする
from app import app as application
