import sys
from LogToDict import logToDict
from ReadLog import read_log

def print_dict_entry_dates(dictionary):
    for key, value in dictionary.items():
        print(f'1 Ip adress/domain name: {key} \n2 nr of requests: {len(value)} \n' 
              f'3.1 date of first request: {min(value, key=lambda a:a["date"])["date"]} \n'
              f'3.2 date of last request: {max(value, key=lambda a:a["date"])["date"]}\n'
              f'4 request ratio with query 200: {int(sum(map(lambda a:a["status code"]=="200", value)))/len(value)}\n')



if __name__ == "__main__":
    print_dict_entry_dates(logToDict(read_log(sys.stdin)))