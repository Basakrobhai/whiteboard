def validate_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Coordinates must be numeric values.")
    return x, y

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)