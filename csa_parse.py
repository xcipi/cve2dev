from lxml import etree
import re

class CSA:
    ''' 
        CSA class - define my CSA structure to save into DB
    '''
    test = "testCSA"
    pokus = "pokusCSA"

    DocumentTitle = ''
    DocumentType = ''
    ID = ''
    Status = ''
    InitialReleaseDate = ''
    CurrentReleaseDate = ''


    def parse (self,element):
        for child in element:
            attr = ''
#        if (order == 0):
            if child.attrib:
                attr = child.attrib
                print (bcolors.HEADER,'child> ',bcolors.ENDC, strip_char(chop_ns_prefix(child.tag),r"\s+"),bcolors.HEADER,', attrib> ', bcolors.ENDC,child.attrib, bcolors.HEADER, ' text> ',bcolors.ENDC, strip_char(child.text,r"\n+"),'\n')

# instancii classu CSA (self) sa prida atribut strip_char(chop_ns_prefix(child.tag),r"\s+") - o whitespaces a namespace stripnuty child.tag, a jeho hodnota sa nastavi na child.attrib
# treba vymysliet, ako to zoradit podla Ordinar a ako k tomu pridat text

                setattr(self, strip_char(chop_ns_prefix(child.tag),r"\s+"), child.attrib)
#                setattr(self, strip_char(chop_ns_prefix(child.tag),r"\s+") + '.text', child.text)
            self.parse(child) 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse_cvrf_recursive(element,precede,order,precedessor):
    '''
        parse CVRF XML recursively and return values
    '''

#    precede = precede + '\t'

    for child in element:
        attr = ''
#        if (order == 0):
        if child.attrib:
            attr = child.attrib


def chop_ns_prefix(element):
    """
    Return the element of a fully qualified namespace URI

    element: a fully qualified ET element tag
    """
    
    return element[element.rindex("}") + 1:]

def strip_char(string,to_strip):
    
    regex = r"\s+"
    subst = ""
    result = re.sub(to_strip, subst, string, 0)
    if result:
        return (result)

def main():
    
    print ('+++ ENTERING CVRF PARSING STAGE IN CSA_PARSE ... ')

    CvrfTree = etree.parse('CSAs/cisco-sa-20160927-openssl_cvrf.xml')
    CvrfRoot = CvrfTree.getroot()

    #parse_cvrf_recursive(CvrfRoot,'',0,chop_ns_prefix(CvrfRoot.tag))
    
    test1 = 'sdsdcsd cd sdc cdsd	kl	jkh'
    test2 = 'sddsf    fgsdgdgf	    	  fgasdfss	'
    
    print(strip_char(test1,r"\s+"))
    print(strip_char(test2,r"\s+"))    
    
    x = CSA()
    x.parse(CvrfRoot)

#    print (x)
    
    print (bcolors.OKBLUE, 'dist > ',bcolors.ENDC, x.__dict__)
    print('DocumentPublisher> ', x.DocumentPublisher)
    print('Vulnerability > ', x.Vulnerability)

main()
