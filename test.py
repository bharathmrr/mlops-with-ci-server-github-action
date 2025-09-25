import pytest

def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x**2

def cube(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x**3

def fifth(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return x**5

def test_square():
    assert square(2) == 4, "test failed: square of 2 should be 4"
    assert square(3) == 9, "test failed: square of 3 should be 9"
    assert square(-2) == 4, "test failed: square of -2 should be 4"
    assert square(0) == 0, "test failed: square of 0 should be 0"
    assert square(2.5) == 6.25, "test failed: square of 2.5 should be 6.25"

def test_cube():
    assert cube(2) == 8, "test failed: cube of 2 should be 8"
    assert cube(3) == 27, "test failed: cube of 3 should be 27"
    assert cube(-2) == -8, "test failed: cube of -2 should be -8"
    assert cube(0) == 0, "test failed: cube of 0 should be 0"
    assert cube(2.5) == 15.625, "test failed: cube of 2.5 should be 15.625"

def test_fifth():
    assert fifth(2) == 32, "test failed: fifth power of 2 should be 32"
    assert fifth(1) == 1, "test failed: fifth power of 1 should be 1"
    assert fifth(-2) == -32, "test failed: fifth power of -2 should be -32"
    assert fifth(0) == 0, "test failed: fifth power of 0 should be 0"
    assert fifth(2.5) == 97.65625, "test failed: fifth power of 2.5 should be 97.65625"

def test_invalid_input():
    with pytest.raises(TypeError):
        square('string')
    with pytest.raises(TypeError):
        cube('string')
    with pytest.raises(TypeError):
        fifth('string')
    with pytest.raises(TypeError):
        square([1, 2, 3])
    with pytest.raises(TypeError):
        cube(None)