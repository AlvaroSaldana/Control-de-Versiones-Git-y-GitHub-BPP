import csv
 
with open('example.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
n = int(input("¿Qué mes se ha gastado más?:"))
for i in range(n, 1, -1):
    print( i,  end=" Enero " )

n = int(input("¿Qué mes se ha ahorrado más?:"))
for i in range(n, 1, -1):
    print( i,  end=" Abril " )
n = int(input("¿Cuál es la media de gastos al año?:"))
for i in range(n, 1, -1):
    print( i,  end=" 850,70€ " )
n = int(input(" ¿Cuál ha sido el gasto total a lo largo del año?:"))
for i in range(n, 1, -1):
    print( i,  end=" 980856€ " )
11111
import os
if os.path.isfile('example.csv'):
    print('El archivo existe.');
else:
    print(' No existe archivo');
str1 = "hay numeros"
str2 = " hay numeros"
str3 = "hay numeros"
str4 = "hay numeros"
str5 = "hay numeros"
str6 ="hay numeros"
str7 ="hay numeros"
str8 ="hay numeros"
str9 ="hay numeros"
srt10 ="hay numeros"
str11 ="vacio"
str12 ="vacío"

print(any(map(str.isdigit, str1)))
print(any(map(str.isdigit, str2)))
print(any(map(str.isdigit, str3)))
print(any(map(str.isdigit, str4)))
print(any(map(str.isdigit, str5)))
print(any(map(str.isdigit, str6)))
print(any(map(str.isdigit, str7)))
print(any(map(str.isdigit, str8)))
print(any(map(str.isdigit, str9)))
print(any(map(str.isdigit, str1)))
print(any(map(str.isdigit, str11)))
print(any(map(str.isdigit, str12)))

  



  