#La funcion nos ayudará a conocer cuales son las zonas que se deben limpiar
def identificarZonasAlimpiar(estado):
    arrayParabriSucios=[]
    for k, v in estado.items():
        if(v[0]=='1'):
            arrayParabriSucios.append(v[1])
    return arrayParabriSucios
#En el caso de que la posicion no sea la menor, la aspiradora se redirigira a la posicion menor
def redirigirAlprimero(costo, posicion, menor):
    if(posicion==menor):
        pass
    else:
        print()
        for i in range(posicion,menor,-1):
            print('redirigiendo un puesto de zona '+str(posicion)+' a posicion '+str(posicion-1))
            costo+=1
        posicion=menor
    return costo, posicion
#Evalua si la zona es contenida en tal caso retorna falso
def containZona(numero, zonaAlimpiar, estado):
    keys = list(estado.keys())
    for x in zonaAlimpiar:
        if(numero==x):
            print('Limpiando '+keys[x-1])
            return True
    return False
        
    
    
#Hace una limpieza de los parabrisas
def limpiezaVidrio(zonasAlimpiar, posicion_aspiradora, estado,costo):
    for i in range(posicion_aspiradora ,zonasAlimpiar[len(zonasAlimpiar)-1]+1,+1):
        print(i)
        if(containZona(i, zonasAlimpiar, estado)):
            costo+=2
            print('Redirigiendo...')
        else:
            costo+=1
            print('Redirigiendo...')
    print('Todo se ha limpiado')
    return costo


#guardara la información de las zonas
estado={}
#ayudará a darle una posición de orden a los estados
valor=1
#nos ayudará a saber el costo de limpiar 
costo=0
print('Para el programa deberá establecer todas las zonas de limpieza \n')
while(True):
    # verificacion para poder ingresar otra zona
    verificacion = (input("Si desea ingresar otra zona escriba Y: ")).upper()
    if(verificacion=='Y'):
        localizacion = input("Ingresa una zona existente: ")
        estadoLimpieza = input("Ingrese el estado de esa zona: ")
        estado[str(localizacion)] = [estadoLimpieza,valor]
        valor+=1
    else:
        break
position = input("Digite la zona en que se encuentra la aspiradora: ")
# Identificación de las zonas para limpiar frente al estado
ventanasSucias=identificarZonasAlimpiar(estado)
# movimiento a la izquierda
costo, position=redirigirAlprimero(int(costo), int(position), int(ventanasSucias[0]))
# asignación del costo en base a la limpieza del vidrio
costo=limpiezaVidrio(ventanasSucias, position, estado, costo)

print('El costo seria '+str(costo))
