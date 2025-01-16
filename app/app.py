from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, GitOpsi! We will use the time and date pull policy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
