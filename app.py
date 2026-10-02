from datetime import datetime
import importlib.metadata
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    # 取得目前 Flask 版本與伺服器時間
    try:
        flask_ver = importlib.metadata.version("flask")
    except Exception:
        flask_ver = "3.x"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html", flask_version=flask_ver, server_time=current_time
    )


if __name__ == "__main__":
    # 啟動本機開發伺服器，預設埠為 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
