def libros(titulo, autor, anio_publicacion):
    """
    Crea un diccionario que representa un libro con su título, autor y año de publicación.

    Parámetros:
    titulo (str): El título del libro.
    autor (str): El autor del libro.
    anio_publicacion (int): El año de publicación del libro.

    Retorna:
    dict: Un diccionario con las claves 'titulo', 'autor' y 'anio_publicacion'.
    """
    return {
        'titulo': titulo,
        'autor': autor,
        'anio_publicacion': anio_publicacion
    }