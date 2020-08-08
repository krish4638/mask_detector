from flask import Flask,jsonify, request
from inference import inference
import flask
import os
import flask_cors


app = Flask(__name__)
flask_cors.CORS(app=app)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route('/inference', methods=['POST'])
def predict():
    content = request.files['image']
    content.save(content.filename)
    label, prob = inference(os.path.join("./", content.filename))
    os.remove(content.filename)
    return jsonify(result=label, probability=prob)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, threaded = True)

