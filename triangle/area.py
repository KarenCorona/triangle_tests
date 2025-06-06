def calculate_area(base: float, height: float) -> float:
    """Calculate the area of a triangle."""
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return (base * height) / 2