from urllib.request import Request, urlopen

# user_input = input("Enter the country Name: ")
# # print(user_input)

# user_input = user_input.replace(" ", "_")
# # print(user_input)

url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Malaysia_(2024)"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
f = open('countrynews.html', 'w', encoding="utf-8")
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f.write(mydata)
f.close()

# url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_February_2020"

# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# f = open('news.html', 'w', encoding="utf-8")
# webpage = urlopen(req).read()
# mydata = webpage.decode("utf8")
# f.write(mydata)
# f.close()



# url = f"https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_May_2021"

# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# f = open('response.html', 'w', encoding="utf-8")
# webpage = urlopen(req).read()
# mydata = webpage.decode("utf8")
# f.write(mydata)
# f.close()