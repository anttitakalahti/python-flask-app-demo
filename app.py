import os
import torch
from predictor import initialize_model, predict
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World! I\'m a Dockerized Flask app!'


@app.route('/predict')
def predict_label() -> str:
    pixels = torch.zeros(1, 1, 28, 28)

    return predict(pixels)


def main():
    initialize_model()

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
