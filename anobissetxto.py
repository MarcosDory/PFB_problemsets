import sys
anoteste=int(sys.argv[1])

if anoteste%4 == 0:
 if not anoteste%100:
  print("O ano é bissexto")
 elif anoteste%400:
  print("O ano é bissexto")
 else:
  print("não é bissexto")
else:
 print ("não será bissexto")

