from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is trying with github action v2.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
