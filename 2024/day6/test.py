import time
import os
import random
import threading

stop_animation = threading.Event()


def snowfall_with_progress(rows=20, width=50, total_percentage=100):
    """
    Displays a snowfall animation in the terminal with a progress bar at the bottom.
    The snowfall density increases as the progress percentage grows.
    A custom message is displayed under the progress bar.

    Parameters:
        rows (int): Number of rows in the snowfall.
        width (int): Width of the terminal display and progress bar.
        total_percentage (int): Percentage to complete the progress bar.
    """
    snow = [" " * width for _ in range(rows)]
    completed = 0

    while not stop_animation.is_set():
        os.system("cls" if os.name == "nt" else "clear")

        # Increase snowflake density based on progress
        density = min(0.1 + (completed / total_percentage) * 0.4, 0.5)  # 10% to 50%

        # Add new row of snowflakes with varying density
        new_row = ["*" if random.random() < density else " " for _ in range(width)]
        snow.append("".join(new_row))
        if len(snow) > rows:
            snow.pop(0)

        # Display snow
        print("\n".join(snow))

        # Display progress bar
        progress = int((completed / total_percentage) * width)
        bar = "#" * progress + " " * (width - progress)
        print(f"\n[{bar}] {completed}%")
        print("Simulating guard positions...")

        # Increment completion percentage
        completed = min(completed + 1, total_percentage)
        time.sleep(0.2)

        # Stop when the progress bar is full
        if completed == total_percentage:
            break


if __name__ == "__main__":
    try:
        print("Press Ctrl+C to stop the animation...")
        snowfall_thread = threading.Thread(
            target=snowfall_with_progress, args=(20, 50, 100), daemon=True
        )
        snowfall_thread.start()

        # Keep the main thread running to allow the animation to play
        while snowfall_thread.is_alive():
            time.sleep(0.1)

    except KeyboardInterrupt:
        stop_animation.set()
