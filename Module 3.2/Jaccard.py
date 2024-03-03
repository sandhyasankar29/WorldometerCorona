from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys
import os
def get_news(country,start,end):
    os.system(f"python3 ./Module 3.2/backjaccard.py {country} {start} {end}")
    f = open("reducer_output.txt",'r')
    data =""
    while True:
        line = f.readline()
        if not line:
            break
        data += line.split(':')[1]
    return data

def calculate_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def jaccard_similarity(country1,start_data,end_data):
    countries = ["Australia","India","Malaysia","England","Singapore"]
    australia_news = get_news(country1,start_data,end_data)
    australia_words = set(set(word_tokenize(australia_news.lower())) - set(stopwords.words('english')))
    max_similarity = 0
    closest_country = ""
    for country in countries:
        try:
            if country != country1:
                country_news = get_news(country,start_data,end_data)
                country_words = set(set(word_tokenize(country_news.lower())) - set(stopwords.words('english')))
                similarity = calculate_jaccard_similarity(australia_words, country_words)
                print(f'{country1} & {country} similarity : {similarity}')
                if similarity > max_similarity:
                    max_similarity = similarity
                    closest_country = country
        except:
            continue
    result=f"The closest country is:{closest_country} with Jaccard similarity: {max_similarity}"
    return result

if __name__ == '__main__':
    country1 = input("Enter Country Name : ").strip()
    start_data = input("Enter Start Date(dd-mm-yyyy) : ")
    end_data = input("Enter End Date(dd-mm-yyyy) : ")
    print(jaccard_similarity(country1,start_data,end_data))