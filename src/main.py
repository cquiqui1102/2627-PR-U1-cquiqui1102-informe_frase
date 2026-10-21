# Desarrolla un programa que lea una frase y muestre una versión normalizada junto con algunos datos sobre ella.

def preparar_texto(frase: str) -> str:
    """
    Eliminar los espacios y convertir el texto a minúsculas.

    Args:
    frase = Frase introducida

    Returns:
    str = Frase completamente en minúsculas

    """

    frase_nueva1: str = frase.strip().lower()

    return frase_nueva1



def analizar_texto(frase: str) -> tuple[int, int, str]:
    """
    Contar el número de caracteres, el número de palabras y si contiene o no la palabra 'python'.

    Args:
    frase = Frase ya preparada

    Returns:
    tuple[int, int, str] = Número de caracteres, Número de palabras, Si contiene o no la palabra 'python'
    
    """

    frase_nueva1: str = preparar_texto(frase)

    numero_caracteres: int = len(frase_nueva1[:])

    palabras: list[str] = frase_nueva1.split()
    numero_palabras: int = len(palabras)

    if "python" in palabras:
        palabra_python = "Sí"
    else:
        palabra_python = "No"

    return numero_caracteres, numero_palabras, palabra_python
    


def main():
    """
    Función principal:
    Solicita al usuario una frase y muestra ese texto en minúsculas, el número de caracteres, el número de palabras y si contiene o no la palabra 'python'.
    
    """

    # Entrada

    frase: str = input()

    # Salida

    if not preparar_texto(frase):
        print("ERROR - La frase introducida está vacía.")
    else:
        numero_caracteres, numero_palabras, palabra_python = analizar_texto(frase)
        
        print(f"Texto: {preparar_texto(frase)}")
        print(f"Caracteres: {numero_caracteres}")
        print(f"Palabras: {numero_palabras}")
        print(f"Contiene la palabra 'python': {palabra_python}")

if __name__ == "__main__":
    main()