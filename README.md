# LangDetection
## Table of Contents

1. [About The Project](#about-the-project)
   - [Built With](#built-with)
2. [Examples](#examples)
   - [Progress Bar Class](#progress-bar-class)
   - [Advanced Status Window Class](#advanced-status-window-class)

## About The Project

We needed a language detection which recognizes a language not using ai, but on the words matched a certain language.

### Built With

* [Python 3.9](www.python.org)

## Examples

Some examples on how I am using the code.

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

rec = Recognition(langs)

print(rec.detect('Ich mag ganz gerne kekse. Denn Kekse sind sehr lecker'))
```
