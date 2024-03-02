from urllib.request import Request, urlopen
import ply.lex as lex
import ply.yacc as yacc
import GetURLIndia

def downloadwebpage(url,filename):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open(f'{filename}.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

###DEFINING TOKENS###
tokens = ('HTAG', 'CLOSEHTAG', 'START', 'END' , 'OPENTABLE', 'CLOSETABLE', 'CAPTION', 'ANCHORREF', 'CLOSEANCHORREF', 'EDITANCHOR', 'CLOSEEDITANCHOR', 'OPENP', 'CLOSEP', 'OPENLI', 'CLOSELI', 'OPENROW', 'CLOSEROW', 'OPENSTYLE', 'CLOSESTYLE', 'OPENTAG', 'CLOSETAG', 'OPENCLOSETAG', 'BREAK', 'CONTENT')
t_ignore = r' \t\n '

###############Tokenizer Rules################

def t_START(t):
    r'<span.class=\"mw\-headline\".id=\"(January|February|March|April|May|June|July|August|September|October|November|December)\">'
    return t

def t_END(t):
    r'<h2>'
    return t

def t_OPENTABLE(t):
    r'<table[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'<\/table[^>]*>'
    return t

def t_OPENP(t):
    r'<p>'
    return t

def t_CLOSEP(t):
    r'<\/p>'
    return t

def t_OPENLI(t):
    r'<li>'
    return t

def t_CLOSELI(t):
    r'<\/li>'
    return t

def CAPTION(t):
    r'\"Major.events.of.COVID\-19.pandemic.in.India.till.(January|February|March|April|May|June|July|August|September|October|November|December)\"'
    return t
    
def t_ANCHORREF(t):
    r'<sup.id=\"cite_ref[^>]*>'
    return t

def t_CLOSEANCHORREF(t):
    r'<\/sup>'
    return t

def t_EDITANCHOR(t):
    r'<span.class=\"mw\-editsection\-bracket\">'
    return t

def t_CLOSEEDITANCHOR(t):
    r'\]<\/span>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'<\/tr[^>]*>'
    return t

def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'<\/style[^>]*>'
    return t
  
def t_HTAG(t):
    r'<h[^>]*>'
    return t

def t_CLOSEHTAG(t):
    r'<\/h[^>]*>'
    return t

def t_CONTENT(t):
    r'[^<>"\'\n\t]+'
    return t

def t_BREAK(t):
    r'<br[^>]*>'
    return t

def t_OPENCLOSETAG(t):
    r'<img[^>]*>'
    return t

def t_OPENTAG(t):
    r'<(?!\/)[A-Za-z]+[^>]*>'
    return t

def t_CLOSETAG(t):
    r'<\/[A-Za-z]+[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : START skiptag'''
    
    p[0]=p[2]
    #print(p[1])
    print(p[0])

def p_skiptag(p):
    '''skiptag : OPENTABLE skiptag
               | CLOSETABLE skiptag
               | CAPTION skiptag
               | ANCHORREF skiptag
               | CLOSEANCHORREF skiptag
               | EDITANCHOR skiptag
               | CLOSEEDITANCHOR skiptag
               | OPENP skiptag
               | CLOSEP skiptag
               | OPENLI skiptag
               | CLOSELI skiptag
               | OPENROW skiptag
               | CLOSEROW skiptag
               | OPENSTYLE skiptag
               | CLOSESTYLE skiptag
               | OPENTAG skiptag
               | CLOSETAG skiptag
               | OPENCLOSETAG skiptag
               | BREAK skiptag
               | CONTENT skiptag
               | CLOSEHTAG skiptag
               | HTAG gettitle'''
    p[0]=p[2]
    #print(p[1])
    
def p_skiptag1(p):
    '''skiptag1 : OPENTABLE skiptag1
                | CLOSETABLE skiptag1
                | CAPTION skiptag1
                | ANCHORREF skiptag1
                | CLOSEANCHORREF skiptag1
                | EDITANCHOR skiptag1
                | CLOSEEDITANCHOR skiptag1
                | CLOSEP skiptag1
                | OPENLI skiptag1
                | CLOSELI skiptag1
                | OPENROW skiptag1
                | CLOSEROW skiptag1
                | OPENSTYLE skiptag1
                | CLOSESTYLE skiptag1
                | OPENTAG skiptag1
                | CLOSETAG skiptag1
                | OPENCLOSETAG skiptag1
                | BREAK skiptag1
                | CONTENT skiptag1
                | CLOSEHTAG skiptag1
                | HTAG gettitle
                | OPENP getpcontent'''
    if(p.slice[1].type=='HTAG'):
        p[0]='\n'+p[2]
    else:
        p[0]=p[2]
    #print(p[1])
              
def p_skipanchorrefp(p):
    '''skipanchorrefp : OPENTAG skipanchorrefp
                      | CLOSETAG skipanchorrefp
                      | CONTENT skipanchorrefp
                      | CLOSEANCHORREF'''
    #print(p[1])

def p_skipanchorrefli(p):
    '''skipanchorrefli : OPENTAG skipanchorrefli
                       | CLOSETAG skipanchorrefli
                       | CONTENT skipanchorrefli
                       | CLOSEANCHORREF getlicontent '''
    #print(p[1])
    p[0]=p[2]

def p_skipanchorreftb(p):
    '''skipanchorrefrw : OPENTAG skipanchorrefrw
                       | CLOSETAG skipanchorrefrw
                       | CONTENT skipanchorrefrw
                       | CLOSEANCHORREF getrowdata '''
    #print(p[1])
    p[0]=p[2]
    
def p_skipeditanchor(p):
    '''skipeditanchor : OPENTAG skipeditanchor
                      | CLOSETAG skipeditanchor
                      | CONTENT skipeditanchor
                      | EDITANCHOR skipeditanchor
                      | CLOSEEDITANCHOR'''
    #print(p[1])

def p_skipcaption(p):
    '''skipcaption : OPENTABLE skipcaption 
                   | CAPTION skipcaption
                   | ANCHORREF skipcaption
                   | EDITANCHOR skipcaption
                   | CLOSEEDITANCHOR skipcaption
                   | OPENP skipcaption
                   | CLOSEP skipcaption
                   | OPENLI skipcaption
                   | CLOSELI skipcaption
                   | OPENROW skipcaption
                   | CLOSEROW skipcaption
                   | OPENSTYLE skipcaption
                   | CLOSESTYLE skipcaption
                   | OPENTAG skipcaption
                   | CLOSETAG skipcaption
                   | OPENCLOSETAG skipcaption
                   | BREAK skipcaption
                   | CONTENT skipcaption
                   | HTAG skipcaption
                   | CLOSEHTAG skipcaption
                   | CLOSEANCHORREF skipcaption
                   | CLOSETABLE gettitle'''
    #print(p[1])
    p[0]=p[2]

def p_gettitle(p):
    '''gettitle : CLOSETABLE gettitle
                | CAPTION gettitle
                | CLOSEANCHORREF gettitle
                | EDITANCHOR skipeditanchor gettitle
                | ANCHORREF skipanchorrefp gettitle
                | CLOSEEDITANCHOR gettitle
                | CLOSEP gettitle
                | CLOSELI gettitle
                | OPENROW gettitle
                | CLOSEROW gettitle
                | OPENSTYLE gettitle
                | CLOSESTYLE gettitle
                | OPENTAG gettitle
                | CLOSETAG gettitle
                | OPENCLOSETAG gettitle
                | BREAK gettitle
                | CONTENT gettitle
                | HTAG gettitle
                | CLOSEHTAG gettitle
                | OPENP getpcontent
                | OPENTABLE gettablecontent
                | OPENLI getlicontent'''
    #print(p[1])
    if(len(p)==4):
        p[0]=p[3]
    elif(p.slice[1].type=='CONTENT'):
        p[0]=p[1]+p[2]
    elif(p.slice[1].type=='OPENP'):
        p[0]='\n'+p[2]
    elif(len(p)>2):
        p[0]=p[2]
    else:
        p[0]=""

def p_getpcontent(p):
    '''getpcontent : OPENTABLE getpcontent
                   | ANCHORREF skipanchorrefp getpcontent
                   | EDITANCHOR skipeditanchor getpcontent
                   | CLOSEEDITANCHOR getpcontent
                   | OPENSTYLE getpcontent
                   | CLOSESTYLE getpcontent
                   | OPENTAG getpcontent
                   | CLOSETAG getpcontent
                   | OPENCLOSETAG getpcontent
                   | BREAK getpcontent
                   | CONTENT getpcontent
                   | HTAG getpcontent
                   | CLOSEHTAG getpcontent
                   | CLOSEANCHORREF getpcontent
                   | CLOSEP getnext'''
    #print(p[1])
    if(len(p)==4):
        p[0]=p[3]
    elif(p.slice[1].type=='CONTENT'):
        p[0]=p[1]+' '+p[2]
    elif(len(p)>2):
        p[0]=p[2]
    else:
        p[0]=""
    
def p_getnext(p):
    '''getnext : END getnext1
               | skiptag1'''
    if(p.slice[1].type=='END'):
        p[0]="\n"+p[2]
    else:
        p[0]=p[1]

def p_getnext1(p):
    '''getnext1 : START skiptag
                | OPENTAG'''
    if(len(p)==2):
        p[0]=""
    else:
        p[0]=p[2]
        
def p_gettablecontent(p):
    '''gettablecontent : OPENTABLE gettablecontent
                       | OPENSTYLE gettablecontent
                       | CLOSESTYLE gettablecontent
                       | CAPTION skipcaption
                       | OPENTAG gettablecontent
                       | CLOSETAG gettablecontent
                       | OPENP gettablecontent
                       | CLOSEP gettablecontent
                       | OPENCLOSETAG gettablecontent
                       | BREAK gettablecontent
                       | CONTENT gettablecontent
                       | HTAG gettablecontent
                       | CLOSEHTAG gettablecontent
                       | CLOSEANCHORREF gettablecontent
                       | CLOSELI gettablecontent
                       | OPENROW getrowdata
                       | CLOSETABLE gettitle'''

def p_getrowdata(p):
    '''getrowdata : OPENTAG getrowdata
                  | CONTENT getrowdata
                  | CLOSETAG getrowdata
                  | OPENCLOSETAG getrowdata
                  | BREAK getrowdata
                  | HTAG getrowdata
                  | OPENSTYLE getrowdata
                  | CLOSESTYLE getrowdata
                  | ANCHORREF skipanchorrefrw
                  | CLOSEROW gettablecontent'''
    # #print(p[1])
    if(p.slice[1].type=='CONTENT'):
        print(p[1])
    
    
def p_getlicontent(p):
    '''getlicontent : OPENTABLE getlicontent
                    | ANCHORREF skipanchorrefli
                    | OPENSTYLE getlicontent
                    | CLOSESTYLE getlicontent
                    | OPENTAG getlicontent
                    | CLOSETAG getlicontent
                    | OPENP getlicontent
                    | CLOSEP getlicontent
                    | OPENCLOSETAG getlicontent
                    | BREAK getlicontent
                    | CONTENT getlicontent
                    | HTAG getlicontent
                    | CLOSEHTAG getlicontent
                    | CLOSEANCHORREF getlicontent
                    | CLOSELI gettitle'''
    # #print(p[1])
    if(p.slice[1].type=='CONTENT'):
        print(p[1])

def p_error(p):
    pass

urls=GetURLIndia.getUrlsIndia()
timelines=list(urls)
# for timeline in timelines:
timeline=timelines[0]
downloadwebpage(urls[timeline],timeline)
file_obj = open(f'{timeline}.html','r',encoding="utf-8")
data = file_obj.read()
lexer = lex.lex()
lexer.input(data)
# for tok in lexer:
#     print(tok)
parser = yacc.yacc()
parser.parse(data)