package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Instruction struct {
	Direction rune
	Distance  int
}

type Instructions []Instruction

func (i *Instructions) ParseString(line string) error {
	if line == "" {
		return nil
	}

	if len(line) < 2 {
		return fmt.Errorf("false instruction %q", line)
	}

	dir := rune(line[0])
	dist, err := strconv.Atoi(line[1:])
	if err != nil {
		return err
	}

	if dir != 'L' && dir != 'R' {
		return fmt.Errorf("false instruction %q", line)
	}

	*i = append(*i, Instruction{dir, dist})
	return nil
}

func mod(a, b int) int {
	remainder := a % b

	if remainder < 0 {
		remainder += b
	}

	return remainder
}

func divmod(a, b int) (int, int) {
	quotient := a / b
	remainder := a % b

	return quotient, remainder
}

func getData(test bool) (Instructions, error) {
	var fileName string
	if test {
		fileName = "test_input.txt"
	} else {
		fileName = "input.txt"
	}

	file, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines Instructions

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		err := lines.ParseString(line)
		if err != nil {
			return nil, err
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

func part1(data Instructions) (int, error) {
	count := 0
	curr := 50
	const max = 100

	for _, instruction := range data {
		switch instruction.Direction {
		case 'L':
			curr = mod(curr-instruction.Distance, max)
		case 'R':
			curr = mod(curr+instruction.Distance, max)
		}

		if curr == 0 {
			count++
		}
	}

	return count, nil
}

func part2(data Instructions) (int, error) {
	count := 0
	curr := 50
	const max = 100

	for _, instruction := range data {
		previous := curr

		fullLaps, remainder := divmod(instruction.Distance, max)
		count += fullLaps

		crossed := false
		switch instruction.Direction {
		case 'L':
			curr = mod(curr-remainder, max)

			if remainder >= previous && previous != 0 {
				crossed = true
			}

		case 'R':
			curr = mod(curr+remainder, max)

			if remainder+previous >= max && previous != 0 {
				crossed = true
			}
		}

		if crossed {
			count++
		}
	}

	return count, nil
}

func main() {
	data, err := getData(false)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}

	part1Answer, err := part1(data)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	part2Answer, err := part2(data)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}

	fmt.Println(part1Answer)
	fmt.Println(part2Answer)
}
