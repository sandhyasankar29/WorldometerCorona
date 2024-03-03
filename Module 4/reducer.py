#!/usr/bin/env python
"""reducer.py"""
f = open("reducer_output.txt", "a")

import sys

# Define initial variables
Total_Cases = Active_Cases = Total_Deaths = Total_Recovered = Total_Tests = Deaths_M = Tests_M = New_Cases = New_Deaths = New_Recovered = 0

# input comes from STDIN (standard input)
flag = 0
for line in sys.stdin:
    line = line.strip()
    if flag == 0:
        choice = line
        flag += 1
        continue
    if flag == 1:
        country = line
        flag += 1
        continue
    if 'World' in line:
        parts = line.split(':')[:-1]
        # Assign values to variables
        Total_Cases, Active_Cases, Total_Deaths, Total_Recovered, Total_Tests, Death_Per_Million, Tests_Per_Million, New_Cases, New_Deaths, New_Recovered = map(float, parts[1:])
        # f.write(Total_Cases)
        continue
    if country in line:
        # f.write(line)
        parts = line.split(':')[:-1]
        # Assign values to variables
        Total_Cases2, Active_Cases2, Total_Deaths2, Total_Recovered2, Total_Tests2, Death_Per_Million2, Tests_Per_Million2, New_Cases2, New_Deaths2, New_Recovered2 = map(float, parts[1:])
        if choice == 'a':
            f.write("Total cases: "+str(Total_Cases2)+"\n")
            f.write("Total Deaths: "+str(Total_Deaths2)+"\n")
            f.write("Total Recovered: "+str(Total_Recovered2)+"\n")
            f.write("Total Tests: "+str(Total_Tests2)+"\n")
            f.write("Death_Per_Million2: "+str(Death_Per_Million2)+"\n")
            f.write("Tests_Per_Million2: "+str(Tests_Per_Million2)+"\n")
            f.write("New_Cases2: "+str(New_Cases2)+"\n")
            f.write("New_Deaths2: "+str(New_Deaths2)+"\n")
            f.write("New_Recovered2: "+str(New_Recovered2)+"\n")

        continue
if choice == 'a':
    f.write("a. Total cases: ")
    if Total_Cases != 0:
        f.write(str((Total_Cases2 / Total_Cases) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'b':
    f.write("b. Active cases: ")
    if Active_Cases != 0:
        f.write(str((Active_Cases2 / Active_Cases) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'c':
    f.write("c. Total deaths: ")
    if Total_Deaths != 0:
        f.write(str((Total_Deaths2 / Total_Deaths) * 100)+'%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'd':
    f.write("d. Total recovered: ")
    if Total_Recovered != 0:
        f.write(str((Total_Recovered2 / Total_Recovered) * 100),+'%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'e':
    f.write("e. Total tests: ")
    if Total_Tests != 0:
        f.write(str((Total_Tests2 / Total_Tests) * 100)+'%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'f':
    f.write("f. Death/million: ")
    if Death_Per_Million != 0:
        f.write(str((Death_Per_Million2 / Death_Per_Million) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'g':
    f.write("g. Tests/million: ")
    if Tests_Per_Million != 0:
        f.write(str((Tests_Per_Million2 / Tests_Per_Million) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'h':
    f.write("h. New cases: ")
    if New_Cases != 0:
        f.write(str((New_Cases2 / New_Cases) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'i':
    f.write("i. New deaths: ")
    if New_Deaths != 0:
        f.write(str((New_Deaths2 / New_Deaths) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
elif choice == 'j':
    f.write("j. New recovered: ")
    if New_Recovered != 0:
        f.write(str((New_Recovered2 / New_Recovered) * 100)+ '%\n')
    else:
        f.write("Cannot divide by zero\n")
else:
    f.write("Invalid choice")
