def test():
    data = {
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}
        }
    }
    return checkio(data)

def flatten(data):
    if data:
        result = {}
        for i in data:
            if isinstance(data[i], dict):
                temp = flatten(data[i])
                if temp:
                    for j in temp:
                        result['%s/%s' % (i,j)] = temp[j]
                else:
                    result[i] = ''
            else:
                result[i] = data[i]
        return result
    else:
        return None


