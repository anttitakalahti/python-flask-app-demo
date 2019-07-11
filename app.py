import os
import torch

from flask import Flask, json, redirect, request
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response

import database
import image
import predictor

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp"  # /tmp is the only place where web app can write


@app.route("/")
def hello_world() -> str:
    return "Hello World! I'm a Dockerized Flask app!"


@app.route("/predict", methods=["POST"])
def predict_label() -> Response:
    if not has_file_form_field(request):
        return redirect("/")

    file = request.files["file"]

    filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(filename)

    # TODO learn how to initialize this properly
    pixels = torch.zeros(1, 1, 28, 28)
    pixels[0][0] = torch.from_numpy(image.jpg_pixels_without_rgb(filename))

    prediction = predictor.predict(pixels)

    return json.jsonify({"predicted_label": prediction})


@app.route("/store", methods=["POST"])
def store() -> Response:
    if not has_file_form_field(request):
        return redirect("/")

    file = request.files["file"]

    filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(filename)

    pixels = image.jpg_pixels_without_rgb(filename)
    label = int(request.form['label'])

    image_id = database.store_image_with_label(pixels, label)

    return json.jsonify({"image_id": image_id})


def has_file_form_field(req: request) -> bool:
    if "file" not in req.files:
        return False

    file = req.files["file"]
    if file.filename == "":
        return False

    return True


def main():
    predictor.initialize_model()

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
