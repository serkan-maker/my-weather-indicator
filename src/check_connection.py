#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of my-weather-indicator
#
# Copyright (c) 2012 Lorenzo Carbonell Cerezo <a.k.a. atareao>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import http.client
import requests
import socket
import time
import logging
import sys
import os

logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOGLEVEL", "DEBUG"))
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def check_connectivity():
    sockets = ['www.google.com',
               '216.58.192.142',
               'www.baidu.com']
    for asocket in sockets:
        if check_connectivity_with_httpconnection(asocket):
            return True
    for asocket in sockets:
        if check_connectivity_with_socket(asocket):
            return True
    urls = ['https://www.google.com',
            'http://www.google.com',
            'http://216.58.192.142',
            'http://www.baidu.com']
    for url in urls:
        if check_connectivity_with_reference(url):
            return True
    return False


def check_connectivity_with_httpconnection(reference):
    try:
        conn = http.client.HTTPConnection(reference)
        conn.close()
        logger.info(f"OK. Internet connection. HTTPConnection: {reference}")
        return True
    except Exception as ex:
        logger.error(f"No internet connection. HTTPConnection: {reference}")
        logger.error(ex)
    return False


def check_connectivity_with_socket(reference, port=80):
    try:
        conn = socket.create_connection((reference, port))
        conn.close()
        logger.info(f"OK. Internet connection. Socket: {reference}")
        return True
    except Exception as ex:
        logger.error(f"No internet connection. Socket: {reference}")
        logger.error(ex)
    return False


def check_connectivity_with_reference(reference, timeout=2):
    try:
        requests.get(reference, timeout=timeout, verify=False)
        logger.info(f"OK. Internet connection. Url: {reference}")
        return True
    except Exception as ex:
        logger.error(f"No internet connection. Url: {reference}")
        logger.error(ex)
    return False


if __name__ == '__main__':
    atime = time.time()
    logger.info(check_connectivity(), time.time() - atime)
