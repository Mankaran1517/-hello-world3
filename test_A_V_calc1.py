'''
TPRG 2131 Fall 202x Assignment 1, Test file template.
Sept, 202x
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''
# test_A_V_calc.py

# test_A_V_calc.py

# Import the pytest module for unit testing
import pytest

# Import functions from A_V_calc module
from A_V_calc_starter(MANK) import (
    calculate_circle_area,
    calculate_rectangle_area,
    calculate_cube_volume,
    calculate_cylinder_volume,
    calculate_sphere_volume,
    display_result
)
# Test the calculate_circle_area function
def test_calculate_circle_area():
    """
    Test the calculate_circle_area function.
    Equation: A = πr^2 (Source: https://www.mathopenref.com/circlearea.html)
    """
    assert calculate_circle_area(1) == pytest.approx(3.14159, rel=1e-5)
    assert calculate_circle_area(0) == 0
    assert calculate_circle_area(2) == pytest.approx(12.56636, rel=1e-5)
# Test the calculate_rectangle_area function
def test_calculate_rectangle_area():
    """
    Test the calculate_rectangle_area function.
    Equation: A = lw (Source: https://www.mathopenref.com/rectanglearea.html)
    """
    assert calculate_rectangle_area(2, 3) == 6
    assert calculate_rectangle_area(0, 5) == 0
    assert calculate_rectangle_area(4, 5) == 20

# Test the calculate_cube_volume function
def test_calculate_cube_volume():
    """
    Test the calculate_cube_volume function.
    Equation: V = s^3 (Source: https://www.mathopenref.com/cubevolume.html)
    """
    assert calculate_cube_volume(1) == 1
    assert calculate_cube_volume(0) == 0
    assert calculate_cube_volume(3) == 27

# Test the calculate_cylinder_volume function
def test_calculate_cylinder_volume():
    """
    Test the calculate_cylinder_volume function.
    Equation: V = πr^2h (Source: https://www.mathopenref.com/cylindervolume.html)
    """
    assert calculate_cylinder_volume(1, 1) == pytest.approx(3.14159, rel=1e-5)
    assert calculate_cylinder_volume(0, 5) == 0
    assert calculate_cylinder_volume(2, 3) == pytest.approx(37.69908, rel=1e-5)

# Test the calculate_sphere_volume function
def test_calculate_sphere_volume():
    """
    Test the calculate_sphere_volume function.
    Equation: V = (4/3)πr^3 (Source: https://www.mathopenref.com/spherevolume.html)
    """
    assert calculate_sphere_volume(1) == pytest.approx(4.18879, rel=1e-5)
    assert calculate_sphere_volume(0) == 0
    assert calculate_sphere_volume(3) == pytest.approx(113.09724, rel=1e-5)


# Test the display_result function
def test_display_result():
    """
    Test the display_result function.
    This function does not return a value, so we will not validate its output here.
    """
    # Testing display_result function by checking if it runs without errors
    assert display_result(10, "Test equation", "simple") is None
    assert display_result(10, "Test equation", "detailed") is None

# Run pytest if this script is executed directly
if __name__ == "__main__":
    pytest.main()