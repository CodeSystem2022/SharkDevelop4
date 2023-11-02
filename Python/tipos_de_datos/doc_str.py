from mi_clase import MiClase
#help(MiClase) #Accedemos a la documentacion completa

#print(MiClase.__doc__)
#print(MiClase.__init__.__doc__) #ingresamos a mi clase para ver la documentacion
#print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo) #esto solo nos mostraria la ubicacion en memoria 
#porque TODO EN PYTHON SON OBJETOS
print(type(MiClase.mi_metodo)) #para ver de q tipo es mi_metodo