def checkio(data):
    result = []
    for i,n in enumerate(data):
        if n in data[i+1:] or n in data[:i]:
            result.append(data[i])
    return result
