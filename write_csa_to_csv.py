# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 2016

@author: skipi

write CVE database to CSV file

"""

#import requests
#import json
#import urllib
#import datetime
#import wget
#import get_cves


def write_csa_to_csv(csaEntry):
    date = str(datetime.date.today())
    print ('Writting CSA CSV file ...')
    if (csaEntry.ok):
        csaContent = json.loads(csaEntry.content)

        csvFile = open("./REPORTS/" + date + ".csv",'wb')
 
#        print "sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list"     
        csvFile.write("sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list")
    
        for line in csaContent["advisories"]:
            print ('Getting CSA XML description file for ' + line ['advisoryId'])
#            csaFile = wget.download(csaUrl)            
            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
            csaFile.write(requests.get(line["cvrfUrl"]).content)
            csaFile.close()
                    
            cve_list = ""
            for cve in line["cves"]:
                print ('ToDo: Download description for ' + cve + ' ...')
#                print get_cves.get_cve(cve)
                if cve_list == "":
                    cve_list = cve
                else:
                    cve_list = cve_list + ", " + cve
    
            report = line["sir"] + ";" + line["advisoryId"] + ";" + line["lastUpdated"] + ";" + line["fi

#            print report        
            csvFile.write("\n" + report)
            
        csvFile.close()

