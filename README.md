# LangDetection
## Table of Contents

1. [About The Project](#about-the-project)
   - [Built With](#built-with)
2. [Examples](#examples)
   - [Detection](#detection)
   - [Cleaning up word lists](#cleaning-up-word-lists)

## About The Project

We needed a language detection which recognizes a language not using ai, but on how many words matched a certain language. We are using the most common words of the languages that we need.

### Built With

* [Python 3.9](www.python.org)

## Examples

Some examples on how I am using the code.

### Detection
With for each lang, the name of the text file and if this language has spaces between words.

```python
from recognition import Recognition

langs = {'arabic': True,
         'chinese': False,
         'english': True,
         'french': True,
         'german': True,
         'hindi': True,
         'persian': True,
         'russian': True,
         'turkish': True,
         'ukrainin': True}

rec = Recognition('example_langs/', langs)

print(rec.detect('This is a Text I would like to recognize'))
```
### Cleaning up word lists
Word lists most be cleaned and lower-cased for good outputs.
```python
from recognition import lower_text

lower_text('example_langs/', 'english')
```
