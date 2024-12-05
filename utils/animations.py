import time
import os
import random


def snowfall_animation(rows=100, width=100, duration=10):
    """
    Displays a snowfall animation in the terminal.

    Parameters:
        rows (int): Number of rows in the snowfall.
        width (int): Width of the terminal display.
        duration (int): How long the snowfall should last (in seconds).
    """
    snow = [" " * width for _ in range(rows)]
    end_time = time.time() + duration

    while time.time() < end_time:
        os.system("cls" if os.name == "nt" else "clear")
        snow.append(" " * random.randint(0, width - 1) + "*")
        snow.pop(0)
        print("\n".join(snow))
        time.sleep(0.2)
