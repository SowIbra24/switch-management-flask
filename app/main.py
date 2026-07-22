
import os 
from flask import Flask, render_template # pyright: ignore[reportMissingImports]
from app.keepass_service import get_all_switches, get_switch_by_name


template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/")
def index():
    switches = get_all_switches()
    return render_template("index.html", switches=switches)

@app.route("/connect/<switch_name>")
def connect(switch_name):
   entry = get_switch_by_name(switch_name)
   if not entry:
       return "Switch not found", 404

   login_url = f"{entry.url}/v1/base/cheetah_login.html"

   return render_template(
        "autologin.html",
        login_url=login_url,
        password=entry.password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
