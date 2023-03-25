"""interfaces for the easyocr package"""

import easyocr as ocr
from easyocr import Reader


def load_reader(model_names: list[str]):
    """creates a reader by loading wanted models"""

    # if not provided any model names return error
    if len(model_names) < 1:
        return (None, Exception("wrong models provided"))

    try:
        # create a reader, load models, and return reader
        reader = ocr.Reader(model_names)
        return (reader, None)
    except ValueError as error:
        return (None, error)


def read_from_image(reader: Reader, image_path: str, paragraph=True):
    """uses reader to read text in given image path"""
    result = reader.readtext(image_path, paragraph=paragraph)

    print(result)
    print(result[0])
    print(result[0][0])
    return result
