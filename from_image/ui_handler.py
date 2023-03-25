from from_image.ocr import load_reader, read_from_image


def click_handler(_):
    """handle the button click"""
    reader, error = load_reader(["en", "ar", "ku"])
    if isinstance(error, Exception):
        print("Exception:", error)
        return

    read_from_image(reader, "mock/note.png")
