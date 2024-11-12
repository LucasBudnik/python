'''Actualización del inventario a partir de un arreglo '''

'''
En una tienda, es necesario actualizar el inventario cuando se venden productos. A continuación, te
proporcionamos un arreglo con una lista de productos, donde cada producto tiene un código, una descripción y
una cantidad en stock. Escribí un programa que permita:

Seleccionar un producto a partir de su código.

Ingresar la cantidad vendida (que debe ser mayor que cero).

Actualizar la cantidad en stock de ese producto restando la cantidad vendida.

tienda
cod
descripción
stock

buscar por codigo
ingresar cantidad vendida validar stock
actualizar stock

'''

# Inicializar el inventario

inventary = []
print("Optional Keys\n\n")
print("0. to exit")
print("1. add product")
print("2. search product")
print("3. Sale Product")
key = int(input("select an option (FIN=0): "))

while( key != 0):
##################################################
    # adding product
    if (key == 1):
        code = int(input("Input code: ")) 
        description = input("Input description: ")
        stock = int(input("Input stock: "))
        # valide stock
        while(stock <= 0):
            stock = int(input("Input stock: "))
            if(stock <= 0):
                print("stock must be greater than 0")

        product = [code, description, stock]
        inventary.append(product)
##################################################
    # searching product
    elif(key == 2):
        if len(inventary) == 0 : 
            print("No products in the inventary")
        else:
            search = True
            while(search):
                code = int(input("input searching code: "))
                index = 0
                formerIndex = 0
                product = inventary[index]
                currentCode = product[0]
                while(code != currentCode)and(index < len(inventary)):
                    product = inventary[index]
                    currentCode = product[0]
                    formerIndex = index
                    index += 1
                if (currentCode  == code):
                    print("Product found")
                    print("Description: ", product[1])
                    print("Stock: ", product[2])
                    print("Position: ", formerIndex)
                else:
                    print("Product not found")
                answer = input("Do you want to keep searching? (Y/N)")
                if (answer == 'n') or (answer == 'N'):
                    search = False
            

##################################################
    # sold product    
    elif(key == 3):
        print("Do you have product Position? ")
        answer = input("Y/N: ")
        if (answer == 'y') or (answer == 'Y'):
            position = int(input("Insert Product Position: "))
            while (position > len(inventary))or(position < 0):
                position = int(input("Try with other position: "))
                if(position > len(inventary))or(position < 0):
                    print("Position must be between 0 and", len(inventary))
            stock = int(input("Insert number of products sold: "))
            while(stock > inventary[position][2])or(stock <= 0):
                stock = int(input("Try with other number of products sold: "))
                if(stock > inventary[position][2])or(stock <= 0):
                    print("Number of products sold must be greater than 0 and less than the stock")
            inventary[position][2] -= stock
        else:
            print("Try searching position (key=2 on menu options) and return to sold product option (key = 3)")
##################################################
    
    
    else:
        print("Invalid option.\n")

    print("Optional Keys\n\n")
    print("0. to exit")
    print("1. add product")
    print("2. search product")
    print("3. Sale Product")
    key = int(input("select an option (FIN=0): "))
##################################################


print("You select exit option ...")
print("########################")
