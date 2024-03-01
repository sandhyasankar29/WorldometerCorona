from urllib.request import Request, urlopen
import activecases
import dailyDeaths
import newRecoveries
import newCases

def downloadwebpage(url):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close
    
countryURL = {}

continents=['Europe','North America','Asia','South America','Africa','Oceania']

file = open('worldometers_countrylist.txt','r')
for line in file:
    ex=False
    line = line.strip()
    if('-' in line):
        continue
    if(line==''):
        continue
    for continent in continents:
        if(continent in line):
            ex=True
            break
    if(ex):
        continue
    if(line.lower()=='usa'):
        url=f'https://www.worldometers.info/coronavirus/country/us/'
    elif(line.lower()=='vietnam'):
        url="https://www.worldometers.info/coronavirus/country/viet-nam/"
    else:
        url=f'https://www.worldometers.info/coronavirus/country/{line.replace(" ","-").lower()}/'
    countryURL[line]=url
file.close()
countries=countryURL.keys()
# for country in countries:
#     print(countryURL[country])
#     downloadwebpage(countryURL[country])
#     activeCases=activecases.getCurrentlyInfected()
#     dailyDeath=dailyDeaths.getDailyDeaths()
#     newRecovered=newRecoveries.getNewRecoveries()
#     newCase=newCases.getNewCases()
#     file.write(f'{country}\n------------------------------\nActive Cases: {activeCases}\nDaily Death: {dailyDeath}\nNew Recovered: {newRecovered}\nNew Cases: {newCase}\n\n')
countries=list(countryURL.keys())
n=len(countries)
while(True):
    try:
        for i in range(0,n):
            print(f"{i+1}. {countries[i]}")
        ch = int(input(f"Choose the Country with its keys in range (1,{n})"))-1
        if(ch<0 or ch>=n):
            raise ValueError
        break
    except:
        print(f"Expected value in range 1 to {n}")
    
downloadwebpage(countryURL[countries[ch]])
def fileWrite(filename,data,dates):
    file=open(filename,'w')
    if (data=='N/A' or dates=='N/A'):
        file.write('N/A')
    else:
        for i in range(0,len(dates)):
            try:
                d=int(data[i])
            except:
                d=0
            file.write(f'{dates[i]}\t{d}\n')
    file.close()
dates,activeCases=activecases.getCurrentlyInfected()
fileWrite('ActiveCases.txt',activeCases,dates)
dates,dailyDeath=dailyDeaths.getDailyDeaths()
fileWrite('DailyDeaths.txt',dailyDeath,dates)
dates,newRecovered=newRecoveries.getNewRecoveries()
fileWrite('NewRecovered.txt',newRecovered,dates)
dates,newCase=newCases.getNewCases()
fileWrite('NewCases.txt',newCase,dates)