import sys
from LogToDict import logToDict
from ReadLog import read_log
from PrintEntries import printEntries

def get_addrs(dictionary):
    return dictionary.keys()

if __name__ == "__main__":
    printEntries(get_addrs(logToDict(read_log(sys.stdin))))

