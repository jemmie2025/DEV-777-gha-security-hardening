from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        message="GitHub Actions Security Hardening Demo",
        status="running",
    )


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200
