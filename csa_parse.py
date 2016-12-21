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
            if child.attrib:
                tag = child.tag
                attr = child.attrib
                text = child.text
#                print ('TAG: ',chop_ns_prefix(tag),"ATTRIB: ", attr,"TEXT: ", text)
                #print (bcolors.HEADER,'child> ',bcolors.ENDC, strip_char(chop_ns_prefix(child.tag),r"\s+"),bcolors.HEADER,', attrib> ', bcolors.ENDC,child.attrib, bcolors.HEADER, ' text> ',bcolors.ENDC, strip_char(child.text,r"\n+"),'\n')

# instancii classu CSA (self) sa prida atribut strip_char(chop_ns_prefix(child.tag),r"\s+") - o whitespaces a namespace stripnuty child.tag, a jeho hodnota sa nastavi na child.attrib
# treba vymysliet, ako to zoradit podla Ordinar a ako k tomu pridat text

                setattr(self, strip_char(chop_ns_prefix(child.tag),r"\s+"), attr)
                if strip_char(text, r"\s+"):
                    setattr(self, strip_char(chop_ns_prefix(child.tag),r"\s+")+'.text', strip_char(text,r"\n+"))
            self.parse(child) 

def print_node(node, strip_ns):
    """
    Print each XML node

    node: the ElementTree node to be printed
    strip_ns: boolean that when true indicates the namespace prefix will be chomped
    f: the file to print to (default is stdout)
    """
    if node.tag:
        print ("TAG: [%s]" %(chop_ns_prefix(node.tag) if strip_ns else node.tag))
    if node.attrib:
        for key in node.attrib:
            print ("ATTRIBS: (%s: %s)" %(key, node.attrib[key]))
    if node.text:
        print ("TEXT: \"", node.text.strip(), "\"")


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

    CvrfTree = etree.parse('CSAs/cisco-sa-20161026-linux_cvrf.xml')
    CvrfRoot = CvrfTree.getroot()

#    parse_cvrf_recursive(CvrfRoot,'',0,chop_ns_prefix(CvrfRoot.tag))
    
    x = CSA()
    x.parse(CvrfRoot)


#    print (bcolors.OKBLUE, 'dist > ',bcolors.ENDC, x.__dict__)

    attrs = vars(x)
#    for polozka in attrs.items():
#        if polozka:
    print('=\n======================================\n'.join("%s> %s" % item for item in attrs.items()))

main()
