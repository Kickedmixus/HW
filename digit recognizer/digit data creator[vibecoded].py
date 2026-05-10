import tkinter as tk
import json
import os

GRID_SIZE = 16
PIXEL_SIZE = 25
MAX_BRIGHTNESS = 100
FILE_NAME = "digits_dataset.json"

class DigitDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Drawer")

        self.label = tk.Label(root, text="Draw with left click. Right click = erase. Click a number to save.")
        self.label.pack()

        self.canvas = tk.Canvas(
            root,
            width=GRID_SIZE * PIXEL_SIZE,
            height=GRID_SIZE * PIXEL_SIZE,
            bg="black"
        )
        self.canvas.pack()

        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.rects = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        self.draw_grid()

        # Mouse bindings
        self.canvas.bind("<Button-1>", self.draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.canvas.bind("<Button-3>", self.erase)
        self.canvas.bind("<B3-Motion>", self.erase)

        # Buttons for digits
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        for i in range(10):
            b = tk.Button(btn_frame, text=str(i), command=lambda n=i: self.save_digit(n))
            b.grid(row=0, column=i)

        # Clear button
        clear_btn = tk.Button(root, text="Clear", command=self.clear_grid)
        clear_btn.pack()

    def draw_grid(self):
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = self.canvas.create_rectangle(
                    x * PIXEL_SIZE,
                    y * PIXEL_SIZE,
                    (x + 1) * PIXEL_SIZE,
                    (y + 1) * PIXEL_SIZE,
                    fill="black",
                    outline="gray"
                )
                self.rects[y][x] = rect

    def update_pixel(self, x, y):
        brightness = self.grid[y][x]
        gray = int(255 * (brightness / MAX_BRIGHTNESS))
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        self.canvas.itemconfig(self.rects[y][x], fill=color)

    def draw(self, event):
        x = event.x // PIXEL_SIZE
        y = event.y // PIXEL_SIZE

        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            self.grid[y][x] = min(MAX_BRIGHTNESS, self.grid[y][x] + 20)
            self.update_pixel(x, y)

    def erase(self, event):
        x = event.x // PIXEL_SIZE
        y = event.y // PIXEL_SIZE

        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            self.grid[y][x] = max(0, self.grid[y][x] - 20)
            self.update_pixel(x, y)

    def save_digit(self, label):
        # Normalize to 0–1
        normalized_grid = [
            [value / MAX_BRIGHTNESS for value in row]
            for row in self.grid
        ]

        data_entry = {
            "label": label,
            "grid": normalized_grid
        }

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = []
        else:
            data = []

        data.append(data_entry)

        with open(FILE_NAME, "w") as f:
            json.dump(data, f)

        print(f"Saved digit {label}")
        self.clear_grid()

    def clear_grid(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.update_pixel(x, y)


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitDrawer(root)
    root.mainloop()