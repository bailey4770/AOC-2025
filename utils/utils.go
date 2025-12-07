package utils

import (
	"bufio"
	"os"
	"strings"
)

func LoadString(test bool) ([]string, error) {
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
		line := strings.Split(text, ",")
		data = append(data, line...)
	}

	return data, nil
}
