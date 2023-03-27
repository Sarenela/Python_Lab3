from tools import returnData
import sys
from PrintEntries import printEntries

def read_log(data_stream):
    lista =[]
    for line in data_stream:
        try:
             lista.append(returnData(line))
        except EOFError:
            break
        except ValueError:
            continue
    return lista


if __name__ == "__main__":
    printEntries(read_log(sys.stdin))
