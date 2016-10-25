# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get CVE database from Cisco API Oauth2 

"""

import requests
import json
from pprint import pprint
import get_token
import get_cves

clientID = 'zetgk3mrfy58nwvbe239tqtr'
clientSecret = 'JkSydPCAnS28M82dKXG94RfY'

ciscoToken = get_token.get_token(clientID, clientSecret)

get_cves.get_cves(ciscoToken)
        