package generator

import "math/rand"

// GenerateAscending creates an array ordered from smallest to largest.
func GenerateAscending(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i
	}
	return arr
}

// GenerateDescending creates an array ordered from largest to smallest.
func GenerateDescending(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = size - i
	}
	return arr
}

// GenerateRandom creates an array with shuffled numbers.
func GenerateRandom(size int) []int {
	arr := GenerateAscending(size)

	// Shuffles the array
	rand.Shuffle(len(arr), func(i, j int) {
		arr[i], arr[j] = arr[j], arr[i]
	})

	return arr
}
