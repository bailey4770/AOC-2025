package utils

import (
	"bufio"
	"os"
	"strings"
)

func LoadString(test bool, separator string) ([]string, error) {
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

	var data []string

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		line := strings.Split(text, separator)
		data = append(data, line...)
	}

	return data, nil
}

func findNeighbours(grid []string, row, col int, dirs [][]int) [][]int {
	var neighbours [][]int

	for _, d := range dirs {
		newRow := row + d[0]
		newCol := col + d[1]

		if 0 <= newRow && newRow < len(grid) {
			if 0 <= newCol && newCol < len(grid[0]) {
				neighbour := []int{newRow, newCol}
				neighbours = append(neighbours, neighbour)
			}
		}
	}

	return neighbours
}

func Neighbours8(grid []string, row, col int) [][]int {
	dirs := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}}
	return findNeighbours(grid, row, col, dirs)
}

func Neighbours4(grid []string, row, col int) [][]int {
	dirs := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	return findNeighbours(grid, row, col, dirs)
}
