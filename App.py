from Inventario import inventario
from Producto_no_perecedero import no_perecedero
from Producto import Producto
from Productoperecedero import producto_perecedero


class app: 
    def star (self) -> None: 
        print ("Bienvenido a tu sistema de gestión de Inventarios") 

    def create_producto(self,product_material:str ):
            nombre = input('Por favor ingrese el nombre del producto: ')
            precio = input('Por favor ingrese el precio del producto: ')
            Cantidad = input('Por favor ingrese la cantidad disponible en inventario: ') 
            fecha_de_expiración = input ('Por favor ingres la fecha de caducidad del producto (en caso de no tener colocar no aplica): ')
            product_material = None
            if product_material == 'Caducible':
                 product_material = producto_perecedero and Producto (nombre, precio, Cantidad, fecha_de_expiración)
                 self.productos.append(product_material)

            elif product_material == 'No caducible':
                     product_material = no_perecedero and Producto (nombre, precio, Cantidad, fecha_de_expiración)
                     self.create_producto.append(Producto)
            return product_material 
    
    def menu(self):
        ans = 'y'
        while ans == 'y':
            option = input('''
                1. Registrar producto
                2. Eliminar producto
                3. Buscar producto 
                4. Listar Productos resgistrados
            ''')  
            
            if option == '1':
                self.create_producto()
            elif option == '2':
                self.delete_producto()
            elif option == '3':
                # Buscar al producto 
                name = input('Por favor ingrese el nombre del producto: ')
                product = self.search_product(product, 'product')
                if isinstance(product, Producto):
                 self.add_product_to_producto(product)
                else:
                    print('Error...')
            elif option == '4':
    
                print('Error...')
            ans = input('Desea continuar (y/n)?: ').lower()

