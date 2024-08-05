
edad = int(input ("Por favor, ingresa tu edad:  "))

permitido = True if edad >= 18 else False

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no puedes ingresar a la discoteca siendo menor de edad")  