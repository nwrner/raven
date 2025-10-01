from flask import Flask
import os

app = Flask(__name__)

# Health state toggle
healthy = True

@app.route("/")
def home():
    return "Hello from the chaos lab! 💥"

@app.route("/healthz")
def healthz():
    if healthy:
        return "ok", 200
    else:
        return "not ok", 500

@app.route("/failz")
def failz():
    global healthy
    healthy = False
    return "Marked unhealthy 😈", 200

@app.route("/fixz")
def fixz():
    global healthy
    healthy = True
    return "Back to healthy ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)