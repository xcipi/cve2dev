from html.parser import HTMLParser
import re
import os

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    write_flag = 0
    print (write_flag)
    def handle_starttag(self, tag, attrs):
#        write_flag = 0
        print("### Encountered a start tag: " + tag)
#D       for i in attrs:
#            if i[0] == ""
#            print ('# ATTR: ', i)


    def handle_endtag(self, tag):
        print(("### Encountered an end tag: "), tag)

    def handle_data(self, data):
            print ('### Encountered an data: ', data)
    write_flag = write_flag + 1
    print ('write flag: ',write_flag)


    def handle_comment(self, data):
        print ("Comment  :", data)

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print ("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print ("Num ent  :", c)

    def handle_decl(self, data):
        print ("Decl     :", data)
        
        
        
        
parser = MyHTMLParser()

f = open('./SOLs/sol05200155.html' ,'r')
parser.feed(f.read())


'''
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
'''