def sumar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Ambos argumentos deben ser números enteros"
    return a + b

def restar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Ambos argumentos deben ser números enteros"
    return a - b

def multiplicar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Ambos argumentos deben ser números enteros"
    return a * b

def dividir(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Ambos argumentos deben ser números enteros"
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

if __name__ == "__main__":
 print(sumar(5, 3))
 print(restar(5, -3))
 print(multiplicar(5, -3))
 print(dividir(5, 0))