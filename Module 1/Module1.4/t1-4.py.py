import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import re

td_count = 0
continent_count = 1

tokens = ('BEGIN', 'OPENROW', 'CLOSEROW', 'OPENHEADER', 'OPENTABLE',
          'CLOSEHEADER', 'PATTERN', 'CONTENT', 'OPENDATA', 'CLOSEDATA', 'THEADOPEN', 'THEADCLOSE', 'GARBAGE')
t_ignore = '\t '

def t_BEGIN(t):
    r'<table.id="main_table_countries_yesterday".class="table.table-bordered.table-hover.main_table_countries".style="width:100%;margin-top:.0px.!important;display:none;">'
    print("begin")
    return t

def t_OPENTABLE(t):
    r'<tbody>'
    return t

def t_THEADOPEN(t):
    r'<thead>'
    return t

def t_THEADCLOSE(t):
    r'</thead>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9,+\(\)\-–\/\.:\' ]+'
    return t

def t_PATTERN(t):
    r'(&\#160;)|(&amp;)|(&\#91;[0-9]&\#93;)|\#'
    return t

def t_GARBAGE(t):
    r'(<[^>]*>)|(<\/[^>]*>)|(<[^\/>]*\/>)|<![^>]>'
    return t

def t_error(t):
    t.lexer.skip(1)

def p_start(p):
    ''' 
    start : BEGIN THEADOPEN skiptag THEADCLOSE OPENTABLE getdata
    '''

def p_skiptag(p):
    '''
    skiptag : GARBAGE skiptag 
            | PATTERN skiptag
            | CONTENT skiptag
            | OPENROW skiptag
            | CLOSEROW skiptag
            | OPENDATA skiptag
            | CLOSEDATA skiptag
            | OPENHEADER skiptag
            | CLOSEHEADER skiptag
            |
    '''
def p_getdata(p):
    '''
    getdata : OPENROW handledata CLOSEROW getdata
            | 
    '''

def p_handledata(p):
    '''
    handledata : onlydata handledata
               | 
    '''
def p_comment(p):
    '''
    comment : GARBAGE
            | 
    '''
def p_onlydata(p):
    '''
    onlydata : OPENDATA CLOSEDATA comment 
             | OPENDATA GARBAGE CONTENT GARBAGE CLOSEDATA comment
             | OPENDATA GARBAGE GARBAGE CLOSEDATA comment
             | OPENDATA CONTENT CLOSEDATA comment 
    '''
    global td_count,continent_count
    td_count = td_count+1
    if continent_count != 7 and continent_count <= 8:
        with open('continents.txt', 'a') as the_file:
            if td_count == 2:
                if p.slice[3].type != 'CONTENT':
                    the_file.write(f'Continent: {p[2]}\n') #in case of world
                else:
                    the_file.write(f'Continent: {p[3]}\n')
            elif td_count == 3 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Total Cases: {p[2]}\n')
            elif td_count == 4 and p.slice[2].type == 'CONTENT':
                the_file.write(f'New Cases: {p[2]}\n')
            elif td_count == 5 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Total Deaths: {p[2]}\n')
            elif td_count == 6 and p.slice[2].type == 'CONTENT':
                the_file.write(f'New Deaths: {p[2]}\n')
            elif td_count == 7 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Total Recovered: {p[2]}\n')
            elif td_count == 8 and p.slice[2].type == 'CONTENT':
                the_file.write(f'New Recovered: {p[2]}\n')
            elif td_count == 9 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Active Cases: {p[2]}\n')
            elif td_count == 12 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Deaths Million: {p[2]}\n')
            elif td_count == 13 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Total Tests: {p[2]}\n')
            elif td_count == 14 and p.slice[2].type == 'CONTENT':
                the_file.write(f'Tests Million: {p[2]}\n')
            if td_count == 22:
                the_file.write("==============================================\n")
                continent_count = continent_count+1
                td_count = 0
    else:
        if td_count == 22:
            continent_count = continent_count+1
            td_count = 0

def p_error(p):
    
    if p:
        print("Syntax error at '%s'" % p)
    else:
        print("Syntax error at EOF")
    pass

def main():
    # req = Request('https://www.worldometers.info/coronavirus/',headers ={'User-Agent':'Mozilla/5.0'})
    # webpage = urlopen(req).read()
    # mydata = webpage.decode("utf8")
    # f=open('webpage.html','w',encoding="utf-8")
    # f.write(mydata)
    # f.close
    file_obj = open('webpage.html','r',encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    print("lex completed")
    # for tok in lexer:
    #     print(tok)
    parser = yacc.yacc()
    parser.parse(data)
if __name__ == '__main__':
    main()