package main

import (
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"

	"github.com/bailey4770/aoc2025/utils"
)

type idRange struct {
	start int
	end   int
}

func (r idRange) contains(ingr int) bool {
	return ingr >= r.start && ingr <= r.end
}

func (r idRange) size() int {
	return r.end - r.start + 1
}

func parseData(data []string) ([]idRange, []int, error) {
	var idRanges []idRange
	var ingredients []int
	parsingRanges := true

	for _, line := range data {
		if line == "" {
			parsingRanges = false
			continue
		}

		if parsingRanges {
			parts := strings.Split(line, "-")
			if len(parts) != 2 {
				return nil, nil, fmt.Errorf("error in parsing range: %s", line)
			}

			start, err := strconv.Atoi(parts[0])
			if err != nil {
				return nil, nil, err
			}

			end, err := strconv.Atoi(parts[1])
			if err != nil {
				return nil, nil, err
			}

			idRanges = append(idRanges, idRange{start, end})

		} else {
			ingredient, err := strconv.Atoi(line)
			if err != nil {
				return nil, nil, err
			}

			ingredients = append(ingredients, ingredient)
		}
	}

	return idRanges, ingredients, nil
}

func part1(data []string) (int, error) {
	idRanges, ingredients, err := parseData(data)
	if err != nil {
		return 0, err
	}

	freshCount := 0
	for _, ingr := range ingredients {
		for _, currRange := range idRanges {
			if currRange.contains(ingr) {
				freshCount++
				break
			}
		}
	}

	return freshCount, nil
}

func combineRanges(idRanges []idRange) []idRange {
	sort.Slice(idRanges,
		func(i, j int) bool {
			return idRanges[i].start < idRanges[j].start
		})

	combinedRanges := []idRange{idRanges[0]}

	for _, currRange := range idRanges[1:] {
		prevRange := &combinedRanges[len(combinedRanges)-1]

		if currRange.start <= prevRange.end+1 {
			prevRange.end = max(currRange.end, prevRange.end)
		} else {
			combinedRanges = append(combinedRanges, currRange)
		}
	}

	return combinedRanges
}

func part2(data []string) (int, error) {
	idRanges, _, err := parseData(data)
	if err != nil {
		return 0, err
	}

	combinedRanges := combineRanges(idRanges)

	numFreshIngredients := 0
	for _, currRange := range combinedRanges {
		numFreshIngredients += currRange.size()
	}

	return numFreshIngredients, nil
}

func main() {
	data, err := utils.LoadString(false, ",")
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
