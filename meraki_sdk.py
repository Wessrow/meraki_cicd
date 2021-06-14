#!/usr/bin/python3
"""
MerakiSDK
Written by Gustav Larsson
"""

import os

class MerakiSDK:
    """
    Class to handle interactions with Meraki API
    """
    def __init__(self, token):
        """ Initial constructor for the class """
        self.token = token

    def _req(self):
        """ Temp main-function"""
        return "hello world"

if __name__ == "__main__":

    token = os.environ["TESTVAR"]

    print(token)
