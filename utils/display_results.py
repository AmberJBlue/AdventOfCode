import random

def display_result(day, part, result):
    """
    Displays the result for a specific day and part in a festive Christmas-themed style,
    with a randomly selected holiday-themed message.
    
    Parameters:
        day (int): The day of the challenge.
        part (int): The part of the challenge (1 or 2).
        result (int or str): The result to display.
    """
    # ANSI escape codes for colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    RESET = "\033[0m"

    # List of holiday-themed messages
    holiday_messages = [
        "🎁 Unwrapping the result for you!",
        "✨ It's a Christmas miracle!",
        "🎅 Ho Ho Ho! Here's your result!",
        "🕯️ Lighting the way to your answer!",
        "❄️ A frosty result, fresh from the North Pole!",
        "🎅 Santa approves this result!",
        "🌟 Shining bright, here's the result!",
        "🍪 Your result, served with milk and cookies!"
    ]

    # Select a random message
    message = random.choice(holiday_messages)

    # Display the result with a festive style
    print(f"{RED}{message}{RESET}")
    print(
        f"{RED}🎄🎄🎄 {GREEN}Day {day}, Part {part}: {YELLOW}{result}{RESET} 🎄🎄🎄"
    )
    print(f"{CYAN}Merry Christmas and Happy Coding!{RESET}")
