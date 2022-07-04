# 1 = si
# 0 = no


personajes_smash={
    "Mario":{'color':'rojo','gorra':'si','humano':'si','bigote':'si','ojos':'no'},
    "Luigi":{'color':'verde','gorra':'si','humano':'si','bigote':'si','ojos':'no'},
    "Donkey Kong":{'color':'cafe','gorra':'no','humano':'no','bigote':'no','ojos':'no'},
    "Link":{'color':'verde','gorra':'si','humano':'si','bigote':'no','ojos':'si'},
    "Samus": {'color':'rojo','gorra':'no','humano':'si','bigote':'si','ojos':'si'},
    "Captain Falcon":{'color':'morado','gorra':'si','humano':'no','bigote':'no','ojos':'no'},
    "Ness":{'color':'morado','gorra':'si','humano':'si','bigote':'si','ojos':'no'},
    "Yoshi":{'color':'verde','gorra':'no','humano':'no','bigote':'no','ojos':'no'},
    "kirby":{'color':'rosa','gorra':'no','humano':'no','bigote':'no','ojos':'si'},
    "Fox":{'color':'cafe','gorra':'no','humano':'no','bigote':'no','ojos':'si'},
    "Pikachu":{'color':'amarillo','gorra':'no','humano':'no','bigote':'no','ojos':'si'},
    "Jigglypuff":{'color':'rosa','gorra':'no','humano':'no','bigote':'no','ojos':'si'}
}


def sistema_experto(personajes_smash):
    color = input("Cual es el color principal de tu personaje?")
    keys = []
    keys2 = []
    keys3 = []
    keys4 = []
    keys5 = []
    print(f"Buscando entre los personajes con color principal {color}")
    for i in personajes_smash.keys():
        if personajes_smash[i]["color"]==color:
            keys.append(i)
    if len(keys)==0:
                return "no hay coincidencias"
    gorra=input("tu personaje tiene gorra")
    if gorra == 'no':
        print(f"Buscando entre los personajes con color {color} y sin gorra")
    else:
        print(f"Buscando entre los personajes con color {color} y con gorra")
    for i in keys:
        if gorra =='si':
            if personajes_smash[i]['gorra']==gorra:
                keys2.append(i)
        else:
            if gorra =='no':
                if personajes_smash[i]['gorra']==gorra:
                    keys2.append(i)
    if len(keys2)==1:
        print(f"tu personaje es {keys2}")
        multsolu=input("Deseas seguir con la busqueda")
        if multsolu == 'si':
            pass
        else:
            if multsolu == 'no':
                return f"tu personaje es {keys2}"


    humano=input("tu personaje tiene forma humana")
    if humano == 'no':
        print(f"Buscando entre los personajes con color {color} y sin forma humana")
    else:
        print(f"Buscando entre los personajes con color {color} y con forma humana")
    for i in keys2:
        if humano=='si':
            if personajes_smash[i]['humano'] == humano:
                keys3.append(i)
        else:
            if humano == 'no':
                if personajes_smash[i]['humano'] == humano:
                    keys3.append(i)
    if len(keys3)==1:
        print(f"tu personaje es {keys3}")
        multsolu = input("Deseas seguir con la busqueda")
        if multsolu == 'si':
            pass
        else:
            if multsolu == 'no':
                return f"tu personaje es {keys3}"

    bigote=input("tu personaje tiene bigote")
    if bigote == 'no':
        print(f"Buscando entre los personajes con color {color} y sin bigote")
    else:
        print(f"Buscando entre los personajes con color {color} y con bigote")
    for i in keys3:
        if bigote == 'si':
            if personajes_smash[i]['bigote'] == bigote:
                keys4.append(i)
        else:
            if bigote == 'no':
                if personajes_smash[i]['bigote'] == bigote:
                    keys4.append(i)
    if len(keys4)==1:
        print(f"tu personaje es {keys4}")
        multsolu = input("Deseas seguir con la busqueda")
        if multsolu == 'si':
            pass
        else:
            if multsolu == 'no':
                return f"tu personaje es {keys4}"

    ojos =input("tiene ojos azules")
    if ojos == 'no':
        print(f"Buscando entre los personajes con color {color} y sin ojos azules")
    else:
        print(f"Buscando entre los personajes con color {color} y con ojos azules")
    for i in keys4:
        if ojos == 'si':
            if personajes_smash[i]['ojos'] == ojos:
                keys5.append(i)
        else:
            if ojos == 'no':
                if personajes_smash[i]['ojos'] == ojos:
                    keys5.append(i)

    return (f"personaje {keys5}")

def interfaz(personajes_smash):
    print("---------------Sistema Experto para personajes de Super Smash Bros -------------------")
    print("Opcion (a) -> Mostrar Base de Datos")
    print("Opcion (b) -> Ejecutar el sistema experto")
    print("Salir presiona cualquier otra tecla")
    seleccion=input()
    if seleccion.lower() == 'a':
            print(personajes_smash)
    elif seleccion.lower() == 'b':
                print(sistema_experto(personajes_smash))
    else:
                print("adios.....")

interfaz(personajes_smash)




