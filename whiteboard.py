"""Contains whiteboard functionality."""
import tkinter as tk
from tkinter.colorchooser import askcolor

class Whiteboard:
    """Whiteboard class."""
    def __init__(self, window):
        """Initialize the whiteboard."""
        self.window = window
        self.window.title("Whiteboard App")
        self.canvas = tk.Canvas(window, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.is_drawing = False
        self.drawing_color = "black"
        self.line_width = 2
        self.prev_x = None
        self.prev_y = None

        self.setup_ui()

    def setup_ui(self):
        """Setup the UI."""
        controls_frame = tk.Frame(self.window)
        controls_frame.pack(side="top", fill="x")

        color_button = tk.Button(controls_frame, text="Change Color", command=self.change_pen_color)
        clear_button = tk.Button(controls_frame, text="Clear Canvas", command=self.clear_canvas)

        color_button.pack(side="left", padx=5, pady=5)
        clear_button.pack(side="left", padx=5, pady=5)

        line_width_label = tk.Label(controls_frame, text="Line Width:")
        line_width_label.pack(side="left", padx=5, pady=5)

        self.line_width_slider = tk.Scale(
            controls_frame,
            from_=1,
            to=10,
            orient="horizontal",
            command=self.change_line_width,
        )
        self.line_width_slider.set(self.line_width)
        self.line_width_slider.pack(side="left", padx=5, pady=5)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def start_drawing(self, event):
        """Start drawing."""
        self.is_drawing = True
        self.prev_x, self.prev_y = event.x, event.y

    def draw(self, event):
        """Draw the line."""
        if self.is_drawing:
            current_x, current_y = event.x, event.y
            self.canvas.create_line(
                self.prev_x,
                self.prev_y,
                current_x,
                current_y,
                fill=self.drawing_color,
                width=self.line_width,
                capstyle=tk.ROUND,
                smooth=True,
            )
            self.prev_x, self.prev_y = current_x, current_y

    def stop_drawing(self, _):
        """Stop drawing."""
        self.is_drawing = False

    def change_pen_color(self):
        """Change the color of the pen."""
        color = askcolor()[1]
        if color:
            self.drawing_color = color

    def change_line_width(self, value):
        """Change the line width of the canvas."""
        self.line_width = int(value)

    def clear_canvas(self):
        """Clear the canvas."""
        self.canvas.delete("all")

root = tk.Tk()
root.geometry("800x600")
app = Whiteboard(root)
root.mainloop()
