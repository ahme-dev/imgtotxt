import sys
import toga
from toga.style.pack import Pack, ROW, COLUMN, TOP
from imgtotxt import state
from imgtotxt.ocr import LANGUAGES, load_reader, read_from_image


APP_NAME = "ImgToText"


class MyApp(toga.App):
    def startup(self):
        # create main window
        self.main_window = toga.MainWindow(title=self.name)

        # create styles for the components
        title_style = Pack(font_size=20, padding_bottom=10, padding_top=20)
        button_style = Pack(padding_bottom=8)
        container_style = Pack(
            padding_bottom=5, padding_top=5, padding_left=20, padding_right=20
        )

        # bind some components to self
        self.langsLabel = toga.Label(state.current.get_langs_text())
        self.imageLabel = toga.Label(state.current.image)
        self.textLabel = toga.Label(state.current.text)

        box = toga.Box(
            style=Pack(direction=ROW, padding=20, padding_bottom=30, padding_top=0),
            children=[
                toga.Box(
                    style=Pack(direction=COLUMN, padding=10),
                    children=[
                        toga.Label("Actions", style=title_style),
                        toga.Button(
                            "Languages",
                            style=button_style,
                            on_press=self.action_open_secondary_window,
                        ),
                        toga.Button(
                            "Open Image",
                            style=button_style,
                            on_press=self.action_open_file_filtered_dialog,
                        ),
                        toga.Button(
                            "Extract Text",
                            style=button_style,
                            on_press=self.extract_text,
                        ),
                    ],
                ),
                toga.Divider(direction=toga.Divider.VERTICAL, style=container_style),
                toga.Box(
                    style=Pack(direction=COLUMN, padding=10, flex=1),
                    children=[
                        toga.Label("Selected Languages", style=title_style),
                        self.langsLabel,
                        toga.Label("Current Image", style=title_style),
                        self.imageLabel,
                        toga.Label("Extracted Text", style=title_style),
                        toga.ScrollContainer(
                            style=Pack(flex=1),
                            vertical=True,
                            content=toga.Box(
                                style=Pack(flex=1, direction=ROW, alignment=TOP),
                                children=[
                                    self.textLabel,
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        )

        # hook on exit handler, add content to main window, set size, and show
        self.on_exit = self.action_question_dialog
        self.main_window.size = (500, 400)
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
                # reset ui and state to none
                state.current.image = "No image selected"
                self.imageLabel.text = "No image selected"
                return

            # otherwise set both ui and state to filename
            state.current.image = str(fname)
            self.imageLabel.text = str(fname)

        except ValueError:
            return

    async def action_question_dialog(self, _):
        """on app exit ask for confirmation"""
        if await self.main_window.question_dialog(
            APP_NAME, "Do you want to exit the app?"
        ):
            print("Exited")
            sys.exit(0)
        else:
            return

    def action_open_secondary_window(self, _):
        window = toga.Window(title="Selected languages to detect")

        lang_item_style = Pack(padding_bottom=10)

        self.langPopupLabel = toga.Label(
            f"Selected: {state.current.get_langs_text()}", style=lang_item_style
        )

        window.content = toga.Box(
            style=Pack(flex=1, direction=COLUMN, padding=20),
            children=[
                toga.Label(
                    style=lang_item_style,
                    text="Note: some languages are incompatible with each other",
                ),
                toga.Selection(
                    items=list(LANGUAGES.keys()),
                    style=lang_item_style,
                    on_select=self.change_select,
                ),
                self.langPopupLabel,
                toga.Button(
                    "Load languages", on_press=self.load_langs, style=lang_item_style
                ),
            ],
        )

        self.windows += window
        window.size = (200, 100)
        window.show()

    def change_select(self, widget: toga.Selection):
        """on new selection change state and ui"""
        state.current.modify_langs(widget.value)
        self.langPopupLabel.text = f"Selected: {state.current.get_langs_text()}"
        self.langsLabel.text = state.current.get_langs_text()

    def load_langs(self, _):
        # if no languages are selected
        if len(state.current.langs) < 1:
            self.langPopupLabel.text = "You have not selected any languages"
            return

        # try to load the languages
        self.reader, error = load_reader(state.current.get_lang_keys())

        # if got an error
        if isinstance(error, Exception):
            # reset langs state and and set ui to error message
            state.current.reset_langs()
            self.langsLabel.text = state.current.get_langs_text()
            self.langPopupLabel.text = f"Error: {error}"
            return

        # otherwise set label to loaded
        self.langPopupLabel.text = "Loaded successfully"

    def extract_text(self, _):
        # if reader is None don't try to read
        if self.reader == None:
            return

        extracted_text = read_from_image(self.reader, state.current.image)
        self.textLabel.text = str(extracted_text)


def run_app():
    return MyApp(
        formal_name=APP_NAME,
        description="A native python OCR app running locally to extract text from your images.",
        app_id="systems.ahmed.imgtotxt",
        app_name=APP_NAME.lower(),
        home_page="http://ahmed.systems",
        author="Ahmed K. A.",
    )
