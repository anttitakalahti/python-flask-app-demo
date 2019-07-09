import numpy
from PIL import Image


def jpg_pixels_without_rgb(filename: str) -> numpy.ndarray:
    i = Image.open(filename)

    # TODO test this!
    w, h = i.size
    if w != 28 and h != 28:
        i.resize((28, 28))

    i.load()
    img = i.convert("L")
    data = numpy.asarray(img, dtype="float32")

    return data
