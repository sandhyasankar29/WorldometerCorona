# import sys
# import os
from urllib.request import Request, urlopen

# def create_directory(directory_path):
#     if not os.path.exists(directory_path):
#         os.makedirs(directory_path)
#         os.makedirs(directory_path+'/2020')
#         os.makedirs(directory_path+'/2021')
#         os.makedirs(directory_path+'/2022')



# # Example usage:
# directory_path = "news"
# create_directory(directory_path)
# directory_path = "response"
# create_directory(directory_path)
# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# years = [2020,2021,2022]


# for year in years:
#     for month in months:
#         link= f'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{month}_{year}'
#         req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
#         webpage = urlopen(req).read()
#         mydata = webpage.decode("utf8")
#         f=open('news.html','w',encoding="utf-8")
#         f.write(mydata)
#         os.system(f"python3 getNews.py ./news/{year}/{month}.txt")
#         # f1=open(f'./news/{year}/{month}.txt','w+',encoding="utf-8")
#         # f1.write(str1)
#         f.close()

# for year in years:
#     for month in months:
#         try:
#             link= f'https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_{month}_{year}'
#             req = Request(link,headers ={'User-Agent':'Mozilla/5.0'})
#             webpage = urlopen(req).read()
#             mydata = webpage.decode("utf8")
#             f=open('response.html','w',encoding="utf-8")
#             f.write(mydata)
#             os.system(f"python3 getresponse.py ./response/{year}/{month}.txt")
#             # f1=open(f'./news/{year}/{month}.txt','w+',encoding="utf-8")
#             # f1.write(str1)
#             f.close()
#         except:
#                 continue
        
import os
import requests

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)
    for year in range(2020, 2023):
        os.makedirs(f"{directory_path}/{year}", exist_ok=True)

def fetch_data(base_url, category, directory):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    for year in range(2020, 2023):
        for month in months:
            url = f"{base_url}{month}_{year}"
            
            try:

                req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
                webpage = urlopen(req).read()
                mydata = webpage.decode("utf8")
                # response = requests.get(url)
                # response.raise_for_status()
                f=open(f'{directory}.html','w',encoding="utf-8")
                f.write(mydata)
                os.system(f"python3 get{category}.py ./{directory}/{year}/{month}.txt")
            except Exception as e:
                print(f"Error fetching data for {month} {year}: {e}")

if __name__ == "__main__":
    news_base_url = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"
    response_base_url = "https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_"
    create_directory("news")
    create_directory("response")
    fetch_data(news_base_url, "News", "news")
    fetch_data(response_base_url, "response", "response")
