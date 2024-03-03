# #extract file
# import sys
# # start=input().split('-')
# # end=input().split('-')
# months = [
#     "January", "February", "March", "April",
#     "May", "June", "July", "August",
#     "September", "October", "November", "December"
# ]


# f=open("mapper_output.txt","w")
# for i in [2020,2021,2022]:
#         for month in months:
#                 f_str="news/"+str(i)+"/"+str(month)+".txt"
#                 try: 
#                         file1=open(f_str,"r+",encoding='cp1252')
#                 except:
#                         print("file not found")
#                         continue
#                 for line in file1.readlines():
#                         line=line.strip()
#                         try:
#                                 if(line==''):
#                                         continue
#                                 data = line.split(':', maxsplit=1)
#                                 data[0] = data[0]+' '+str(i)
#                                 f.write(':'.join(data) + '\n')
#                         except:
#                                 continue
                                

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def write_data_to_file(year, months, output_file):
    for month in months:
        file_path = f"response/{year}/{month}.txt"
        
        try:
            with open(file_path, "r", encoding='cp1252') as file1:
                for line in file1:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data = line.split(':', maxsplit=1)
                        data[0] = data[0] + ' ' + str(year)
                        output_file.write(':'.join(data) + '\n')
                    except Exception as e:
                        print(f"Error processing line: {e}")
        except FileNotFoundError:
            # File not found, skip to the next month
            continue

with open("mapper_output.txt", "w") as f:
    for year in [2020, 2021, 2022]:
        write_data_to_file(year, months, f)

