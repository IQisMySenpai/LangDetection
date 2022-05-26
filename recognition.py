from dataclasses import dataclass
import os


@dataclass()
class LanguageDetection:
    language: str
    matches: int
    probability: float

    def __cmp__(self, other):
        if self.probability < other.probability:
            return -1
        elif self.probability > other.probability:
            return 1
        else:
            return 0

    def __le__(self, other):
        return self.probability <= other.probability

    def __lt__(self, other):
        return self.probability < other.probability

    def __gt__(self, other):
        return self.probability > other.probability

    def __ge__(self, other):
        return self.probability >= other.probability


class Recognition:
    words = {}
    langs = {}

    def __init__(self, fp: str = '', langs: dict = None):
        if langs is None or len(langs) < 1:
            exit()

        self.langs = langs

        for lang in langs:
            self.words[lang] = open(os.path.join(fp, f'{lang}.txt'), 'r', encoding='utf8').read().splitlines()

    def detect(self, text):
        text = text.lower()
        score = []
        total_chars = len(text)

        for lang in self.words:
            lang_chars = 0
            cur_lang = LanguageDetection(language=lang, matches=0, probability=0)

            spaced = self.langs[lang]

            for word in self.words[lang]:
                if spaced:
                    word = f'{word} '
                count = text.count(word)

                cur_lang.matches += count

                lang_chars += count * len(word)

            cur_lang.probability = lang_chars/total_chars
            score.append(cur_lang)

        # for i in range(len(score)):
        #     if total_chars > 0:
        #         score[i].probability = score[i].matches/total_chars

        # return dict(sorted(score.items(), key=lambda item: item[1]['probability'], reverse=True))
        return sorted(score, reverse=True)


def lower_text (fp, lang):
    words = open(os.path.join(fp, f'{lang}.txt'), 'r', encoding='utf8').read().splitlines()
    new_words = []
    for i in range(len(words)):
        if words[i] != '' and len(words[i]) > 1:
            new_words.append(words[i].lower())

    with open(os.path.join(fp, f'{lang}.txt'), 'w', encoding='utf8') as file:
        [file.write(f'{new_words[i]}\n') for i in range(len(new_words)-1)]
        file.write(new_words[-1])
