# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:45:54 2016

@author: skipi

get CVE database from Cisco API

"""

import requests
import json
import urllib
import datetime

def get_cves(ciscoToken):

    date = str(datetime.date.today())

    ciscoTokenHeader = "Bearer " + ciscoToken
    advUrl = 'https://api.cisco.com/security/advisories/cvrf/year/2016'

    advHeaders = {'Accept': 'application/json', 'Authorization': ciscoTokenHeader}

    advResponse = requests.get(advUrl, headers = advHeaders)

    if (advResponse.ok):
        advCritical = json.loads(advResponse.content)

        csvFile = open("./REPORTS/" + date + ".csv",'wb')
        
#        print "sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list"     
        csvFile.write("sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list")
        
        for line in advCritical["advisories"]:
        
            cve_list = ""
            for cve in line["cves"]:
                if cve_list == "":
                    cve_list = cve
                else:
                    cve_list = cve_list + ", " + cve
        
            report = line["sir"] + ";" + line["advisoryId"] + ";" + line["lastUpdated"] + ";" + line["firstPublished"] + ";" + cve_list + ";" + line["cvrfUrl"]

#            print report        
            csvFile.write("\n" + report)
            
        csvFile.close()
            
#	FUNKCNY download CSA files - NEMAZAT !!!
#            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
#            csaFile.write(requests.get(line["cvrfUrl"]).content)
#            csaFile.close()
            
get_cves("ZxpN9LrcHeC4WNtILZbunqYKYKo0")
