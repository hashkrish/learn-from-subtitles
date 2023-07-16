import MeCab
from pykakasi import kakasi


def tokenize_japanese_text(text):
    tagger = MeCab.Tagger()
    result = tagger.parse(text)
    lines = result.split("\n")
    tokens = []
    for line in lines[:-2]:
        surface = line.split("\t")[0]
        tokens.append(surface)
    return tokens


def get_japanese_pronounciation(text):
    return kakasi().convert(text).pop()["hira"]
