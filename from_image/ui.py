import toga
from toga import Button
from toga.style.pack import Pack, ROW, CENTER
from from_image.ocr import get_languages, load_reader, read_from_image


def create_ui(_):
    return toga.Box(
        children=[
            toga.Box(
                style=Pack(direction=ROW, alignment=CENTER, padding=10),
                children=[
                    toga.Label("Languages:"),
                    toga.Selection(items=list(get_languages().keys())),
                    toga.Button("Do", on_press=click_handler),
                ],
            )
        ]
    )


def click_handler(btn: Button):
    reader, error = load_reader(["en", "ar", "ku"])
    if isinstance(error, Exception):
        print(error)
        btn.text = "Error"
        return

    read_from_image(reader, "mock/note.png")
    btn.text = "Read"
