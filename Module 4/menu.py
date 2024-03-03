import os

# Print the menu
# print("COVID-19 comparison Menu:")
# print("a. Total cases")
# print("b. Active cases")
# print("c. Total deaths")
# print("d. Total recovered")
# print("e. Total tests")
# print("f. Death/million")
# print("g. Tests/million")
# print("h. New cases")
# print("i. New deaths")
# print("j. New recovered")
def menu(country):
    for choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        os.system(f"python mapper.py {choice} {country} | python combiner.py | python reducer.py > percentagechange.txt")
        
# menu("India")