import sys
from ReadLog import read_log
from PrintEntries import printEntries
def sort_log (tupletsList, n):
    if n < len(tupletsList[0]) and n >= 0:
        return sorted(tupletsList, key=lambda a: a[n])  #sorted zwraca ty p ktory byl przekazany
    else:
        return 0

if __name__ == "__main__" :
    printEntries(sort_log(read_log(sys.stdin),4))

