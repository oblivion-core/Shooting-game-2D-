#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TP N1 - Part 1 : corrected version of the buggy text-processing program
import re
import sys


def clean_text(text):
    """Remove punctuation from a text"""
    punct = '+.*/?,;\'#!:"()'
    for p in punct:
        text = text.replace(p, "")
    return text


def tokenize(text):
    """Convert text into tokens, return a list of tokens (words)"""
    return text.split()


def tokenize2(text):
    """Same as tokenize, using a regular expression"""
    spaces = r"\s+"
    words = re.split(spaces, text)
    return words


def word_freq(words):
    """Count words and return a dictionary of words with their occurrences"""
    index = {}
    for w in words:
        if w in index:
            index[w] += 1
        else:
            index[w] = 1
    return index


def most_common_word(words_freq_table):
    """Return the most frequent word of a frequency dictionary"""
    frequent = None
    frequency = 0
    for word in words_freq_table:
        if words_freq_table[word] > frequency:
            frequent = word
            frequency = words_freq_table[word]
    return frequent


def read_file(filename):
    """Read a text from a file"""
    try:
        with open(filename, encoding="utf-8") as fl:
            text = fl.read()
    except OSError:
        print("Can't open file", filename)
        sys.exit()
    return text


def main(args):
    text = """Surprise steepest recurred landlord mr wandered amounted of.
    Continuing devonshire but considered its. Rose past oh shew roof
    is song neat. Do depend better praise do friend garden an wonder to.
    Intention age nay otherwise but breakfast.
    Around garden beyond to extent by.
    """
    text = clean_text(text)
    print(text)
    words = tokenize(text)
    print(words)
    words_nb = word_freq(words)
    print(words_nb)

    data = read_file("data.txt")
    print(data)
    text = clean_text(data).lower()
    words = tokenize2(text.strip())
    print(words)
    word_freq_table = word_freq(words)
    print(word_freq_table)
    freqw = most_common_word(word_freq_table)
    print("most frequent word is", freqw, word_freq_table[freqw])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
