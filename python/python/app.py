# ------------------------------------------------ 
'''
x = 4
x = "wendy"
print(x)
'''
# ------------------------------------------------
'''
x = str(3)
y = int(3) 
z = float (3)
print(x , y , z)
'''
# ------------------------------------------------
'''
x = 5
y = "william"
print(type(x))
print(type(y))
'''
# ------------------------------------------------
'''
print("digite su nomnbre")
nombre = input()
print("nombre" +  nombre)
'''
# ------------------------------------------------
'''
print("porfavor digite un numero")
a = int(input())
print("digite un segundo numeor")
b = int(input())

sum  = a + b
print("este es la suma de los numeros")
print(sum)
'''
# ------------------------------------------------
'''
numero = int(input('porfavor ingrese un numero'))
if  numero > 0 :
        print(f'el valor es {numero} es positivo')
else:
        print(f'el valor es {numero} es negativo')
        
'''
# ------------------------------------------------
'''
numero = int(input('porfavor ingrese un numero'))
if  numero > 0 :
    print(f'el valor es {numero} es positivo')
elif numero < 0 :
    print(f'el valor es {numero} es negativo')
else:
    print(f'el valor es {numero} es cero')
'''
# ------------------------------------------------
'''
diasemanas = input(
    "selecionas cual quier dia de la semana: 'lunes','martes','miercoles','jueves','viernes','sabado','domingo': ")
time = int(input("escriba el tiempo en minutos: "))


def cobrarhora(costo):
    costo = float(time * costo)
    print(f"el costo es: ${costo} ")


if diasemanas == 'lunes' or diasemanas == 'martes' or diasemanas == 'miercoles':

    if time > 5:
        costo = 2.00
        cobrarhora(costo)
    else:
        print("costo estipulado:  $0.00 ")

if diasemanas == 'jueves' or diasemanas == 'viernes':

    if time > 5:
        costo = 2.50
        cobrarhora(costo)

    else:

        print("costo estipulado: $0.00 ")

if diasemanas == 'sabado' or diasemanas == 'domingo':

    if time > 5:
        costo = 3.00
        cobrarhora(costo)

    else:

        print("costo estipulado: $0.00 ")
'''
# ------------------------------------------------ ciclos repetitivos for
'''
for x in range(6):
    print(x)
'''
# ------------------------------------------------
'''

for x in range(2,6):
    print(x)
'''
# ------------------------------------------------
'''

for x in range(2,30,3):
    print(x)
'''
# ------------------------------------------------
'''

for x in "banana":
    print(x)

'''
# ------------------------------------------------
'''
for x in range(6):
    if x == 3: break
    print(x)
       
else:
    print("finally finished")
'''
# ------------------------------------------------ ciclos repetitivos while
'''
i = 1 
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
'''
# ------------------------------------------------
'''
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
'''
# ------------------------------------------------
'''
i = 1
while i < 6:
    print(i)
    i += i
else: 
    print("i no es menor a 6")
'''
# ------------------------------------------------ arrays 
'''
a = "hola mundo"
print(a[1])
'''
# ------------------------------------------------ 
'''
txt = "hola mundo"
print("hola" in txt)
'''
# ------------------------------------------------ 
'''
a = "hola mundo"
print(len(a))
'''
# ------------------------------------------------ buscador en texto
'''
txt = " hola mundo"
if "hola" in txt:
    print("yes , 'hola' is present")
'''
# ------------------------------------------------ 
'''
txt = " hola mundo"
if "hola" no in txt:
    print("no , 'hola' is not present")
'''
# ------------------------------------------------ 
'''
b = "hola mundo"
print(b[2:5])
'''
# ------------------------------------------------ 
'''
b = "hola mundo"
print(b[2:])
'''
# ------------------------------------------------ 
'''
b = "hola mundo"
print(b[:5])
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b[-5:-2])
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b.upper())
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b.strip())
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b.split(","))
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b.alower())
'''
# ------------------------------------------------
'''
b = "hola mundo"
print(b.replace("h","j"))
'''
# ------------------------------------------------
'''
age = 36 
txt = "hola mundo" + age
print(txt)
'''
# ------------------------------------------------
'''
age = 36 
txt = "hola mundo {}" 
print(txt.format(age))
'''
# ------------------------------------------------
'''
quanity = 3
itemmno = 567
price = 49.95
myorde = "hola mundo {} xd {} dea {} dollar"
print(myorde.format(quanity , itemmno , price))
'''
# ------------------------------------------------  
'''
quanity = 3
itemmno = 567
price = 49.95
myorde = "hola mundo {2} xd {0} dea {1} dollar"
print(myorde.format(quanity , itemmno , price))
'''
#------------------------------------------------ imprime en fila 
'''
fruits = ["aplle", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
'''
#------------------------------------------------ imprimir en ordende lista
'''
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)
'''
#------------------------------------------------ eliminar un string por posicion
'''
thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)
'''
#------------------------------------------------ limpiar
'''
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
'''
#------------------------------------------------ agregar ultima posicion
'''
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
'''
#------------------------------------------------ unir 2 lista
'''
thislist = ["apple","banana","cherry"]
tropical = ["mango","manzana","pera"]
thislist.extend(tropical)
print(thislist)
'''
#------------------------------------------------ buscador en una lista nombre te validara si esta en la lista 
'''
thislist = ["apple","banana","cherry"]
if "banana" in thislist:
    print("si esta")
else:
    print("no esta")    
'''
#------------------------------------------------ buscador de nombre y te muestra la posicion
'''
thislist = ["apple","banana","cherry"]
elemento = "banana"
try:
    indice = thislist.index(elemento)
    print(f"El thislist {elemento} se encuentra en el índice {indice}")
except ValueError:
    print(f"El thislist {elemento} no se encuentra en el array")

'''
#------------------------------------------------ te imprime el nombre por la posicion
'''
thislist = ["apple","banana","cherry"]
print(thislist[0])
'''
#------------------------------------------------ elimina por posicion
'''
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
'''
#------------------------------------------------ agregrar despues del string siguiente por la posicion
'''
thislist = ["apple","banana","cherry"]
thislist.insert(2,"wilches")
print(thislist)
'''
#------------------------------------------------ agregrar despues del string siguiente por la posicion
'''
my_list = []  

while True:
    element = input("Ingrese un nombre o precione enter para finalizar: ")
    if element == "":
        break
    my_list.append(str(element))

my_array = my_list  

print(my_array)
'''