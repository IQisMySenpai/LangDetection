class Recognition:
    words = {}
    langs = {}

    def __init__(self, langs: dict = None):
        if langs is None or len(langs) < 1:
            exit()

        self.langs = langs

        for lang in langs:
            self.words[lang] = open(f'{lang}.txt', 'r', encoding='utf8').read().splitlines()

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
                if count > 0:
                    print(f'{lang} has found {word}: {count} times')
                score[lang]['matches'] += count

            total_words += score[lang]['matches']

        for lang in self.words:
            score[lang]['probability'] = score[lang]['matches']/total_words

        return dict(sorted(score.items(), key=lambda item: item[1]['probability'], reverse=True))


def lower_text (lang):
    words = open(f'{lang}.txt', 'r', encoding='utf8').read().splitlines()
    new_words = []
    for i in range(len(words)):
        if words[i] != '' and len(words[i]) > 2:
            new_words.append(words[i].lower())

    with open(f'{lang}.txt', 'w', encoding='utf8') as file:
        [file.write(f'{new_words[i]}\n') for i in range(len(new_words)-1)]
        file.write(new_words[-1])
