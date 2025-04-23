import tkinter as tk
from utils.helpers import validate_input
from services.drawing_service import DrawingService

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard Application")
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()
        
        self.drawing_service = DrawingService(self.canvas)
        
        self.setup_ui()

    def setup_ui(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_clear = tk.Button(toolbar, text="Clear", command=self.clear_board)
        btn_clear.pack(side=tk.LEFT)

        btn_save = tk.Button(toolbar, text="Save", command=self.save_board)
        btn_save.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        # Example of adding a shape on click
        if validate_input(event.x, event.y):
            self.drawing_service.add_shape(event.x, event.y)

    def clear_board(self):
        self.drawing_service.clear_board()

    def save_board(self):
        self.drawing_service.save_state()

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()