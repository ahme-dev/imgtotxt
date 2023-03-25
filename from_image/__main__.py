""""main module"""

import sys
import toga
from from_image.ui import create_ui


def run_app():
    """run the app"""
    return toga.App(
        formal_name="From Image",
        app_id="systems.ahmed.from-image",
        app_name="from-image",
        author="https://ahmed.systems",
        startup=create_ui,
        on_exit=exit_app,
    )


def exit_app(_):
    """exit the app"""
    print("Exited")
    sys.exit(0)


# run the main loop
run_app().main_loop()
