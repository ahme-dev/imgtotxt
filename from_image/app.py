import sys
import toga
from toga.style.pack import Pack, ROW, CENTER, COLUMN
from from_image.ocr import LANGUAGES, load_reader, read_from_image


class FromImageApp(toga.App):
    def startup(self):
        # create main window
        self.main_window = toga.MainWindow(title=self.name)

        # create image
        image = toga.ImageView(toga.Image("../mock/note.png"))
        image.style.update(height=300, width=300)

        box = toga.Box(children=[])

        # hook on exit handler, add content to main window and show
        self.on_exit = self.action_question_dialog
        self.main_window.content = box
        self.main_window.show()

    async def action_open_file_filtered_dialog(self, _):
        """open a file dialog with filetype filters"""
        try:
            # open a dialog and get filepath
            fname = await self.main_window.open_file_dialog(
                title="Open an image to read text from",
                multiselect=False,
                file_types=["png", "jpg", "jpeg"],
            )

            # if no file was selected return
            if fname is None:
                self.main_window.title = "No file selected!"
                return

            self.main_window.title = f"File to open: {fname}"
        except ValueError:
            self.main_window.text = "Open file dialog was canceled"

    async def action_question_dialog(self, _):
        """on app exit ask for confirmation"""
        if await self.main_window.question_dialog(
            "FromImage", "Do you want to exit the app?"
        ):
            print("Exited")
            sys.exit(0)
        else:
            return

    # def click_handler(self, btn):
    #     reader, error = load_reader(["en", "ar", "ku"])

    #     if isinstance(error, Exception):
    #         print(error)
    #         btn.text = "Error"
    #         return

    #     read_from_image(reader, "mock/note.png")
    #     btn.text = "Read"


def run_app():
    return FromImageApp(
        formal_name="FromImage",
        app_id="systems.ahmed.from-image",
        app_name="from-image",
        author="https://ahmed.systems",
    )
