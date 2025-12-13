package utils

import (
	"fmt"
	"testing"
)

var grid = []string{"123", "456", "789"}

func TestNeighbours8(t *testing.T) {
	t.Run("neighbours8", func(t *testing.T) {
		row := 0
		col := 1

		neighbours := Neighbours8(grid, row, col)
		fmt.Print(row, col)
		fmt.Println()

		for _, neighbour := range neighbours {
			fmt.Print(neighbour)
		}
	})
}

func TestNeighbours4(t *testing.T) {
	t.Run("neighbours4", func(t *testing.T) {
		row := 0
		col := 1

		neighbours := Neighbours4(grid, row, col)
		fmt.Print(row, col)
		fmt.Println()

		for _, neighbour := range neighbours {
			fmt.Print(neighbour)
		}
	})
}
