import sys
import re
month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]

def getdaterange(country):
        f=open("mapper_output.txt","w+", encoding='utf-8')
        if(country=='Singapore'):
                f1=open('Singapore (2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Singapore (2021).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Singapore (2022).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2022"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
        elif(country=='Malaysia'):
                f1=open('Malaysia (2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Malaysia (2021).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Malaysia (2022).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2022"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Malaysia (2023).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2023"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Malaysia (2024).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2024"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
        elif(country=='England'):
                f1=open('England (January–June 2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('England (July–December 2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('England (2021).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('England (2022).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2022"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
        elif(country=='India'):
                f1=open('India (January–May 2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('India (June–December 2020).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('India (2021).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
        elif(country=='Australia'):
                f1=open('Australia_2020.txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2020"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Australia_(Jan-Jun 21).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Australia(Jul-Dec 21).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2021"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue
                f1=open('Australia_(2022).txt','r')
                for line in f1.readlines():
                        line=line.strip()
                        try:
                                if(line==''):
                                        continue
                                data = line.split(':', maxsplit=1)
                                data[0] = data[0]+' '+"2022"
                                f.write(':'.join(data) + '\n')
                        except:
                                continue      
        else:
                print("invalid country")
                exit()
                
        f.close()
        map_data=open("mapper_output.txt",'r', encoding='utf-8')
        first_line=map_data.readline()
        last_line=None
        while(True):
                line = map_data.readline()
                if not line:
                        break
                if(line.strip()!=''):
                        last_line=line
        patternDateMonth=r'(\d\d|\d).(January|February|March|April|May|June|July|August|September|October|November|December)'
        patternYear=r'(\d\d\d\d)'
        fdate=re.findall(patternDateMonth,first_line.split(':')[0])[0]
        fyear=re.findall(patternYear,first_line.split(':')[0])[0]
        ldate=re.findall(patternDateMonth,last_line.split(':')[0])[-1]
        lyear=re.findall(patternYear,last_line.split(':')[0])[-1]
        result = f"From Date: {fdate[0]} {fdate[1]} {fyear}\nTo Date: {ldate[0]} {ldate[1]} {lyear}"
        return result

if __name__ == '__main__':
        country = input("Enter Country Name : ").strip()
        print(getdaterange(country))
        



