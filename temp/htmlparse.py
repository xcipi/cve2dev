from html.parser import HTMLParser
import wget
import re
import os
import requests

numSol = 10
startSol = 0


baseSolUrl = 'https://support.f5.com/kb/en-us/search.res.html?q=+inmeta:archived%3DArchived%2520documents%2520excluded&dnavs=inmeta:kb_doc_type%3DSecurity%2520Advisory+inmeta:archived%3DArchived%2520documents%2520excluded&filter=p&requiredfields=kb_doc_type:Security%2520Advisory.archived:Archived%2520documents%2520excluded'
#&num=100&start=0'

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
 
#    def handle_starttag(self, tag, attrs):
#        print(("### Encountered a start tag:"), tag)

#    def handle_endtag(self, tag):
#        print(("### Encountered an end tag :"), tag)

    def handle_data(self, data):
        f5UrlRegex = r"\n +"
        f5FileRegex = r"^(http)\:\/\/[a-zA-Z]{7}\.(f5)\.(com)\/(([a-zA-Z]|\d|\-)+\/)+"
        solNum = 0
        replace = ''
        a = ['support.f5.com', 'sol']
        
        if all(x in data for x in a):
            solNum+=1
            try:
                matchUrl = re.sub(f5UrlRegex, replace, data, 0)
                matchFile = re.sub(f5FileRegex, replace, matchUrl, 0) 
            except Exception as e:
                print(e)    
           
#            print ('### Po regexpe: ', matchUrl)
#            print ('### File:', matchFile)

            solFile = open('./SOLs/' + matchFile, 'wb')
            solFile.write(requests.get(matchUrl).content)
            solFile.close()
            
            print ('### Downloaded file: ', matchUrl)
#            print ('#########################')



def get_sol_links_file(baseUrl, num, start):
    solListUrl = baseUrl + '&num=' + str(num) + '&start=' + str(start)
    print ('### SOL number per page: ' + str(num) + ' and starts at ' + str(start))
#    print ('### SOL list URL is: ', solListUrl)

    try:
        print ('### Downloading file ', solListUrl)
        solList = requests.get(solListUrl)
    except Exception as e:
        print ('ERROR: ', e)
        
    print ('Writting SOL list file ... ' + str(start) + ' - ' + str(start+num))
    solListFile = open('./SOLs/solList' + str(start) + '.html', 'wb')
    solListFile.write(solList.content)
    solListFile.close()
    




for i in {1, 2, 999999}:
    try:
        get_sol_links_file(baseSolUrl,numSol,((startSol+numSol)*i))
    except Exception as e:
        print ('ERROR: ', e)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for file in os.listdir("./SOLs"):
    if file.startswith("solList"):
        print('### Detected file: ' + file)
        try:
            print ('### Parsing file: ', file)
            f = open('./SOLs/' + file,'r')
            parser.feed(f.read())
        except Exception as e:
            print (e)
