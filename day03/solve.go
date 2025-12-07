package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/bailey4770/aoc2025/utils"
)

func search(bank, batteries string, start, end int) (string, error) {
	largest := 0
	largestPos := 0
	stop := len(bank) - end
	runes := strings.Split(bank, "")

	for i := start; i < stop; i++ {
		if asInt, err := strconv.Atoi(runes[i]); err != nil {
			return "", err
		} else if asInt > largest {
			largest = asInt
			largestPos = i
		}
	}

	batteries += strconv.Itoa(largest)

	if end == 0 {
		return batteries, nil
	} else {
		return search(bank, batteries, largestPos+1, end-1)
	}
}

func callSearch(data []string, numBatteriesToFind int) (int, error) {
	total := 0

	for _, bank := range data {
		batteries := ""

		res, err := search(bank, batteries, 0, numBatteriesToFind-1)
		if err != nil {
			return 0, nil
		}

		if asInt, err := strconv.Atoi(res); err != nil {
			return 0, err
		} else {
			total += asInt
		}
	}

	return total, nil
}

func part1(data []string) (int, error) {
	numBatteriesToFind := 2
	return callSearch(data, numBatteriesToFind)
}

func part2(data []string) (int, error) {
	numBatteriesToFind := 12
	return callSearch(data, numBatteriesToFind)
}

func main() {
	data, err := utils.LoadString(false, "\n")
	if err != nil {
		log.Fatalf("Error: %v", err)
	}

	res1, err := part1(data)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	fmt.Printf("Part 1: %v\n", res1)

	res2, err := part2(data)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	fmt.Printf("Part 2: %v\n", res2)
}
