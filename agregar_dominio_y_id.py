
#def agregar_dominio_a_correos(nombre,dominio):




nombres="""
SALAS JUAREZ MONICA
ROMAN MARTINEZ RIGOBERTO FERNANDO
GOMEZ HERNANDEZ JOSSY DANIEL
CERVANTES FERNANDEZ RAQUEL
CONTRERAS GONZALEZ MARIA DEL SOCORRO
CORONADO MOJARRO YAHANY ARELY
SANCHEZ CORREA JAVIER
GOMEZ GARCIA JOSE MAGDALENO
PEREZ MENDEZ NEFTALI
TRIANA DEL ANGEL MONTSERRAT
TORRES GONZALEZ ANDREA VICTORIA
RAMOS CASTANEDA ROBERTO JAVIER
CARDENAS CERVANTES NANCY GUADALUPE
ZAMORA SANCHEZ MARIA ELIZABETH
PEREZ GARCIA JOSE NATHANAEL
ROMERO ALVAREZ VALERY RUBI
RODRIGUEZ HURTADO YESENIA ITZEL
ESCANUELA GAMEZ SARAHI
GUTIERREZ VILLALOBOS ABDIEL ALEJANDRO
SORIA ENRIQUEZ SELENE GUADALUPE
LIZARDI ALCARAZ JORGE IVAN
"""


def poner_guiones(str): #esta funcion agrega guiones bajos en lugar de espacios y el dominip
  nombres_con_guion=str.replace(" ","_")
  nombres_listos=nombres_con_guion.replace("\n","@educacionguadalajara.mx \n")
  lista_de_correos = nombres_listos.split('\n')  # estas lineas de aqui basicamente crean la lista de correos
  return enumerate(lista_de_correos,254) #en el caso de los nuevos correos agregar el segundo parametro de enumerate


for count,element in poner_guiones(nombres):
    print(str(count)+'_'+element)



def separar_nombre_apellidos(str):
  pass