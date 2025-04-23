class DrawingService:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def clear_board(self):
        self.shapes.clear()

    def save_state(self, filename):
        with open(filename, 'w') as file:
            for shape in self.shapes:
                file.write(f"{shape}\n")  # Assuming shape has a string representation

    def load_state(self, filename):
        with open(filename, 'r') as file:
            self.shapes = [line.strip() for line in file.readlines()]  # Assuming shapes can be reconstructed from string representation