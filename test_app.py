from io import BytesIO
import torch
import numpy

from app import app
import database
import image
import predictor


def mock_jpg_pixels_without_rgb(filename: str) -> numpy.ndarray:
    return numpy.zeros((28, 28))


def mock_predict(img: torch.Tensor) -> int:
    if not torch.all(torch.eq(torch.zeros(1, 1, 28, 28), img)):
        return 0

    return 11


def mock_store_image_with_label(pixels: numpy.ndarray, label: int) -> int:
    if not numpy.array_equal(numpy.zeros((28, 28)), pixels):
        return 0

    if label != 3:
        return 0

    return 10


def test_predict_label(monkeypatch):
    monkeypatch.setattr(image, "jpg_pixels_without_rgb", mock_jpg_pixels_without_rgb)
    monkeypatch.setattr(predictor, "predict", mock_predict)

    data = {
        "file": (BytesIO(b"my file contents"), "test_file.jpg")
    }

    client = app.test_client()
    res = client.post("/predict", data=data)

    assert res.data == b"{\"predicted_label\":11}\n"


def test_store(monkeypatch):
    monkeypatch.setattr(database, "store_image_with_label", mock_store_image_with_label)
    monkeypatch.setattr(image, "jpg_pixels_without_rgb", mock_jpg_pixels_without_rgb)

    data = {
        "file": (BytesIO(b"my file contents"), "test_file.jpg"),
        "label": 3
    }

    client = app.test_client()
    res = client.post("/store", data=data)

    assert res.data == b"{\"image_id\":10}\n"
