package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/bailey4770/aoc2025/utils"
)

func parseData(data []string) [][]string {
	var parsed [][]string

	for _, line := range data {
		parsed = append(parsed, strings.Fields(line))
	}

	return parsed
}

func buildCols1(parsed [][]string) [][]string {
	cols := make([][]string, len(parsed[0]))

	for _, line := range parsed {
		for i, item := range line {
			cols[i] = append(cols[i], item)
		}
	}

	return cols
}

func sumElements(col []string) (int, error) {
	total := 0

	for _, item := range col {
		asInt, err := strconv.Atoi(item)
		if err != nil {
			return 0, err
		}

		total += asInt
	}

	return total, nil
}

func multiplyElements(col []string) (int, error) {
	total := 1

	for _, item := range col {
		asInt, err := strconv.Atoi(item)
		if err != nil {
			return 0, err
		}

		total *= asInt
	}

	return total, nil
}

func getCheckSum(problems [][]string) (int, error) {
	checkSum := 0

	for _, col := range problems {
		lastIdx := len(col) - 1
		operator := col[lastIdx]

		switch operator {
		case "+":
			res, err := sumElements(col[:lastIdx])
			if err != nil {
				return 0, err
			}
			checkSum += res

		case "*":
			res, err := multiplyElements(col[:lastIdx])
			if err != nil {
				return 0, err
			}
			checkSum += res
		}
	}

	return checkSum, nil
}

func part1(data []string) (int, error) {
	parsed := parseData(data)
	cols := buildCols1(parsed)

	res, err := getCheckSum(cols)
	if err != nil {
		return 0, err
	}

	return res, nil
}

func reverseString(s string) string {
	var res string

	for _, char := range s {
		res = string(char) + res
	}

	return res
}

func buildCols2(grid []string) [][]string {
	cols := make([]string, len(grid[0])+1)
	for i := range cols {
		cols[i] = ""
	}

	numProblems := 0
	for _, line := range grid {
		for i, char := range reverseString(line) {
			if char == '+' || char == '*' {
				cols[i+1] += string(char)
				numProblems++
			} else {
				cols[i] += string(char)
			}
		}
	}

	problems := make([][]string, numProblems)
	i := 0
	for _, col := range cols {
		col = strings.TrimSpace(col)
		problems[i] = append(problems[i], col)

		if col == "+" || col == "*" {
			i++
		}
	}

	return problems
}

func part2(data []string) (int, error) {
	problems := buildCols2(data)

	res, err := getCheckSum(problems)
	if err != nil {
		return 0, err
	}

	return res, nil
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
