"""interfaces for the easyocr package"""

from os import path
import easyocr as ocr
from easyocr import Reader


LANGUAGES = {
    "Abaza": "abq",
    "Adyghe": "ady",
    "Afrikaans": "af",
    "Angika": "ang",
    "Arabic": "ar",
    "Assamese": "as",
    "Avar": "ava",
    "Azerbaijani": "az",
    "Belarusian": "be",
    "Bulgarian": "bg",
    "Bihari": "bh",
    "Bhojpuri": "bho",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Simplified Chinese": "ch_sim",
    "Traditional Chinese": "ch_tra",
    "Chechen": "che",
    "Czech": "cs",
    "Welsh": "cy",
    "Danish": "da",
    "Dargwa": "dar",
    "German": "de",
    "English": "en",
    "Spanish": "es",
    "Estonian": "et",
    "Persian (Farsi)": "fa",
    "French": "fr",
    "Irish": "ga",
    "Goan Konkani": "gom",
    "Hindi": "hi",
    "Croatian": "hr",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Ingush": "inh",
    "Icelandic": "is",
    "Italian": "it",
    "Japanese": "ja",
    "Kabardian": "kbd",
    "Kannada": "kn",
    "Korean": "ko",
    "Kurdish": "ku",
    "Latin": "la",
    "Lak": "lbe",
    "Lezghian": "lez",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Magahi": "mah",
    "Maithili": "mai",
    "Maori": "mi",
    "Mongolian": "mn",
    "Marathi": "mr",
    "Malay": "ms",
    "Maltese": "mt",
    "Nepali": "ne",
    "Newari": "new",
    "Dutch": "nl",
    "Norwegian": "no",
    "Occitan": "oc",
    "Pali": "pi",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian (cyrillic)": "rs_cyrillic",
    "Serbian (latin)": "rs_latin",
    "Nagpuri": "sck",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Albanian": "sq",
    "Swedish": "sv",
    "Swahili": "sw",
    "Tamil": "ta",
    "Tabassaran": "tab",
    "Telugu": "te",
    "Thai": "th",
    "Tajik": "tjk",
    "Tagalog": "tl",
    "Turkish": "tr",
    "Uyghur": "ug",
    "Ukranian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
}


def load_reader(model_names: list[str]):
    """creates a reader by loading wanted models"""

    # if not provided any model names return error
    if len(model_names) < 1:
        return (None, Exception("No models provided"))

    try:
        # create a reader, load models, and return reader
        reader = ocr.Reader(model_names)
        return (reader, None)
    except ValueError as error:
        return (None, error)


def read_from_image(reader: Reader, image_path: str, paragraph=True):
    """uses reader to read text in given image path"""

    result = reader.readtext(image_path, paragraph=paragraph)

    result_string = ""

    for res in result:
        result_string += f"{res[1]} \n"

    return result_string
