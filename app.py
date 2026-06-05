from flask import Flask, request, jsonify
import subprocess
import uuid

app = Flask(__name__)

@app.route("/")
def health():
    return {
        "service": "terraform-runner",
        "status": "UP"
    }

@app.route("/create-s3", methods=["POST"])
def create_s3():

    data = request.json

    bucket_name = (
        data.get("bucket_name")
        or f"cloud-orch-{uuid.uuid4().hex[:8]}"
    )

    subprocess.run(
        ["terraform", "init"],
        cwd="./terraform/s3"
    )

    subprocess.run(
        [
            "terraform",
            "apply",
            "-auto-approve",
            f"-var=bucket_name={bucket_name}"
        ],
        cwd="./terraform/s3"
    )

    return jsonify({
        "message": "S3 bucket created",
        "bucket": bucket_name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)