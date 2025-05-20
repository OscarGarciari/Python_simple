import random
import string
product = []
print("=== Registro de 10 productos ===\n")
for i in range(1, 11):
    name = input(f"Ingrese el nombre del producto #{i}: ")
    code = "TIENDA-"
    for _ in range(4):
        code += random.choice(string.ascii_letters + string.digits)
    product.append((name, code))
print("\n=== Lista de productos registrados ===")
for i, item in enumerate(product, 1):
    print(f"{i}. Producto: {item[0]} - Código: {item[1]}")