def checkio(data):
    data = sorted(data)
    if len(data) % 2 == 0:
        return 0.5 * (data[int(len(data)/2)] + data[int(len(data)/2) - 1])
    else:
        return data[int((len(data)/2))]
