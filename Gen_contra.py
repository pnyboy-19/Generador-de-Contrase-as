import random

caracteres ="abcdefghijklmnñopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ°|¬!#$%&/()=?\"\'\\¡¿¨´*+~[{^]}`<>;,:._-*-"
x = True

while x == True:
    contraseña_lon=(int(input("De que cuantos caracteres quieres la contraseña?: ")))
    cant_contra=(int(input("Cuantas contraseñas quieres generar?: ")))

    for x in range(0, cant_contra):
        contraseña = ""
        for x in range(0, contraseña_lon):
            contraseña_caracter= random.choice(caracteres)
            contraseña = contraseña + contraseña_caracter
        print("Aqui esta tu contraseña: ", contraseña)
    x = False