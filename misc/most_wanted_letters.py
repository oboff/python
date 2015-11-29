def checkio(text):
    return max([x for x in sorted(text.lower()) if x.isalpha()], key = text.lower().count)
