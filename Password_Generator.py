import random
def juego():
    letras = ["1","2","3","4","5","6","7","8","9","0", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","x","y","z"]
    mayusc = ["1","2","3","4","5","6","7","8","9","0", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","x","y","z"]
    números = ["1","2","3","4","5","6","7","8","9","0", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","x","y","z"]
    for i in range(0, 1):
        pc_letras = random.choice(letras)
        pc_num = random.choice(números)
        pc_mayusc = random.choice(mayusc)
        resultado = str(pc_letras)
        resultado1 = str(pc_num)
        resultado2 = str(pc_mayusc)
        x = print(resultado + resultado1 + resultado2)
def número():
    for i in range(0, 1):
        total = juego()
        return total
for i in range(0, 10):
    lista1 = []
    x = número()
    lista1.append(x)
    
