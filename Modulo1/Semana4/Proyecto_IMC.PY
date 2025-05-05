# Proyecto IMC
nombre = input('Ingresa tu nombre: ')
apellido_paterno = input('Ingresa tu apellido paterno: ')
apellido_materno = input('Ingresa tu apellido materno: ')
edad = int(input('Ingresa tu edad: '))
peso = float(input('Ingresa tu peso en kg: '))
estatura = float(input('Ingresa tu estatura en metros: '))

 
IMC = peso / estatura ** 2


print('-RESULTADOS-')
print('nobre completo:', nombre, apellido_paterno, apellido_materno)
print('edad:', str(edad) + 'años')
print('peso:', str(peso) + 'kg')
print('estatura:', str(estatura) + 'm')
print(f'IMC: {IMC:.2f}')
print()
