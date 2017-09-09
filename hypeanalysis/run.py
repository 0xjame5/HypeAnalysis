#!/usr/bin/env python
# -*- coding: utf-8 -*-

from views import app


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        add_help=False
    )
    # positional arguments
    parser.add_argument('port')

    # parse arguments to pass into function
    args = parser.parse_args()
    app.run(port=int(args.port))
