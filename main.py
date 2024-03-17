import pyautogui
import time
from pynput import mouse
import math


def draw_circle(x_center, y_center, button, pressed):
    num_steps = 36  # Number of steps to draw the circle (more steps = smoother circle)

    # Calculate the angle between each step
    angle_step = 2 * math.pi / num_steps

    # Move the mouse to the starting position (without drawing)
    pyautogui.moveTo(x_center + radius, y_center)

    # Press the mouse to start drawing
    pyautogui.mouseDown()

    for step in range(num_steps + 1):
        # Calculate the x, y position of the next point
        x = x_center + radius * math.cos(step * angle_step)
        y = y_center + radius * math.sin(step * angle_step)

        # Move the mouse to the new position (this draws the segment)
        pyautogui.moveTo(x, y, duration=0.1)  # You can adjust the duration for smoother drawing

    # Release the mouse to stop drawing
    pyautogui.mouseUp()
    return False  # Stop the listener


def idle():
    while True:
        time.sleep(1)


def main():
    global radius

    # Get custom radius value
    while True:
        radius = input("Enter the desired radius: ")
        try:
            radius = int(radius)
            break
        except:
            print("Invalid input. Please enter a valid number.")

    print("Move the mouse to the center of the circle and click to start drawing.")
    time.sleep(2)

    # Start a non blocking listener to listen for mouse clicks
    listener = mouse.Listener(on_click=draw_circle)
    listener.start()
    print("Listening for mouse clicks..."
          "Press Ctrl+C to stop.")

    # Continue running the program so it doesn't cause an interruption.
    idle()


if __name__ == "__main__":
    main()
