from tools import returnData
import sys
def entryToDict( data_tuple):
    try:
        return { "host":data_tuple[0], "date":data_tuple[1], "request type":data_tuple[2], "status code":data_tuple[3], "data size":data_tuple[4]}
    except ValueError as e:
        raise  ValueError("invalid string format!!!!") from e



