import re


def checkio(data):
    if re.match(".*[A-Z]+.*", data):
        if re.match(".*[a-z]+.*", data):
            if re.match(".*[0-9]+.*", data):
                if len(data) >= 10:
                    return True
    else: 
        return False
