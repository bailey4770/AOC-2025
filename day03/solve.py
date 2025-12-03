def get_data(test: bool):
    file_name = "test_input.txt" if test else "input.txt"

    with open(file_name, "r") as f:
        return f.read().splitlines()


def _search(bank: str, start: int, end: int, batteries: str) -> str:
    largest = ""
    largest_pos = 0
    for i in range(start, len(bank) - end):
        if bank[i] > largest:
            largest: str = bank[i]
            largest_pos = i

    batteries += largest

    if end == 0:
        # we've reached the end of the digits to find
        return batteries
    else:
        return _search(bank, largest_pos + 1, end - 1, batteries)


def _call_search(data: list[str], num_batteries_to_find: int):
    total = 0

    for bank in data:
        batteries = ""
        total += int(_search(bank, 0, num_batteries_to_find - 1, batteries))

    return total


def part1(data: list[str]):
    return _call_search(data, 2)


def part2(data: list[str]):
    return _call_search(data, 12)


def main():
    data = get_data(test=False)
    print(part1(data))
    print(part2(data))

    # day 3 ez bro
    # I like a nice recursive question


if __name__ == "__main__":
    main()
