from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"message": f"Hello, {name}!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8100, debug=True)

