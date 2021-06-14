#!/usr/bin/python3
"""
Unittests for Meraki SDK
Written by Gustav Larsson
"""

import os
from meraki_sdk import MerakiSDK

sdk_instance = MerakiSDK(token=os.environ["MERAKI_API_TOKEN"], verify=False)

def test_key_exist():
    """ Testing so a key is exported """

    assert os.environ["MERAKI_API_TOKEN"]

def test_valid_key():
    """ Testing so exported key is valid """

    response = sdk_instance.get_orgs()

    assert response.status_code != 401
