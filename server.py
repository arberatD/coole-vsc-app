from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/enrico')
def enrico():
  return jsonify({"name": "Enrico"})
@app.route('/push-force-hard')
def force():
    return "Force push hard"

@app.route('/flamur')
def flamur():
    return 'Flamurs Endpoint'
=======
@app.route('/muhammed', methods=['GET'])
def muhammed():
    return "Hallo, Muhammed!", 200
>>>>>>> 819ac2a (feat:Endpoint GET-request Hello)

if __name__ == '__main__':
    app.run(debug=True)