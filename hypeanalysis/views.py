#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import render_template
import numpy as np

from config import app
from price_is_right import come_on_down


@app.route('/')
def home():
    """Returns home"""

    with open('hypeanalysis/data.json', 'r') as data_j:
        data = data_j.read()

    data = json.loads(data)[:100]

    for i, j in enumerate(data):
        data[i]["price"] = come_on_down(j["date"])

    y2 = [i["price"] for i in data]
    alpha = np.mean(y2)
    x = [i["date"] for i in data]
    y1 = [i["sentiment"] + alpha for i in data]

    return render_template('chart.html', x=x, y1=y1, y2=y2)

# no toda via
# @app.errorhandler(404)
# def page_not_found(e):
#     """Handles 404 error"""
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def server_error(e):
#     """Handles 500 error"""
#     return render_template('500.html'), 500
