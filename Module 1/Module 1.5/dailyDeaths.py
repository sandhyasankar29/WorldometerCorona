import ply.lex as lex
import ply.yacc as yacc

env={}
###DEFINING TOKENS###
tokens = ('START','NAME','OPENDATA','CLOSEDATA','STYLE','CONTENT')
t_ignore = r' \t\n '

###############Tokenizer Rules################

def t_START(t):
    r'series:.\[{'    
    return t

def t_NAME(t):
    r'(name|ame):.\'Daily.Deaths\','
    return t

def t_OPENDATA(t):
    r'data:.\['
    return t

def t_CLOSEDATA(t):
    r'\]'
    return t

def t_STYLE(t):
    r'[A-Za-z0-9]+:.[^,]+,'
    return t

def t_CONTENT(t):
    r'[^<>\n\t\[\]]+'
    return t

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES

def p_start(p):
    '''start : START NAME getdata'''

def p_getdata(p):
    '''getdata : STYLE getdata
               | OPENDATA getcontent'''
               
def p_getcontent(p):
    '''getcontent : CONTENT CLOSEDATA'''
    env['data']=p[1]

def p_error(p):
    pass

def getDailyDeaths():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # for tok in lexer:
    #     print(tok)
    parser = yacc.yacc()
    try:
        parser.parse(data)
        dailyDeaths = int(env['data'].split(',')[-1])
        del env['data']
    except:
        dailyDeaths='N/A'
    return dailyDeaths
# dailyDeaths=getDailyDeaths()
# print(f"Daily Death: {dailyDeaths}")