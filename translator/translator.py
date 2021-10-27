from googletrans import Translator

LENGUAGE = 'pt'

translation = Translator()
text = translation.translate('How did you learn Python?', dest='pt').text


def translate(original_text):
    translation = Translator()
    output_text = translation.translate(original_text, dest=LENGUAGE).text

    return output_text
