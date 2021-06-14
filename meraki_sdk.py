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
        self.headers = { "X-Cisco-Meraki-API-Key": token }
        self.verify = verify

        if verify is False:
            requests.urllib3.disable_warnings()

    def _req(self, resource, payload=None, method="GET"):
        """ Temp main-function """

        url = f"{self.base_url}{resource}"
        response = requests.request(url=url,
                                    method=method,
                                    data=payload,
                                    headers=self.headers,
                                    verify=self.verify)

        if response.status_code in [200, 201, 204]:

            jresp = response.json()

        else:
            jresp = f"Error with request: {response.status_code}"

        return jresp

    def get_orgs(self):
        """ Return available orgs """
        response = self._req("/organizations")

        return response

    def get_networks(self):
        """ Return available networks in an org """
        response = self._req("/networks")

        return response

if __name__ == "__main__":

    test = MerakiSDK(token=os.environ["MERAKI_API_TOKEN"])

    print(test.get_orgs())
