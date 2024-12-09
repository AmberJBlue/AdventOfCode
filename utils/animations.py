import time
import os
import random
import threading

stop_animation = threading.Event()


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


def snowfall_progress(
    rows=1000, width=1000, duration=None, progress=None, context="", show_fraction=False
):
    """
    Displays a snowfall animation in the terminal with an optional progress bar.

    Parameters:
        rows (int): Number of rows in the snowfall.
        width (int): Width of the terminal display and progress bar.
        duration (int or None): If specified, the animation lasts for the given seconds.
                                If None, the animation runs indefinitely until stopped.
        progress (callable): Optional callable that returns a tuple (complete, total).
                             Used to compute progress percentage and fraction.
        context (str): Optional message to display below the progress bar.
        show_fraction (bool): If True, display complete/total fraction instead of percentage.
    """
    snow = [" " * width for _ in range(rows)]
    start_time = time.time()
    completed = 0
    total = 100  # Default total percentage

    while not stop_animation.is_set():
        os.system("cls" if os.name == "nt" else "clear")

        # Update progress values if callable is provided
        if progress:
            completed, total = progress()
            percent_complete = (completed / total) * 100
        else:
            percent_complete = (completed / total) * 100

        density = min(0.1 + (percent_complete / 100) * 0.4, 0.5)  # 10% to 50%

        new_row = ["*" if random.random() < density else " " for _ in range(width)]
        snow.append("".join(new_row))
        if len(snow) > rows:
            snow.pop(0)

        print("\n".join(snow))

        progress_units = int((percent_complete / 100) * width)
        bar = "#" * progress_units + " " * (width - progress_units)

        if progress:
            if show_fraction:
                progress_text = f"[{completed}/{total}]"
            else:
                progress_text = f"{percent_complete:.2f}%"
        else:
            progress_text = ""

        if context:
            progress_text = context + progress_text
        print(f"\n{progress_text}")

        if duration and time.time() - start_time >= duration:
            break

        time.sleep(0.2)
