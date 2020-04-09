import tablib

headers = ('Nome', 'Sobrenome', 'Idade')
data = [
    ('Flavio', 'Conca', 36),
    ('João', 'Silva', 26),
    ('Maria', 'Santos', 23)
]

data = tablib.Dataset(*data, headers=headers)
# print(data.export('json'))
# print(data.export('yaml'))
# data.export('df')
# data.export('xls')
print(data)