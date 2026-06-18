"""Módulo calculadora.

Provee operaciones aritméticas básicas (suma, resta, multiplicación y
división) usadas como proyecto de ejemplo para el taller de Integración
Continua con GitHub Actions.
"""


def suma(a, b):
    """Retorna la suma de dos números.

    Args:
        a: Primer operando.
        b: Segundo operando.

    Returns:
        La suma de ``a`` y ``b``.
    """
    return a + b


def resta(a, b):
    """Retorna la resta de dos números.

    Args:
        a: Minuendo.
        b: Sustraendo.

    Returns:
        La diferencia entre ``a`` y ``b``.
    """
    return a - b


def multiplicacion(a, b):
    """Retorna el producto de dos números."""
    return a * b


def division(a, b):
    """Retorna la división de dos números.

    Raises:
        ValueError: Si ``b`` es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    """Punto de entrada: muestra ejemplos de cada operación."""
    print("Suma 5 + 3 =", suma(5, 3))
    print("Resta 10 - 4 =", resta(10, 4))
    print("Multiplicación 6 * 7 =", multiplicacion(6, 7))
    print("División 20 / 5 =", division(20, 5))


if __name__ == "__main__":
    main()
