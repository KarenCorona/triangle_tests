import pytest
from triangle.area import calculate_area

def test_area_calculation():
    """Test that area is calculated correctly with valid inputs."""
    assert calculate_area(5, 7) == 17.5

def test_negative_base():
    """Test that negative base raises ValueError."""
    with pytest.raises(ValueError):
        calculate_area(-5, 7)

def test_negative_height():
    """Test that negative height raises ValueError."""
    with pytest.raises(ValueError):
        calculate_area(5, -7)

def test_zero_base():
    """Test that zero base raises ValueError."""
    with pytest.raises(ValueError):
        calculate_area(0, 7)

def test_zero_height():
    """Test that zero height raises ValueError."""
    with pytest.raises(ValueError):
        calculate_area(5, 0)

def test_negative_both():
    """Test that negative base and height raises ValueError."""
    with pytest.raises(ValueError):
        calculate_area(-5, -7)