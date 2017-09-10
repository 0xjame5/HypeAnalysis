#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
"""

Example:

https://min-api.cryptocompare.com/data/pricehistorical?fsym=ETH&tsyms=BTC,USD,EUR&ts=1452680400&extraParams=your_app_name
                                 data/pricehistorical/fsym=ETH&tsyms=BTC,USD,EUR&ts=1452680400&extraParams=your_app_name
"""


def come_on_down(ts):

    BASE_URL = "https://min-api.cryptocompare.com/data"
    TYPE = "pricehistorical"

    url = "{0}/{1}".format(BASE_URL, TYPE)

    fsym = "BTC"
    tsyms = "USD"
    extraParams = "your_app_name"

    added = "fsym={0}&tsyms={1}&ts={2}&extraParams={3}".format(
        fsym, tsyms, ts, extraParams)

    final_url = "{0}?{1}".format(url, added)

    response = requests.get(url=final_url).text  # .decode('utf-8')
    response = json.loads(response)["BTC"]["USD"]

    return response
