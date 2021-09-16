import postidata
import re

def pyydaSyote():
    return input('Kirjoita postitoimipaikka: ')

def cleanString(string):
    return re.sub(r'-|\ ', '', string).upper()

def flipData(data):
    flipped_data = {}
    for key, value in data.items():
        value = cleanString(value)
        flipped_data.setdefault(value, []).append(key)
    return flipped_data

def haePostitoimipaikanNumerot(postitoimipaikka):
    data = postidata.getData()
    cleanedInput = cleanString(postitoimipaikka)
    flipped_data = flipData(data)
    return flipped_data.get(cleanedInput, 'Virheellinen postitoimipaikka: ' + postitoimipaikka)

if __name__ == '__main__':
    print(haePostitoimipaikanNumerot(pyydaSyote()))