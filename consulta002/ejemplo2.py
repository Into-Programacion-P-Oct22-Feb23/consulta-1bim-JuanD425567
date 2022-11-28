 
edad = input ("Ingrese su edad")
  
if edad<2:
    print('Todavía no puede conducir')
else:
    print('Requiere de una licencia especial')


if edad<16:
    print('Todavía no puede conducir')
elif edad<18:
    print('Puede obtener un permiso para conducir')
elif edad<70:
    print('Puede obtener la licencia estandar')
else:
    print('Requiere de una licencia especial')