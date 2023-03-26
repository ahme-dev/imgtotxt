from imgtotxt.ocr import LANGUAGES


class AppState:
    def __init__(self):
        self.langs = []
        self.image = "No image selected"
        self.text = "No text extracted"

    def get_langs_text(self):
        """retun a nicely formatted string of languages or none"""
        text = ", ".join(self.langs)
        ret = text if len(text) > 0 else "None"
        return ret

    def modify_langs(self, lang):
        """add lang to list, and remove if already in list"""
        # if language is already in list remove it
        if lang in self.langs:
            self.langs.remove(lang)
            # return
            return

        # if there are 5 languages in the list, don't add
        if len(self.langs) > 5:
            return

        # otherwise add to list
        self.langs.append(lang)


current = AppState()
