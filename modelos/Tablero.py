from modelos.Ficha import Ficha


class Tablero:
    def __init__(self):
        #Matriz de 7 casillas de ancho y 6 de alto
        self.tablero = []
        for i in range(6):
            self.tablero.append([Ficha.VACIO]*7)

    def comprobar_ganador(self, fila: int, columna: int) -> bool:
        # Ficha del jugador actual
        ficha_actual = self.tablero[fila][columna]

        # Comprobamos si hay 4 en línea en horizontal (↔)
        contador = 0
        for col in range(7):  # Iteramos sobre las columnas de la fila
            if self.tablero[fila][col] == ficha_actual:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Comprobamos si hay 4 en línea en vertical (↕)
        contador = 0
        for fil in range(6):  # Iteramos sobre las filas de la columna
            if self.tablero[fil][columna] == ficha_actual:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Comprobamos si hay 4 en línea en diagonal ↘
        contador = 0
        dif = columna - fila  # Diferencia entre columna y fila
        for offset in range(max(-fila, -columna), min(6 - fila, 7 - columna)):  # Rango válido para ↘
            if self.tablero[fila + offset][columna + offset] == ficha_actual:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Comprobamos si hay 4 en línea en diagonal ↗
        contador = 0
        suma = fila + columna  # Suma entre columna y fila
        for offset in range(max(-fila, columna - 6), min(6 - fila, columna + 1)):  # Rango válido para ↗
            if self.tablero[fila + offset][columna - offset] == ficha_actual:
                contador += 1
                if contador == 4:
                    return True
            else:
                contador = 0

        # Si ninguna condición se cumple, no hay ganador
        return False