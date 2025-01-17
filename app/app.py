from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route with a welcome message
@app.route("/")
def home():
    return "Welcome to the Advanced Flask App! Try using '/greet/<name>' or '/calculate'."

# Dynamic route with a greeting
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name.capitalize()}! Nice to meet you!"

# Route that performs a basic calculation based on query parameters
@app.route("/calculate")
def calculate():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 + num2
        return jsonify({"num1": num1, "num2": num2, "result": result})
    except ValueError:
        return jsonify({"error": "Invalid input, please use numbers only."}), 400

# Custom error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Page not found! Check the URL."}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

