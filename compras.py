lista_compras = []

while True:
    productos = input("Ingrese el nombre del producto(o 'Terminar'para finalizar): ")
    if productos == 'Terminar' :
        break
    else:
        lista_compras.append(productos)

print ("-----lista de compras-----")
for productos in lista_compras:
    print(productos)
    





