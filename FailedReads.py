from ReadLog import read_log
from PrintEntries import printEntries
import sys

def getFailedReads(tuple_list, concatenate):
    list4=[]
    list5=[]
    for tuple in tuple_list:
        if tuple[3] //100 == 4 :
            list4.append(tuple)
        if tuple[3] //100 == 5:
            list5.append(tuple)
    return list4 + list5 if concatenate else [list4,list5]


if __name__ == "__main__":
    printEntries(getFailedReads(read_log(sys.stdin), 1))

