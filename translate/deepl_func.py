import deepl
import io

translator = None

def __init__():
    translator = deepl.Translator("")

    return translator

def ah(translated, tar_lang):
    
    result = translator.translate_text(translated, target_lang=tar_lang)
    print(result.text)