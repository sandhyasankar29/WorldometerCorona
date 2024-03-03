from urllib.request import Request, urlopen
import subprocess
import os

root_directory = os.path.abspath(os.sep)
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
                f=open(f'{directory}.html','w',encoding="utf-8")
                f.write(mydata)
                current_directory = os.getcwd()
                directory_components = current_directory.split(os.sep)
                new_directory_components = directory_components[:-1]
                new_directory = os.sep.join(new_directory_components)
                rel_path=os.path.join(new_directory,f'./Module 3.2/get{category}.py')
                subprocess.run(['python3', rel_path, f'./{directory}/{year}/{month}.txt'])
            except Exception as e:
                print(f"Error fetching data for {month} {year}: {e}")

if __name__ == "__main__":
    news_base_url = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"
    response_base_url = "https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_"
    create_directory("news")
    create_directory("response")
    fetch_data(news_base_url, "News", "news")
    fetch_data(response_base_url, "response", "response")
