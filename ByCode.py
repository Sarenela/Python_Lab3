import sys
from ReadLog import read_log
from tools import validateCode
from PrintEntries import printEntries
def get_entries_by_code (tupletsList, statusCode):
    if validateCode(statusCode):
        return list(filter(lambda a: a[3] == statusCode, tupletsList))
    else:
       return []



if __name__ == "__main__":
    printEntries(get_entries_by_code(read_log(sys.stdin), 200))