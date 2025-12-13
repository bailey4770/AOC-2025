package main

import (
	"fmt"
	"log"

	"github.com/bailey4770/aoc2025/utils"
)

type coordT [2]int

func part1(grid []string) int {
	total := 0

	for row, line := range grid {
		for col, char := range line {
			if char != '@' {
				continue
			}

			neighbours := utils.Neighbours8(grid, row, col)
			numNeighbours := 0

			for _, neighbour := range neighbours {
				if grid[neighbour[0]][neighbour[1]] == '@' {
					numNeighbours++
				}
			}

			if numNeighbours < 4 {
				total++
			}
		}
	}

	return total
}

func searchAndRemove(grid []string, removed map[[2]int]struct{}, total int) int {
	roundTotal := 0
	toRemove := make(map[[2]int]struct{})

	for row, line := range grid {
		for col, char := range line {

			coord := coordT{row, col}
			if _, ok := removed[coord]; ok || char != '@' {
				continue
			}

			neighbours := utils.Neighbours8(grid, row, col)
			numNeighbours := 0

			for _, neighbour := range neighbours {
				neighbourCoord := coordT{neighbour[0], neighbour[1]}
				if _, ok := removed[neighbourCoord]; !ok && grid[neighbour[0]][neighbour[1]] == '@' {
					numNeighbours++
				}
			}

			if numNeighbours < 4 {
				roundTotal++
				toRemove[coord] = struct{}{}
			}
		}
	}

	for coord := range toRemove {
		removed[coord] = struct{}{}
	}

	if roundTotal == 0 {
		return total
	} else {
		return searchAndRemove(grid, removed, total+roundTotal)
	}
}

func part2(grid []string) int {
	total := 0
	removed := make(map[[2]int]struct{})

	return searchAndRemove(grid, removed, total)
}

func main() {
	data, err := utils.LoadString(false, "\n")
	if err != nil {
		log.Fatalf("Error: %v", err)
	}

	res1 := part1(data)
	fmt.Printf("Part 1: %v\n", res1)

	res2 := part2(data)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	fmt.Printf("Part 2: %v\n", res2)
}
