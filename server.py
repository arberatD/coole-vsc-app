from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/push-force-hard')
def force():
    return "Force push hard"