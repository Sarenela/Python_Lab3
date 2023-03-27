import re
import datetime


def validateCode(code):
    return 1 if type(code) == int and  code>=100 and code <=599 else 0

def returnData(line):
    try:
        string_data= separate(line)
        return  (string_data[0], getDate(string_data[1]), getRequestType(string_data[2]), int(string_data[3]), toInt(string_data[4]))
                #host                data                      rodzaj requestu http             kod                  rozmiar
    except ValueError as e  :
        raise  ValueError("invalid string format!!!!") from e

def toInt(string_data):
    num=0
    try:
        num = int(string_data)
    except Exception as e:
        return 0
    return num


def separate(line):
    try:
        data = re.match(r"(.+) - - \[(.+)\] \"(.+)\" (.+) (.+)",line)
        return [data[1],data[2],data[3],data[4],data[5]]
    except ValueError as e:
       raise  ValueError("invalid string format!!!!") from e



def getDate(string_date):
    try:
        return datetime.datetime.strptime(string_date , "%d/%b/%Y:%X %z")

    except Exception as e:
        raise ValueError("invalid string format!!!!") from e


def getRequestType(string_request):
    try:
        return string_request.split(" ")[0]
    except:
        raise ValueError("invalid string format!!!!")


def getPath(string_request):
    try:
        return string_request.split(" ")[1]
    except:
        raise ValueError("invalid string format!!!!")

def getFileType(line):
    try:
        return getPath(line).split(".")[-1]
    except:
        raise ValueError("invalid string format!!!!")


