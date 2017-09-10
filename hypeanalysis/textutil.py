#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from string import punctuation

from dateutil import parser as date_parser
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()


def penn_to_wn(tag):

    if tag in ("JJ", "JJR", "JJS"):
        return wn.ADJ

    elif tag in ("RB", "RBR", "RBS"):
        return wn.ADV

    elif tag in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
        return wn.VERB

    return wn.NOUN


def normalize_text(content):

    norm_text = content.encode("ascii", "ignore").lower()

    for punc in punctuation:
        norm_text = norm_text.replace(punc, " ")

    words = norm_text.split()

    words = [word for word in words if not word.isdigit()]
    words = pos_tag(words)
    words = [
        lemma.lemmatize(word[0], penn_to_wn(word[-1]))
        for word in words
    ]

    for i, word in enumerate(words):
        if any(p in word for p in ("(", ")")):
            words[i] = word[word.find("(") + 1:word.find(")")]

    time_filtered = []

    for word in words:
        try:
            if date_parser.parse(word):
                pass

        except (TypeError, ValueError):
            time_filtered.append(word)

    return " ".join(filter(None, time_filtered))
