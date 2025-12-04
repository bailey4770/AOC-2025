import shutil
from pathlib import Path
import sys


def create_day_dir():
    if len(sys.argv) > 2:
        print("Error: only input the day to create")
        return

    day = sys.argv[1]
    if not day.isdigit():
        print("Error: only input a number for the day")
        return
    if len(day) == 1:
        day = "0" + day

    new_day_dir = Path(f"day{day}")
    new_day_dir.mkdir()

    template = Path("utils/template.py")
    destination = new_day_dir / "solve.py"
    shutil.copy(template, destination)

    (new_day_dir / "input.txt").touch()
    (new_day_dir / "test_input.txt").touch()


if __name__ == "__main__":
    create_day_dir()
