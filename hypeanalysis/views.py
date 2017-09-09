#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from config import app


@app.route('/')
def home():
    """Returns home"""
    return render_template('index.html')


# no toda via
# @app.errorhandler(404)
# def page_not_found(e):
#     """Handles 404 error"""
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def server_error(e):
#     """Handles 500 error"""
#     return render_template('500.html'), 500
