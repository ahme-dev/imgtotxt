import sys
import toga
from toga.style.pack import Pack, ROW, CENTER, COLUMN
from from_image.ocr import LANGUAGES, load_reader, read_from_image


class FromImageApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)
        self.on_exit = self.action_question_dialog

        image = toga.ImageView(toga.Image("../mock/note.png"))
        image.style.update(height=300, width=300)

        box = toga.Box(
            children=[
                toga.Box(
                    style=Pack(direction=ROW, alignment=CENTER, padding=10),
                    children=[
                        toga.Box(
                            style=Pack(direction=COLUMN, alignment=CENTER),
                            children=[
                                image,
                                toga.Button(
                                    "Open file",
                                    on_press=self.action_open_file_filtered_dialog,
                                ),
                            ],
                        ),
                        toga.Box(children=[toga.Label("hello")]),
                    ],
                )
            ]
        )
        # self.on_exit = self.exit_handler
        self.main_window.content = box
        self.main_window.show()

    async def action_open_file_filtered_dialog(self, _):
        try:
            fname = await self.main_window.open_file_dialog(
                title="Open file with Toga",
                multiselect=False,
                file_types=["png", "jpg", "jpeg"],
            )
            if fname is not None:
                self.main_window.title = f"File to open: {fname}"
            else:
                self.main_window.title = "No file selected!"
        except ValueError:
            self.main_window.text = "Open file dialog was canceled"

    async def action_question_dialog(self, _):
        if await self.main_window.question_dialog(
            "FromImage", "Do you want to exit the app?"
        ):
            self.exit_handler()
        else:
            return

    def click_handler(self, btn):
        reader, error = load_reader(["en", "ar", "ku"])

        if isinstance(error, Exception):
            print(error)
            btn.text = "Error"
            return

        read_from_image(reader, "mock/note.png")
        btn.text = "Read"

    def exit_handler(self):
        print("Exited")
        sys.exit(0)


def run_app():
    return FromImageApp(
        formal_name="FromImage",
        app_id="systems.ahmed.from-image",
        app_name="from-image",
        author="https://ahmed.systems",
    )
