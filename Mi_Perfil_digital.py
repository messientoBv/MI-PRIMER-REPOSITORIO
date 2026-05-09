#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Luis Eduardo Niño Gomez"
edad = 14
estatura = 1.65
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("messientoBv", "nin.x07")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Casita Vieja", "artista": "Dario Gomez", "duracion": "3:01"},
{"titulo": "MR.Trance", "artista": "Esteman", "duracion": "2:49"},
{"titulo": "De la vida como una película, tragedia, comedia y ficción", "artista": "Cancerbero", "duracion": "8:01"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
for cancion in Playlist:
    print(f"{cancion['titulo']} - {cancion['artista']} ({cancion['duracion']}) min")
print ("----------------------------------")