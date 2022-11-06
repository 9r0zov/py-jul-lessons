import re


def count_vowel(string):
    return len(re.findall("[aeoiyu]", string.lower()))
