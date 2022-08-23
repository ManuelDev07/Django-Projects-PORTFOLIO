#Dentro de este archivo nuevo estarán todas las funciones que tendrá el carrito de compras mediante el uso de una clase (P.O.O):
#Este carrito de cmpras también tiene que tener una sesión con sus prodcuctos dentro, la cual se mantedrá así el usuario se salga o no de la tienda o vaya a otra página dentro de esta
#Dentro de este archivo nuevo estarán todas las funciones que tendrá el carrito de compras mediante el uso de una clase (P.O.O):
#Este carrito de cmpras también tiene que tener una sesión con sus prodcuctos dentro, la cual se mantedrá así el usuario se salga o no de la tienda o vaya a otra página dentro de esta
class Shopping_Cart_Class:
    #Esta clase tendrá un constructor que inicie las tareas más importantes como:
    #Tengo que detectar el request/petición para acceder al carro
    #tengo que construir la sesión y el carro
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart') #creo el carrito con la sesión del usuario y el nombre entre ()

        #se verifica si el carrito se ha creado o no, para asi crearlo y mantener tanto su sesión abierta como su contenido almacenado
        if not cart:
            cart = self.session['cart'] = {} #Se crea el carrito donde su contenido será almacenado en un dict. 
            #En este dict la key será el 'id' del producto y su value será otro dict con las características del producto.
            self.cart = self.session['cart']

        else: #Caso contrario si ya está creado, que su contenido y sesión se mantenga para seguir modificando su contenido desde otro lugar o si se ha ido de la página
            self.cart = cart

    def save_products(self):#Este función ACTUALIZARÁ/GUARDARÁ los datos en la sesión del carrito luego de cada acción realizada en el carrito
        self.session['cart'] = self.cart
        self.session.modified = True 

    def add_product(self, product):#Función para AGREGAR productos al carrito
        #Tengo que verificar si el producto (su id) ya ha sido agregado o no al carrito para que no se repita:
        if (str(product.id) not in self.cart.keys()):
            #Agrego el producto al carrito (al dict) con todos sus datos
            self.cart[product.id] = {
                'product_id':product.id, #su id
                #'image':product.image.url, #La imagen del producto (el url es para acceder a la carpeta donde se guardan las imágenes)
                'name':product.name, #su nombre
                'price':float(product.price), #su precio (se debe pasar como string)
                'quantity':1, #la cantidad de productos
            } 
        
        else: #Caso contrario si ya está el producto en el carrito, pues se agregará una unidad más de ese producto al carrito y el precio de ESE producto (no el total) irá aumentando según la cantidad
            #Se recorren todas las key:value, luego compruebo si la key corresponde al id del producto y si es existe en el carrito, aumento la cantidad de ese artículo:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    value['price'] = float(value['price']) + product.price 
                    break #Se deja de recorrer el dict al encontrarlo
        
        self.save_products() #Se guardan los datos y cambios hechos

    def delete_product(self, product): #Esta función ELIMINARÁ el producto del carrito. Recibirá obviamente el producto que quiero eliminar.
        product.id = str(product.id) #Almaceno el id en una variable

        if product.id in self.cart: #y verifico si el id está en el carrito de compras
            del self.cart[product.id] #Se elimina
            self.save_products() #Guardo los cambios en la sesión

    def discount_product(self, product): #Esta función RESTARÁ -1 la cantidad que haya de un producto en específico
        
        #Se hace la misma verificación que al agregar productos:
        #Recorro los pares key:value y compruebo si la key es del producto que está en el carrito y si es True se resta la cantidad de ese artículo
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity'] - 1
                value['price'] = float(value['price']) - product.price 
                
                #Si la cantidad del producto llega a ser 0 (cero) se eliminará del carrito de compras:
                if value['quantity'] < 1:
                    #Se llama la función de eliminar:
                    self.delete_product(product)

                break #Se deja de recorrer el dict al encontrarlo
            
        self.save_products() #Se guardan los datos y cambios hechos
    
    def clean_shopping_cart(self): #Esta función es para LIMPIAR todo el contenido del carrito
        self.session['cart'] = {} #Se vuelve a asignar un dict vacío (como cuando se creó el carrito en el constructor)

        self.session.modified = True 
