package main

import (
	"fmt"
	"log"
	"math"
	"strconv"
	"strings"

	"github.com/bailey4770/aoc2025/utils"
)

func getBounds(idRange string) (int, int, error) {
	splitRange := strings.Split(idRange, "-")
	lower, err := strconv.Atoi(splitRange[0])
	if err != nil {
		return 0, 0, err
	}
	higher, err := strconv.Atoi(splitRange[1])
	if err != nil {
		return 0, 0, nil
	}

	return lower, higher, nil
}

func invalid1(num int) bool {
	length := len(strconv.Itoa(num))

	if length%2 != 0 {
		return false
	}

	half := int(math.Pow10(length / 2))
	left := num / half
	right := num % half

	return left == right
}

func part1(data []string) (int, error) {
	total := 0

	for _, idRange := range data {
		lower, higher, err := getBounds(idRange)
		if err != nil {
			return 0, err
		}

		for num := lower; num <= higher; num++ {
			if invalid1(num) {
				total += num
			}
		}
	}

	return total, nil
}

func invalid2(num int) bool {
	asString := strconv.Itoa(num)
	length := len(asString)

	doubled := asString + asString
	truncated := doubled[1 : len(doubled)-1]

	for i := 0; i <= len(truncated)-length; i++ {
		if truncated[i:i+length] == asString {
			return true
		}
	}

	return false
}

func part2(data []string) (int, error) {
	total := 0

	for _, idRange := range data {
		lower, higher, err := getBounds(idRange)
		if err != nil {
			return 0, err
		}

		for num := lower; num <= higher; num++ {
			if invalid2(num) {
				total += num
			}
		}
	}

	return total, nil
}

func main() {
	data, err := utils.LoadString(false)
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
