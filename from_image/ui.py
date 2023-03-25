import toga
from from_image import ui_handler as uih


def create_ui(_):
    """ui setup"""
    box = toga.Box()

    button = toga.Button("Do", on_press=uih.click_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box
