from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return {
        "service": "terraform-runner",
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)