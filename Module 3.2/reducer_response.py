
month_names = [
    "january", "february", "march", "april",
    "may", "june", "july", "august",
    "september", "october", "november", "december"
]
def parse_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    month -= 1  # Adjust month to be zero-indexed
    return day, month, year



def extract_data(start_data, end_data):

    start_date, start_month, start_year = parse_date(start_data)
    end_date, end_month, end_year = parse_date(end_data)
    with open("mapper_output.txt", "r") as f:
        with open("reducer_output_response.txt", "w") as final:
            for line in f:
                try:
                    key = line.split(":")[0].split(' ')
                    key_month = key[1].strip().lower()
                    key_day = int(key[0].strip())
                    key_year = int(key[2].strip())
                    
                    if (month_names.index(key_month) >= start_month and key_day >= start_date and key_year >= start_year):
                        flag = 1
                    if flag:
                        final.write(line)
                    if (month_names.index(key_month) >= end_month and key_day >= end_date and key_year >= end_year):
                        break
                except Exception as e:
                    continue

if __name__ == "__main__":
    start_date = input("Enter Start Date(dd-mm-yyyy) : ")
    end_date = input("Enter End Date(dd-mm-yyyy) : ")
    extract_data(start_date, end_date)
