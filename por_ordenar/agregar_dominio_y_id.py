
#def agregar_dominio_a_correos(nombre,dominio):




nombres="""
SANCHEZ ALEMAN SANDRA PAOLA
DELGADILLO GONZALEZ LAURA ANAHI
MOLINA SALDAÑA CARLOS ALBERTO
PEREZ ARAUJO HANIEL ARELI
TRIGUEROS HERNANDEZ MARCOS JAVIER
GONZALEZ RODRIGUEZ HECTOR DE JESUS
MARTINEZ IBAÑEZ ADRIAN NATHANAEL
BRAVO LEMUS GUADALUPE
DIAZ MORENO ANGELA AIMEÉ
VARINDER X
PEREZ MACIAS CRISTOPHER ALEXANDER
CALDERA LUJANO LAURA GEORGINA
JAIME BARAJAS HUGO RICARDO
TORRES DE LEON ALBERTO ARTURO
RIVERA ARRIAGA LESLE GABRIELA
ORNELAS CHAVEZ ROSIO ADRIANA
RODRIGUEZ DELGADILLO BRENDA GUADALUPE
SANDOVAL VAZQUEZ CLAUDIA ELIZABETH
ACEVEDO VILLEGAS ERENDIRA IVONNE
ALVAREZ PEREZ ESTAFANI YAZMIN
YAÑEZ FABIAN FERNANDO
MENDOZA ZEPEDA FRANCISCO DE JESUS
COVARRUBIAS RAMIREZ GUADALUPE AZUCENA
ALVAREZ LOPEZ IVETTE
ALVAREZ GUZMAN LUIS ERNESTO
ARREOLA RUVALCABA MARCO ANTONIO
PONCE TISCAREÑO MARIA IRENE
ALVAREZ LOPEZ OSCAR
ROMERO VILLALPANDO OSCAR
LEDEZMA FABIAN RODOLFO
CORONEL VELAZCO SILVERIO
OROZCO ALVAREZ VICTOR EFRAIN
OROZCO ALVAREZ VIRIDIANA ARIZVETTE
BUGARIN MARTINEZ ALEJANDRA
JARAMILLO REYES CARLOS ALBERTO
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