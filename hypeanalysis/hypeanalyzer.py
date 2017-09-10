#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import time

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
START_TIME = "Sat Sep 09 19:25:11 +0000 2017"
END_TIME = "Sat Sep 09 19:27:03 +0000 2017"


def get_date(date_str):

    time_struct = time.strptime(date_str, "%a %b %d %H:%M:%S +0000 %Y")
    date = datetime.fromtimestamp(time.mktime(time_struct))

    return date


def twitter_time_to_epoch_time(date_str):

    return get_date(date_str).strftime('%s')


data = {}

with open("file_of_json.txt") as output_file:
    for i, line in enumerate(output_file):
        line = dict(json.loads(line))
        data[twitter_time_to_epoch_time(line["created_at"])] = line["text"]

data = [
    {
        "date": date,
        "sentiment": sid.polarity_scores(text)["compound"],
    } for date, text in data.items()
]

data = sorted(data, key=lambda x: x["date"])
print(data)
