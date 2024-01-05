import tkinter as tk
import random

class SnakeLaddersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladders Game")

        self.board_size = 10
        self.current_position = 1

        # Create game board
        self.create_board()

        # Create Dice Roll button
        tk.Button(root, text="Roll Dice", command=self.roll_dice).pack(pady=10)

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.cells = []
        for i in range(self.board_size, 0, -1):
            for j in range(1, self.board_size + 1):
                cell_value = i * self.board_size - (j - 1)
                cell = tk.Label(self.board_frame, text=str(cell_value), width=4, height=2, relief="ridge")
                cell.grid(row=self.board_size - i, column=j - 1)
                self.cells.append(cell)

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        self.move_player(dice_value)

    def move_player(self, steps):
        new_position = self.current_position + steps

        if new_position <= self.board_size ** 2:
            # Update player position on the board
            self.cells[self.current_position - 1].config(bg="white")
            self.cells[new_position - 1].config(bg="blue")

            # Check for Snake or Ladder
            new_position = self.check_snake_ladder(new_position)

            # Update current position
            self.current_position = new_position

            # Check for Win
            if new_position == self.board_size ** 2:
                tk.messagebox.showinfo("Congratulations!", "You reached the last cell! You win!")

    def check_snake_ladder(self, position):
        snake_ladder_dict = {
            16: 6, 47: 26, 49: 11, 56: 53,
            62: 19, 64: 60, 87: 24, 93: 73,
            95: 75, 98: 78
        }

        if position in snake_ladder_dict:
            new_position = snake_ladder_dict[position]
            tk.messagebox.showinfo("Snake or Ladder", f"You hit a Snake or Ladder! Move to cell {new_position}.")
            return new_position

        return position

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLaddersGame(root)
    root.mainloop()
