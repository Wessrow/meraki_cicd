#!/usr/bin/python3
"""
MerakiSDK
Written by Gustav Larsson
"""

import os
import requests

class MerakiSDK:
    """
    Class to handle interactions with Meraki API
    """
    def __init__(self, token, verify=False):
        """ Initial constructor for the class """
        self.base_url = "https://api.meraki.com/api/v1"
        self.token = token

        if verify is False:
            self.verify = verify
            requests.urllib3.disable_warnings()

    def _req(self, resource, method="GET"):
        """ Temp main-function """

        url = f"{self.base_url}{resource}"
        response = requests.request(method=method, url=url)
        return response

    def get_orgs(self):
        """ Return available orgs """
        response = self._req(self, "/organizations").json()

        return response

    def get_networks(self):
        """ Return available networks in an org """
        response = self._req(self, "/networks").json()

        return response

if __name__ == "__main__":

    print(os.environ["MERAKI_API_TOKEN"])
