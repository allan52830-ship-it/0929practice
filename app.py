from datetime import datetime
import importlib.metadata
import os
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
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
