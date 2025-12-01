def load_data(test: bool = True):
    if test:
        with open("test_input.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("input.txt", "r") as f:
            data = f.read().splitlines()

    return data


def part1(data: list[str]):
    MAX = 100
    curr = 50
    count = 0

    for line in data:
        instruction = line[0]
        dist = int(line[1:])

        if instruction == "R":
            curr = (curr + dist) % MAX
        elif instruction == "L":
            curr = (curr - dist) % MAX

        if curr == 0:
            count += 1

    return count


def part2(data: list[str]):
    MAX = 100
    curr = 50
    count = 0

    for line in data:
        instruction = line[0]
        dist = int(line[1:])

        full_laps, dist = divmod(dist, MAX)
        count += full_laps

        if instruction == "R":
            while dist:
                curr += 1
                dist -= 1

                if curr == MAX:
                    count += 1

        elif instruction == "L":
            while dist:
                curr -= 1
                dist -= 1

                if curr == 0:
                    count += 1

        curr %= MAX

    return count


if __name__ == "__main__":
    data = load_data(False)
    print(part1(data))
    print(part2(data))
