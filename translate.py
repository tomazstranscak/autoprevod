from googletrans import Translator
import os

def translate_file(fajl, target_language):

    translator = Translator()
    
    with open(fajl, 'r', encoding='utf-8') as file:
        content = file.read()

    translated = translator.translate(content, dest=target_language)
    output_file = os.path.join(os.getcwd(), f'readme_{target_language}.md')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated.text)

def read_languages(lang_file):
    with open(lang_file, 'r', encoding='utf-8') as file:
        languages = [line.strip() for line in file if line.strip()]
    return languages

if __name__ == "__main__":
    fajl = 'readme.md'
    lang_file = 'jeziki.md'

    languages = read_languages(lang_file)
    for lang in languages:
        try:
            translate_file(fajl, lang)
        except:
            pass
