from google.cloud import translate

translate_client = translate.Client()
target = 'en'

def detect_language(text):
    result = translate_client.detect_language(text)
    return result['language']

def translate_text(text):
    translation = translate_client.translate(
        text,
        target_language=target)
    translatedText = str(translation['translatedText']).lower()
    return translatedText