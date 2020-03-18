dict_country = {

    "es": "España",
    "ec": "Ecuador",
    "mx": "México",
    "pe": "Perú",
    "co": "Colombia",
    "ve": "venezuela"
}

paises = [

    "España",
    "Ecuador",
    "México",
    "Perú",
    "Colombia",
    "venezuela"
]


ordenado = sorted(dict_country.items())
print("order: ", ordenado, " \n")

ordenado = sorted(paises, reverse=True)
print("order: ", ordenado, " \n")


#Tradicional filter + function filtrado

def filtro(elemento):
    return elemento >= 10

#lambda
filtro_2 = lambda arg: arg >= 10

numeros = [1, 10, 15, 25, 3]

for item in filter(filtro_2, numeros):
    print(item)

