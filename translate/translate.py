
# Imports the Google Cloud client library
from google.cloud import translate


class Translator:
    translate_client = None

    # Instantiates a client
    translate_client = translate.Client()

    def translate(self, message, language):
        print(message, language)
        if message is not None:
            print(message)
            # Translates some text into spanish
            translation = self.translate_client.translate(
                message,
                target_language=language)
            return translation
        return None


if __name__ == '__main__':
    text = 'Testing if this works!'
    translator = Translator()
    translation = translator.translate(text)
    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
