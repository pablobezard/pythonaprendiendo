myStr = "Hello world"

print(dir(myStr)) 

print(myStr.upper()) #mayusculas
print(myStr.lower()) #minusculas
print(myStr.swapcase()) #variado
print(myStr.capitalize()) #primeraletraM
myStr.replace("hello" , "bye").upper #reemplaza 
print(myStr.count("l")) #cuantasvecestengoelcaracter

print(myStr.startwith("hello"))#empiezaconelcaracter? boolean
print(myStr.endswith("word"))#terminaconelcaracter? boolean

print(myStr.split("")) #separa palabra por caracter seleccionado
print(myStr.find ("")) #encuentra caracter por posicion numerica

print(len(myStr)) #buscar longitud de variable
print(myStr.index("")) #buscar indice 

print(myStr.isnumeric()) #es numerico  
print(myStr.isalpha()) #inverso 

print(myStr()) #imprimir tal caracter 

#formas de concatenar 
print("bienvenido " + myStr)
print(f"bienvenido (myStr)") 
print("bienvenido (0)" .format(myStr))
