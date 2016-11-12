# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get CVE database from Cisco API

"""

import requests
import json
import datetime
import write_csa

def get_csas(ciscoToken,csaParam,csaParamValue,bendType):
    """
    get_csas
    
    ciscoToken - auth token from Cisco API Oauth
    csaParam - search by what
    csaParamValue - search parameter value
    
    """

    date = str(datetime.date.today())

    ciscoTokenHeader = "Bearer " + ciscoToken

    csaBaseUrl = 'https://api.cisco.com/security'

    csaUrlY = '/advisories/cvrf/year/' # <YYYY - year>
    csaUrlAll = '/advisories/cvrf/all'
    csaUrlCve = '/advisories/cvrf/cve/' # <CVEID>
    csaUrlAdv = '/advisories/cvrf/advisory/' # <advisoryId>
    csaUrlSev = '/advisories/cvrf/severity/' # <critical|high|medium|low>
    csaUrlLatest = '/advisories/cvrf/latest/' # <number of latest csas>

    if csaParam == 'YEAR':
       csaUrl = csaBaseUrl + csaUrlY + csaParamValue
    elif csaParam == 'ALL':
       csaUrl = csaBaseUrl + csaUrlAll + csaParamValue
    elif csaParam == 'CVE':
       csaUrl = csaBaseUrl + csaUrlCve + csaParamValue
    elif csaParam == 'ADVIS':
       csaUrl = csaBaseUrl + csaUrlAdv + csaParamValue
    elif csaParam == 'SEV':
       csaUrl = csaBaseUrl + csaUrlSev + csaParamValue
    elif csaParam == 'LATEST':
       csaUrl = csaBaseUrl + csaUrlLatest + csaParamValue

    print ('Getting CSA JSON ... from ' + csaUrl)
    csaHeaders = {'Accept': 'application/json', 'Authorization': ciscoTokenHeader}

    csaResponse = requests.get(csaUrl, headers = csaHeaders)


    if bendType == 'DB':
        write_csa.write_csa_to_db(csaResponse)
    elif bendType == 'CSV':
        write_csa.write_csa_to_csv(csaResponse)
    

#	FUNKCNY download CSA files - NEMAZAT !!!

#            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
#            csaFile.write(requests.get(line["cvrfUrl"]).content)
#            csaFile.close()
            
#get_csas('xxxxxxxxxxxx')
