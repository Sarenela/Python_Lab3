from EntryToDict import entryToDict
from ByAddress import getEntriesByAddr
from ReadLog import read_log

import sys

def logToDict(tuple_list):
    result_dict={}
    for tuple in tuple_list:
        try:
            if tuple[0] not in result_dict:
                result_dict[tuple[0]] =[entryToDict(log_tuple) for log_tuple in getEntriesByAddr(tuple_list,tuple[0])]
        except ValueError:
            continue
    return result_dict



if __name__ == "__main__":
    print(logToDict(read_log(sys.stdin)))
