import postidata

data = postidata.getData()

postinumero = input('Kirjoita postinumero: ')

print(data[postinumero])