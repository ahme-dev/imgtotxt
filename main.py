""""main module"""
import toga
import easyocr as ocr


def read_and_write(*args):
    """read from image file and write to text file"""
    reader = ocr.Reader(["en", "ar"])
    read_result = reader.readtext("note.png", paragraph=True)
    with open("res.txt", "x", encoding="utf-8") as file:
        for i, item in enumerate(read_result):
            file.write(str(i) + item[1] + "\n")


def build(app):
    """ui setup"""
    box = toga.Box()

    button = toga.Button("Do", on_press=read_and_write)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    """main app run"""
    return toga.App("From Image", "systems.ahmed.from-image", startup=build)


if __name__ == "__main__":
    main().main_loop()
