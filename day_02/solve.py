def get_data(test: bool = True):
    if test:
        with open("test_input.txt", "r") as f:
            return f.read().split(",")
    else:
        with open("input.txt", "r") as f:
            return f.read().split(",")


def part1(data: list[str]):
    def invalid(num):
        num = str(num)
        length = len(num)

        if length % 2 != 0:
            return False

        first, second = num[: length // 2], num[length // 2 :]

        if first != second:
            return False

        return True

    total = 0

    for id_range in data:
        lower, higher = id_range.split("-")
        lower, higher = int(lower), int(higher)

        for num in range(lower, higher + 1):
            if invalid(num):
                total += num

    return total


def part2(data):
    def invalid(num):
        num = str(num)

        for i in range(2, len(num) + 1):
            if len(num) % i != 0:
                continue

            sequence_len = len(num) // i
            sequence = num[:sequence_len]

            repeating = True
            for j in range(sequence_len, len(num), sequence_len):
                if sequence != num[j : j + sequence_len]:
                    repeating = False

            if repeating:
                return True

    total = 0

    for id_range in data:
        lower, higher = id_range.split("-")
        lower, higher = int(lower), int(higher)

        for num in range(lower, higher + 1):
            if invalid(num):
                total += num

    return total


if __name__ == "__main__":
    data = get_data(False)
    print(part1(data))
    print(part2(data))
