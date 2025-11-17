def buscar_libro(titulo, libros):
    """
    Busca un libro por su título en una lista de libros.

    Parámetros:
    titulo (str): El título del libro a buscar.
    libros (list): Una lista de diccionarios que representan los libros.

    Retorna:
    dict o None: El diccionario del libro si se encuentra, de lo contrario None.
    """
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            return libro
    return None

def buscar_por_autor(autor, libros):
    """
    Busca libros por su autor en una lista de libros.

    Parámetros:
    autor (str): El nombre del autor cuyos libros se desean buscar.
    libros (list): Una lista de diccionarios que representan los libros.

    Retorna:
    list: Una lista de diccionarios de los libros escritos por el autor especificado.
    """
    resultados = []
    for libro in libros:
        if libro['autor'].lower() == autor.lower():
            resultados.append(libro)
    return resultados