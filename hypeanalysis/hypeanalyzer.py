#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

sid = SentimentIntensityAnalyzer()


class CompoundSentiment(object):

    @staticmethod
    def trimmed_mean(data, m=2.):

        d = np.abs(data - np.median(data))
        mdev = np.median(d)
        s = d / mdev if mdev else 0.

        return np.mean(data[s < m])

    @staticmethod
    def get_compound(date, text):

        compound = np.zeros(len(text))
        for i, sentence in enumerate(text):
            compound[i] = sid.polarity_scores(sentence)["compound"]

        return {
            "date": date,
            "sentiment": CompoundSentiment().trimmed_mean(compound),
        }

    def get_sentiment(self, data):

        return json.dumps([
            self.get_compound(date, text) for date, text in data.items()
        ])


if __name__ == '__main__':

    print(CompoundSentiment().get_sentiment(dict(input())))
