import os
import subprocess
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))

# DEFINING TOKENS
tokens = ('BEGINTABLE', 'ENDDATA',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN','CLOSESPAN', 
'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','IGNOREDATA')
import os
t_ignore = '\t'

links = {}

# Tokenizer Rules
def t_BEGINTABLE(t):
     r'The.following.are.the.timelines.of.the.COVID-19.pandemic.respectively.in:.'
     return t

def t_ENDDATA(t):
     r'<dl><dt>Responses</dt></dl>'
     return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'

def t_OPENROW(t):
    r'<tr[^>]*>'

def t_CLOSEROW(t):
    r'</tr[^>]*>'

def t_OPENHEADER(t):
    r'<th[^>]*>'

def t_CLOSEHEADER(t):
    r'</th[^>]*>'

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t


def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'

def t_CLOSESTYLE(t):
    r'</style[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_GARBAGE(t):
    r'<[^>]*>'

def t_CLOSEHREF(t):
    r'</a[^>]*>'

def t_OPENDATA(t):
    r'<td[^>]*>'

def t_CLOSEDATA(t):
    r'</td[^>]*>'

def t_IGNOREDATA(t):
    r'&nbsp; | (160;)'

def t_CONTENT(t):
    r'[A-Za-z0-9, ()–]+'
    return t


def t_error(t):
    t.lexer.skip(1)

# GRAMMAR RULES
def p_start(p):
    '''start : table'''
    # p[0] = p[1]

    


def p_links(p):
    '''links : OPENHREF CONTENT links 
             | CONTENT links
             | '''
    if len(p) ==4:
        p[0] = p[1] + p[3]
        global links
        links[p[2]] = p[0]
        # print(p[0])
        # print(p[2])
    else: 
        p[0]=''
    # print(p[1])
def printoutput():
    # links = ["https://en.wikipedia.org" + element.split('"')[1] for element in links]
    # for link in links:
    #     print(link)

    # names = [element.split("https://en.wikipedia.org//wiki/")[1] for element in links]
    # print(names)
    links_dict = {}

    for key, value in links.items():
        link = "https://en.wikipedia.org" + value.split('"')[1]
        links_dict[key] = link
    query = sys.argv[1]
    # print(links_dict)
    
    # name = link.split("https://en.wikipedia.org//wiki/")[1]
    req = Request(links_dict[query],headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('news.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
    # subprocess.run(["python", os.path.join(current_directory, "Ta2.py")])
    subprocess.run(["python3", os.path.join(current_directory, "getNews.py"), query])
        
def p_table(p):
    '''table : BEGINTABLE  links ENDDATA'''


def p_empty(p):
    '''empty : '''
    pass


def p_error(p):
    pass
#########DRIVER FUNCTION#######
def main():
    file_obj= open('Timeline of the COVID-19 pandemic.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # for tok in lexer:
    #     print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    printoutput()
    # print(links)
    
    

if __name__ == '__main__':
    main()