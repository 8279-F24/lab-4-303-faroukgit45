# Import Circuit Playground library
from adafruit_circuitplayground import cp

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Setup for manual LED control
cp.pixels.auto_write = False
cp.pixels.brightness = 0.3  # Default brightness

# Main loop: runs until the user chooses to quit
while True:
    # Display menu and get user choice
    print("Choose a color for the LEDs:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("Press 'q' to quit")

    choice = input("Enter your choice: ")

    # Quit if user enters 'q'
    if choice.lower() == 'q':
        print("Exiting program.")
        break

    # Try to convert input to an integer and update LED color
    try:
        choice = int(choice)
        if choice == 1:
            cp.pixels.fill(red)
        elif choice == 2:
            cp.pixels.fill(green)
        elif choice == 3:
            cp.pixels.fill(blue)
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number or 'q' to quit.")

    # Show LEDs with selected color
    cp.pixels.show()
