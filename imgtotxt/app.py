import sys
import toga
from toga.style.pack import Pack, ROW, CENTER, COLUMN
from imgtotxt.ocr import LANGUAGES, load_reader, read_from_image


APP_NAME = "ImgToText"


class MyApp(toga.App):
    def startup(self):
        # create main window
        self.main_window = toga.MainWindow(title=self.name)

        # create image
        image = toga.ImageView(toga.Image("../mock/note.png"))
        image.style.update(height=300, width=300)

        # create styles for the components
        title_style = Pack(font_size=20, padding_bottom=12, padding_top=10)
        button_style = Pack(padding_bottom=8)
        container_style = Pack(
            padding_bottom=5, padding_top=5, padding_left=20, padding_right=20
        )

        box = toga.Box(
            style=Pack(direction=ROW, padding=10),
            children=[
                toga.Box(
                    style=Pack(direction=COLUMN, padding=10),
                    children=[
                        toga.Label("Actions", style=title_style),
                        toga.Button("Languages", style=button_style),
                        toga.Button("Open Image", style=button_style),
                        toga.Button("Extract Text", style=button_style),
                    ],
                ),
                toga.Divider(direction=toga.Divider.VERTICAL, style=container_style),
                toga.Box(
                    style=Pack(direction=COLUMN, padding=10),
                    children=[
                        toga.Label("Image", style=title_style),
                        toga.Label("Text", style=title_style),
                        toga.Label("The text extracted will display here"),
                    ],
                ),
            ],
        )

        # hook on exit handler, add content to main window and show
        self.on_exit = self.action_question_dialog
        self.main_window.size = (500, 300)
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
            APP_NAME, "Do you want to exit the app?"
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
    return MyApp(
        formal_name=APP_NAME,
        description="A native python OCR app running locally to extract text from your images.",
        app_id="systems.ahmed.imgtotxt",
        app_name=APP_NAME.lower(),
        home_page="http://ahmed.systems",
        author="Ahmed K. A.",
    )
