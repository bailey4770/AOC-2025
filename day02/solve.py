def get_data(test: bool = True):
    if test:
        with open("test_input.txt", "r") as f:
            return f.read().split(",")
    else:
        with open("input.txt", "r") as f:
            return f.read().split(",")


def part1(data: list[str]):
    def invalid(num: int):
        length: int = len(str(num))

        if length % 2 != 0:
            return False

        """We can avoid expensive str casting with divisor trick.
           Consider 123123:
               half = 1000
               left = 123123 // 1000 = 123
               right = 123123 % 1000 = 123"""
        half: int = 10 ** (length // 2)
        left: int = num // half
        right: int = num % half

        return left == right

    total = 0

    for id_range in data:
        lower, higher = map(int, id_range.split("-"))

        for num in range(lower, higher + 1):
            if invalid(num):
                total += num

    return total


def part2(data: list[str]):
    def invalid(num: int):
        """double the string, remove first and last letters, then check if original string is still substring of the new string.
        If it is, then string must be composed entirely of repeating sections"""
        s = str(num)
        return s in (s + s)[1:-1]

    total = 0

    for id_range in data:
        lower, higher = map(int, id_range.split("-"))

        for num in range(lower, higher + 1):
            if invalid(num):
                total += num

    return total


if __name__ == "__main__":
    data = get_data(False)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
