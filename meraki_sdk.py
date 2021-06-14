#!/usr/bin/python3
"""
MerakiSDK
Written by Gustav Larsson
"""

import os
import json
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

        if response.status_code in [400, 401, 403, 404]:

            return f"Error with request: {response.status_code}"

        return response

    def get_orgs(self):
        """ Return available orgs """
        response = self._req("/organizations")

        return response

    def get_org_networks(self, org_id):
        """ Return available networks in an org """
        response = self._req(f"/organizations/{org_id}/networks")

        return response

    def get_network_devices(self, network_id):
        """ Return devices in a network """
        response = self._req(f"/networks/{network_id}/devices")

        return response

if __name__ == "__main__":

    test = MerakiSDK(token=os.environ["MERAKI_API_TOKEN"])

    jresp = test.get_orgs().json()
    print(json.dumps(jresp, indent=2))
    #print(json.dumps(test.get_org_networks(865776), indent=2))
    #print(json.dumps(test.get_network_devices("L_575334852396597361"), indent=2))
