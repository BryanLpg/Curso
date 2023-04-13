#  if, if-else, if-elif-else while, for

#Decicion if,elif y else
a=1
if a==1:
    print('Se cumple la condicion a==1')
elif a!=1:
    print('Se cumple la condicion a!=1')
elif a<=1:
    print('Se cumple la condicion a<=1')
elif a>=1:
    print('Se cumple la condicion a>=1')
else:
    print('No se cumplen ninguna de las anteriores')
    
#ciclo while
a=1
while a<10:
    a+=1
    print('Recorre este codigo hasta que se no cumpla la condicion de arriba')

#ciclo for
mochila = ['Mochila verde', 'Mochila amarilla', 'Mochila roja', 'Mochila azul', 'Mochila blanca' ]

for i in mochila:
    print(f'Aqui esta la {i}')
    
for i in range(10):
    print(i)
    
for i, mochila  in enumerate(mochila, start=1):
    print(f'{i}. {mochila}')
#recordando que en los ciclos y deciciones se usan los break (Interrumpe el siclo) pass (hace caso omiso osea no hace nada) y continue (Suma una vuelta al siclo obviando el codigo de abajo)