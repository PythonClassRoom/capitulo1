#Introduccion al depurador mediante pdb.set_trace()
import pdb

print('Inicia valores')

a = 100
b = 2
pdb.set_trace()

b = 5
a = a /b
