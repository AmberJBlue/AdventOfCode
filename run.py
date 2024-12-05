import argparse
import importlib.util
import sys
from pathlib import Path


def get_latest_day(year):
    """
    Finds the most recent solution (highest-numbered day) for a given year.

    Parameters:
        year (int): The year of the challenge.

    Returns:
        int: The most recent day (highest number) with a solution.
    """
    year_path = Path(str(year))
    if not year_path.exists():
        print(f"Error: Directory for year {year} does not exist.")
        sys.exit(1)

    # Find all directories matching 'dayX' in the specified year's folder
    day_dirs = [
        d for d in year_path.iterdir() if d.is_dir() and d.name.startswith("day")
    ]
    if not day_dirs:
        print(f"No solutions found for year {year}.")
        sys.exit(1)

    # Extract the day number and return the highest
    latest_day = max(int(d.name.replace("day", "")) for d in day_dirs)
    return latest_day


def run_solution(year, day, part, test, snow):
    """
    Dynamically runs the solution for the specified year, day, and part.

    Parameters:
        year (int): The year of the challenge (e.g., 2024).
        day (int): The day of the challenge (1-25).
        part (int): The part of the challenge (1 or 2).
        test (bool): Whether to use test input.
        snow (int): Duration of snowfall animation (0 to skip).
    """
    # Build the path to the solution file
    solution_file = Path(f"{year}/day{day}/solution.py")

    if not solution_file.exists():
        print(f"Error: Solution file for Year {year}, Day {day} does not exist.")
        sys.exit(1)

    # Dynamically import the solution module
    spec = importlib.util.spec_from_file_location(
        f"{year}_day{day}_solution", solution_file
    )
    solution_module = importlib.util.module_from_spec(spec)
    sys.modules[f"{year}_day{day}_solution"] = solution_module
    spec.loader.exec_module(solution_module)

    # Pass arguments to the solution's main logic
    if hasattr(solution_module, "__name__") and solution_module.__name__ == "__main__":
        # Mock arguments for the solution
        sys.argv = [
            str(solution_file),
            f"--part={part}",
            f"--test={test}",
        ]
        if snow:
            sys.argv.append(f"--snow={snow}")

        # Execute the solution's main
        solution_module.main()
    else:
        print(
            f"Error: Year {year}, Day {day} solution does not have a '__main__' function."
        )
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions for any year and day."
    )
    parser.add_argument(
        "-year",
        required=False,
        default=2024,
        type=int,
        help="The year of the challenge (e.g., 2024).",
    )
    parser.add_argument(
        "-day",
        required=False,
        type=int,
        help="The day of the challenge (1-25). Defaults to the latest solution.",
    )
    parser.add_argument(
        "-part",
        required=False,
        default=1,
        type=int,
        help="The part of the challenge (1 or 2).",
    )
    parser.add_argument(
        "-test",
        required=False,
        default="False",
        type=str,
        help="Use test input? (True/False).",
    )
    parser.add_argument(
        "--snow",
        required=False,
        type=int,
        help="Make it snow! Specify duration (seconds).",
    )

    args = parser.parse_args()
    test_flag = args.test.lower() == "true"

    # Determine the most recent day if no day is specified
    day = args.day if args.day else get_latest_day(args.year)

    run_solution(
        year=args.year, day=day, part=args.part, test=test_flag, snow=args.snow
    )
