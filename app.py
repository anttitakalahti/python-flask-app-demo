import os
import torch
import numpy
from predictor import initialize_model, predict
from flask import Flask, json, redirect, request
from image import jpg_pixels_without_rgb
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response

app = Flask(__name__)

dirname = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(dirname, 'upload')

@app.route('/')
def hello_world() -> str:
    return 'Hello World! I\'m a Dockerized Flask app!'


@app.route('/predict', methods=['POST'])
def predict_label() -> Response:
    main()

    if 'file' not in request.files:
        return redirect('/')

    # http://flask.pocoo.org/docs/1.0/api/#flask.Request.files
    file = request.files['file']
    if file.filename == '':
        return redirect('/')

    filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(filename)

    p = jpg_pixels_without_rgb(filename)

    # TODO learn how to initialize this properly
    pixels = torch.zeros(1, 1, 28, 28)
    pixels[0][0] = torch.from_numpy(p)

    print(type(pixels))

    return json.jsonify(predict(pixels))


def main():
    initialize_model()

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
