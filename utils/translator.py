from googletrans import Translator

def translate_ru_to_en(text):
    translator = Translator()
    try:
        return translator.translate(text, src='ru', dest='en').text
    except Exception as e:
        return f"An error occurred during translation: {e}"