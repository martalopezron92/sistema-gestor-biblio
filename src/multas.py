def multas(libro, dias_atraso, usuario):
    tarifa_diaria = 0.50  # Tarifa fija por día de atraso
    multa_total = dias_atraso * tarifa_diaria
    return multa_total