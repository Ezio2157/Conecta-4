import tkinter as tk
from tkinter import messagebox

from modelos.Ficha import Ficha
from modelos.Tablero import Tablero

ROWS = 6
COLS = 7


class Conecta4:
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta 4")

        # Estado del juego
        self.board = Tablero()
        self.current_player = "🔴"  # Jugador 1

        # Contadores de victorias
        self.red_wins = 0
        self.yellow_wins = 0

        self.create_ui()

    def create_ui(self):
        # Contadores de victorias
        self.score_label = tk.Label(
            self.root, text=f"Rojo: {self.red_wins}\tAmarillo: {self.yellow_wins}", font=("Arial", 14)
        )
        self.score_label.grid(row=0, column=0, columnspan=COLS, pady=5)

        # Botones para colocar fichas
        self.buttons = []
        for col in range(COLS):
            button = tk.Button(self.root, text="⬇", command=lambda c=col: self.drop_token(c))
            button.grid(row=1, column=col, padx=5, pady=5)
            self.buttons.append(button)

        # Tablero gráfico
        self.canvas = tk.Canvas(self.root, width=COLS * 60, height=ROWS * 60, bg="blue")
        self.canvas.grid(row=2, column=0, columnspan=COLS, padx=10, pady=10)

        # Dibujar el tablero gráfico
        self.oval_grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * 60 + 5
                y1 = row * 60 + 5
                x2 = x1 + 50
                y2 = y1 + 50
                self.oval_grid[row][col] = self.canvas.create_oval(x1, y1, x2, y2, fill="white")

    def drop_token(self, col):
        for row in reversed(range(ROWS)):
            if self.board.tablero[row][col] == Ficha.VACIO:  # Verifica el estado lógico
                # Actualiza el estado lógico
                self.board.tablero[row][col] = self.current_player

                # Actualiza el tablero gráfico
                color = "red" if self.current_player == "🔴" else "yellow"
                self.canvas.itemconfig(self.oval_grid[row][col], fill=color)

                # Comprobar si hay un ganador
                if self.check_winner(row, col):
                    if self.current_player == "🔴":
                        self.red_wins += 1
                        messagebox.showinfo("¡Victoria!", "¡El jugador Rojo gana!")
                    else:
                        self.yellow_wins += 1
                        messagebox.showinfo("¡Victoria!", "¡El jugador Amarillo gana!")

                    # Actualizar el contador de victorias
                    self.update_score_label()
                    self.reset_board()
                else:
                    # Cambiar turno
                    self.current_player = "🟡" if self.current_player == "🔴" else "🔴"
                return

        # Si no hay espacio en la columna
        messagebox.showwarning("Columna llena", "¡Esa columna está llena!")

    def check_winner(self, row, col):
        return self.board.comprobar_ganador(row, col)

    def reset_board(self):
        # Restablecer el estado lógico
        self.board = Tablero()

        # Restablecer el estado gráfico
        for row in range(ROWS):
            for col in range(COLS):
                self.canvas.itemconfig(self.oval_grid[row][col], fill="white")
        self.current_player = "🔴"

    def update_score_label(self):
        # Actualiza la etiqueta de puntuación
        self.score_label.config(text=f"Rojo: {self.red_wins} | Amarillo: {self.yellow_wins}")


# Crear la ventana
root = tk.Tk()
game = Conecta4(root)
root.mainloop()
