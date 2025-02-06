def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b <= 0:
        return None
    return a, b


OPERATIONS = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


if __name__ == "__main__":
    result = 0
    first_operand = 0
    second_operand = 0
    operation = None
    print("Calculadora para operaciones simples.(':q' para salir.)")
    while True:
        problem = input(">>> ")

        for char in problem:
            if char == " ":
                continue

        if problem == ":q":
            print("Saliendo...")
            break

        if not OPERATIONS.keys().__contains__(problem[1]):
            print(">>> operación no implementada o no válida.")
            continue
        else:
            operation = OPERATIONS[problem[1]]

        if problem[0] == "_":
            first_operand = result
        else:
            try:
                first_operand = float(problem[0])
            except ValueError:
                print(f"{problem[0]!r} no es un valor válido.")
                continue

        if problem[2] == "_":
            second_operand = result
        else:
            try:
                second_operand = float(problem[2])
            except ValueError:
                print(f"{problem[2]!r} no es un valor válido.")
                continue
        result = operation(first_operand, second_operand)
        print(result)
