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
country = input("Type Country Name(Case Sensitive), use the format specified in worldometers_countrylist.txt: ")
countries=countryURL.keys()
file=open('Result.txt','w')
# for country in countries:
#     print(countryURL[country])
#     downloadwebpage(countryURL[country])
#     activeCases=activecases.getCurrentlyInfected()
#     dailyDeath=dailyDeaths.getDailyDeaths()
#     newRecovered=newRecoveries.getNewRecoveries()
#     newCase=newCases.getNewCases()
#     file.write(f'{country}\n------------------------------\nActive Cases: {activeCases}\nDaily Death: {dailyDeath}\nNew Recovered: {newRecovered}\nNew Cases: {newCase}\n\n')

downloadwebpage(countryURL[country])
activeCases=activecases.getCurrentlyInfected()
dailyDeath=dailyDeaths.getDailyDeaths()
newRecovered=newRecoveries.getNewRecoveries()
newCase=newCases.getNewCases()
file.write(f'{country}\n------------------------------\nActive Cases: {activeCases}\nDaily Death: {dailyDeath}\nNew Recovered: {newRecovered}\nNew Cases: {newCase}')
file.close()