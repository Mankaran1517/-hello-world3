'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
'''
# A_V_calc.py
# Mankaran Singh Chattha
# 100944566
# TPRG-2131

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the volume of a cube
def calculate_cube_volume(side):
    return side ** 3

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    return 3.14159 * radius ** 2 * height

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    return (4/3) * 3.14159 * radius ** 3

def main():
    while True:  # Outer loop to keep returning to the main menu
        # Display view options
        print("A/V Calculator Menu")
        print("Press Q/q to exit the application.")
        print("Press D/d for Detailed view or V/v for Simple view.")
        view_mode = input("Please select a view mode (D/d or V/v): ")
        while view_mode.lower() not in ['d', 'v']:
            view_mode = input("Invalid input. Please select a view mode (D/d or V/v): ")
        view_mode = 'detailed' if view_mode.lower() == 'd' else 'simple'

        # Display menu options
        while True:
            print("\nSelect a calculation:")
            print("1. Circle Area")
            print("2. Rectangle Area")
            print("3. Cube Volume")
            print("4. Cylinder Volume")
            print("5. Sphere Volume")
            print("6. Return to Calculator Menu")

            choice = input("Please enter your choice: ")
            if choice.lower() == 'q':
                print("Exiting the application. Goodbye!")
                return  # Exit the application
            elif choice == '6':
                print("Returning to Calculator Menu...")
                break  # Break to the outer loop to restart the menu
            else:
                # Handle calculations based on choice
                if choice == '1':
                    # Calculate circle area
                    radius = float(input("Enter radius: "))
                    result = calculate_circle_area(radius)
                    display_result(result, "Circle Area = π * r^2", view_mode)
                elif choice == '2':
                    # Calculate rectangle area
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    result = calculate_rectangle_area(length, width)
                    display_result(result, "Rectangle Area = length * width", view_mode)
                elif choice == '3':
                    # Calculate cube volume
                    side = float(input("Enter side length: "))
                    result = calculate_cube_volume(side)
                    display_result(result, "Cube Volume = side^3", view_mode)
                elif choice == '4':
                    # Calculate cylinder volume
                    radius = float(input("Enter radius: "))
                    height = float(input("Enter height: "))
                    result = calculate_cylinder_volume(radius, height)
                    display_result(result, "Cylinder Volume = π * r^2 * height", view_mode)
                elif choice == '5':
                    # Calculate sphere volume
                    radius = float(input("Enter radius: "))
                    result = calculate_sphere_volume(radius)
                    display_result(result, "Sphere Volume = (4/3) * π * r^3", view_mode)
                else:
                    # Handle invalid user input
                    print("Invalid choice. Please try again.")

def display_result(result, equation, view_mode):
    if view_mode == 'detailed':
        print(f"{result} ({equation})")
    else:
        print(result)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()


