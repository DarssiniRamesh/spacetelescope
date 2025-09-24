#! /usr/bin/env python

"""Script that can be used to query websites used by JWQL, and return whether or not the
websites are reachable (alive).

Authors
-------

    - Brian York

Use
---

    This module is called as an independent script.


Dependencies
------------
    The user must have a configuration file named ``config.json``
    placed in the ``jwql`` directory.
"""

import logging
import requests

from jwql.utils.constants import URLS
from jwql.utils.logging_functions import log_info, log_fail

@log_info
@log_fail
def check_web_service(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout for the request
        if response.status_code == 200:
            message = f"Service at {url} is alive. Status code: {response.status_code}"
            logging.info(message)
            return True
        else:
            message = f"Service at {url} returned non-200 status: {response.status_code}"
            logging.warning(message)
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to connect to {url}: {e}")
        return False

if __name__ == "__main__":
    for url_name in URLS:
        if check_web_service(URLS[url_name]):
            logging.info(f"URL {url_name} passed status check")
        else:
            logging.warning(f"URL {url_name} failed status check")
