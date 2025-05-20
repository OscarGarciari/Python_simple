import random
import time 
shown_numbers = [] 
print("¡Bienvenido al BINGO!\n")
while len(shown_numbers) < 75:
    number = random.randint(1, 75)
    if number not in shown_numbers:
        shown_numbers.append(number)
        print("El numero es:", number)
        time.sleep(0.2)  
print("¡Ya se mostraron todos los números del 1 al 75!")