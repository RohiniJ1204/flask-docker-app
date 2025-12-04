from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home endpoint accessed")
    return "Branch DevOps Container Running!"

@app.route('/health')
def health():
    app.logger.info("Health check endpoint accessed")
    return "Healthy"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
