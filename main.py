import arrow


print("""
#####    ##    ####  #    # #    # #####  #####   ####  ##### 
#    #  #  #  #    # #   #  #    # #    # #    # #    #   #   
#####  #    # #      ####   #    # #    # #####  #    #   #   
#    # ###### #      #  #   #    # #####  #    # #    #   #   
#    # #    # #    # #   #  #    # #      #    # #    #   #   
#####  #    #  ####  #    #  ####  #      #####   ####    #   
""")
print("Este programa va en tu usb o disco duro lo que hace es sencillo busca en los directorios")
print("y recolecta los archivos con las extenciones .jpeg , jpg , png ")
print("y crea copias de seguridad en el dispositivo de almacenamiento donde se encuentre este programa ")
print("AUTOR : DH ")
hora = arrow.now()
print("hora y dia en que se ejecuta este programa -> " , hora)
entrar = input("Presiona ENTER para entrar ->  ")
if entrar != "":
    print("Hasta Luego")
else : 
    print("Hola")