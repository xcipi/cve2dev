# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 2016

@author: skipi

write CVE database to CSV file

"""

import requests
import json
import datetime
from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB

client = MongoClient('localhost:27017')
db = client.CSAs
date = str(datetime.date.today())

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
    
            report = line["sir"] + ";" + line["advisoryId"] + ";" + line["lastUpdated"] + ";" + line["firstPublished"] + ";" + cve_list + ";" + line["cvrfUrl"]

#            print report        
            csvFile.write("\n" + report)
            
        csvFile.close()


# Function to insert data record into mongo db
def insert_csa(csaRecord,csaCveList):
    try:
        db.csas.insert_one(
            {
# sir;cvrfUrl;lastUpdated;firstPublished;advisoryId;CVE list
                "csaSir": csaRecord['sir'],
                "csaCvrfUrl": csaRecord['cvrfUrl'],                
                "csaLastUpdated": csaRecord['lastUpdated'], 
                "csaFirstPublished": csaRecord['firstPublished'],                
                "csaAdvisoryId": csaRecord['advisoryId'], 
                "csaCveList": csaCveList,                
            })
        print ('- Data inserted successfully ...')
    except Exception as e:  
        print ('INSERT ERROR')
        print (e)

# function to read ALL records from mongo db    
def read_csadb():
    try:
#        print (db.find_one())
        csaCol = db.csas.find()
        print ('\nAll data from CSA Database \n', db)
        for csa in csaCol:
            print (csa)
    except Exception as e:         
        print ('READ ERROR')
        print (e)

## function to read LAST INSERTED record from mongo db    
def read_lastcsa(csaRecord):
    csa = db.CSAs
    search = csaRecord['advisoryId']
    try:
        print ('- Reading ID ' + search + '\n')
        csa.find_one({"advisoryId": search})
    except Exception as e:         
        print ('READ ERROR')
        print (e)


# Function to delete record from mongo db
def deleteAnyInDb():
    try:
        csaCol = db.CSAs.find()

        for csa in csaCol:
            print ('Deleting ' + csa['advisoryId'])
            csa.deleteOne({'advisoryId': csa['advisoryId']})
#        criteria = input('\nEnter employee id to delete\n')
#        db.csas.delete_many({"advisoryId":criteria})
        print ('- Deletion of ' + csa['advisoryId']+ ' successful ...')

    except Exception as e:
        print ('DELETE ERROR')
        print (e)

# Function to drop database
def drop_db(db):
    try:
        db.drop()
        print ('- Databae DROPed ...')
    except Exception as e:
        print ('DROP DB ERROR')
        print (e)
        
        
def write_csa_to_db(csaEntry):
#    print ('Writting CSA CSV file to DB: ' + {{db}} + '...')
    if (csaEntry.ok):
        print (client)
        csaContent = json.loads(csaEntry.content)

        for line in csaContent["advisories"]:
            print ('- Getting CSA XML description file for ' + line ['advisoryId'] + '...')
#            csaFile = wget.download(csaUrl)            
            csaFile = open("./CSAs/" + line["advisoryId"] + ".xml",'wb')
            csaFile.write(requests.get(line["cvrfUrl"]).content)
            csaFile.close()
                    
            cve_list = ""
            for cve in line["cves"]:
                print '--- ToDo: Download description for ' + cve + ' ...'
#                print get_cves.get.cve(cve)
                if cve_list == "":
                    cve_list = cve
                else:
                    cve_list = cve_list + ", " + cve
        
            insert_csa(line,cve_list)
#            read_lastcsa(line)    
            read_csadb()
             
#            deleteAnyInDb()
                        