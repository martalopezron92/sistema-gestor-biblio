def prestamos(libro, usuario, fecha_prestamo, fecha_devolucion, isbn):
    """
    Crea un diccionario que representa un préstamo de libro con el libro prestado, el usuario,
    la fecha de préstamo y la fecha de devolución.

    Parámetros:
    libro (dict): Un diccionario que representa el libro prestado.
    usuario (str): El nombre del usuario que realiza el préstamo.
    fecha_prestamo (str): La fecha en que se realizó el préstamo.
    fecha_devolucion (str): La fecha en que se debe devolver el libro.

    Retorna:
    dict: Un diccionario con las claves 'libro', 'usuario', 'fecha_prestamo' y 'fecha_devolucion'.
    pequeño cambio
    
    """
    return {
        'libro': libro,
        'usuario': usuario,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion': fecha_devolucion
    }