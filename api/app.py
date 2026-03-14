from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)

START_TIME = datetime.datetime.utcnow()

@app.route("/")
def home():
    return "API running"

@app.route("/api")
def hello():
    return jsonify({"message": "Hello from API"})

@app.route("/api/health")
def health():
    uptime = str(datetime.datetime.utcnow() - START_TIME).split('.')[0]
    return jsonify({
        "status": "healthy",
        "uptime": uptime,
        "version": os.environ.get("IMAGE_TAG", "local"),
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "app": "Agentic DevOps Demo",
        "engineer": "Dhana Shekhar",
        "stack": {
            "ci_cd": "GitHub Actions",
            "registry": "Azure ACR",
            "orchestration": "Kubernetes AKS",
            "gateway": "Kong API Gateway",
            "gitops": "ArgoCD",
            "cloud": "Azure Landing Zone"
        },
        "pipeline": "Build Once Deploy Many",
        "repo": "https://github.com/Dhana10/DevOps"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
