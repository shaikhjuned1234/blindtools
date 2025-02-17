from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({"sum": a + b})
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

@app.route('/json')
def json_example():
    return jsonify({
        "message": "This is a JSON response",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)
