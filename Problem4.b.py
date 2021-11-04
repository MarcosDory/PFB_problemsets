myList=[101,2,15,22,95,33,2,27,72,15,52]
somaPares=0
somaImpar=0
for numero in myList:
 if numero % 2 == 0:
  print(numero)
  somaPares+=numero
 else:
  somaImpar+=numero
print(f'Sum of even numbers: {somaPares}\nSum of odds: {somaImpar}')

