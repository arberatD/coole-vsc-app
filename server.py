from flask import Flask

app = Flask(__name__)

@app.route('/enrico')
def enrico():
  return jsonify({"name": "Enrico"})
@app.route('/push-force-hard')
def force():
    return "Force push hard"

@app.route('/flamur')
def flamur():
    return 'Flamurs Endpoint'

if __name__ == '__main__':
    app.run(debug=True)