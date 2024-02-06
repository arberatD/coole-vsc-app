from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/enrico')
def enrico():
  return jsonify({"name": "Enrico"})