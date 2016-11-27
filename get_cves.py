from ares import CVESearch
import requests 
import json

def get_cve(cveid):

    cveBaseUrl = "http://192.168.56.101:5000/api/cve/"
    cveUrl = cveBaseUrl + cveid
    print ('### Zhanam ' + cveid + ' na URL ' + cveUrl + ' ...')

#    cve = ./../cve-search/bin/search.py -c cveid
    #CVE-2016-4429

    try:
        cveResponse = requests.get(cveUrl)
    except Exception as e:
        print (e)
        
    #, headers = csaHeaders)

#    CVESearch()

    if (cveResponse.ok):
        cveContent = json.loads(cveResponse.content)            
        for line in cveContent["Modified"]:
           print ('- Getting CSA XML description file for ' + line["Modified"])
#        print (cveResponse)
#        print (cveContent)

#    print (cveResponse)
#    .search(cveid))

get_cve('CVE-2016-4429')
