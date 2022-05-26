import os


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
        score = {}
        total_words = 0

        for lang in self.words:
            score[lang] = {'matches': 0}

            spaced = self.langs[lang]

            for word in self.words[lang]:
                if spaced:
                    count = text.count(f'{word} ')
                else:
                    count = text.count(word)
                score[lang]['matches'] += count

            total_words += score[lang]['matches']

        for lang in self.words:
            if total_words > 0:
                score[lang]['probability'] = score[lang]['matches']/total_words
            else:
                score[lang]['probability'] = 0

        return dict(sorted(score.items(), key=lambda item: item[1]['probability'], reverse=True))


def lower_text (fp, lang):
    words = open(os.path.join(fp, f'{lang}.txt'), 'r', encoding='utf8').read().splitlines()
    new_words = []
    for i in range(len(words)):
        if words[i] != '' and len(words[i]) > 1:
            new_words.append(words[i].lower())

    with open(os.path.join(fp, f'{lang}.txt'), 'w', encoding='utf8') as file:
        [file.write(f'{new_words[i]}\n') for i in range(len(new_words)-1)]
        file.write(new_words[-1])
