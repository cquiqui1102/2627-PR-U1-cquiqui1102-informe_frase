## 1. Informe de una frase
**Desarrolla un programa que lea una frase y muestre una versión normalizada junto con algunos datos sobre ella.**

---

## Funciones que debes implementar:

**preparar_texto(frase):** elimina los espacios de los extremos y convierte el texto a minúsculas. Devuelve el texto preparado.

**analizar_texto(frase):** recibe el texto preparado y devuelve una tupla con tres datos: número de caracteres —incluidos los espacios interiores—, número de palabras y si contiene la palabra completa "python". Para obtener las palabras, utiliza split().

La función **main()** debe leer la frase, llamar a **preparar_texto()** y comprobar si el resultado está vacío. Si está vacío, mostrará un mensaje de error. En caso contrario, llamará a **analizar_texto()**, desempaquetará la tupla y mostrará el informe.

---

## Ejemplo:

**Entrada:**<br>
  Aprender PYTHON es divertido<br>  

**Salida:**<br>
Texto: aprender python es divertido<br>
Caracteres: 28<br>
Palabras: 4<br>
Contiene la palabra python: sí<br>

Puedes suponer que las palabras están separadas por espacios y que la frase no contiene signos de puntuación.

---

## Requisitos

- Añade anotaciones de tipo a los parámetros, retornos y variables principales.<br>
- Documenta las funciones auxiliares mediante docstrings con :param y :return.<br>
- Gestiona la entrada y la salida en main(); las funciones auxiliares devuelven sus resultados con return.<br>
- Incluye la guarda de ejecución.<br>

Entrega un repositorio PÚBLICO con el nombre **2627-PR-U1-usarioPasen-informe_frase** y tu solución.

---

## Ejecutado

El programa indica a la perfección los requerimientos.

![Si](imagen/resultado1.png)

![No](imagen/resultado2.png)