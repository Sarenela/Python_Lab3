from ReadLog import read_log
from tools import validateCode
import sys
from PrintEntries import printEntries

def getEntriesByAddr(list,host_name ):
    return [ log for log in list if host_name in log  and validateCode(log[3])]


if __name__ == "__main__":
    printEntries(getEntriesByAddr( read_log(sys.stdin), "isdn6-34.dnai.com"))

