package main

import (
	"fmt"
	"time"

	// Importing our local packages
	"github.com/EGS-software/sort-benchmark-go.git/generator"
	"github.com/EGS-software/sort-benchmark-go.git/sort"
)

func main() {
	var maxN, sampleM, stepSize int

	// 1. Data Input
	fmt.Println("=== Sorting Performance Analysis ===")
	fmt.Print("Enter the maximum array size (N): ")
	fmt.Scan(&maxN)
	fmt.Print("Enter the step size (e.g., 1000 to test 1000, 2000... up to N): ")
	fmt.Scan(&stepSize)
	fmt.Print("Enter the number of tests for random arrays (M - Sample Size): ")
	fmt.Scan(&sampleM)

	fmt.Println("\nProcessing... (This might take a few seconds depending on N)\n")

	// Table Header
	fmt.Println("-------------------------------------------------------------------------------------------------")
	fmt.Printf("%-18s | %-20s | %-20s | %-25s\n", "Array Size", "Ascending (Time)", "Descending (Time)", "Random (Avg Time)")
	fmt.Println("-------------------------------------------------------------------------------------------------")

	// 2. Test Scenarios (Iterating in steps up to maxN)
	for currentSize := stepSize; currentSize <= maxN; currentSize += stepSize {

		// Ascending Test
		ascArray := generator.GenerateAscending(currentSize)
		startAsc := time.Now()
		sort.Algorithm(ascArray)
		timeAsc := time.Since(startAsc)

		// Descending Test
		descArray := generator.GenerateDescending(currentSize)
		startDesc := time.Now()
		sort.Algorithm(descArray)
		timeDesc := time.Since(startDesc)

		// Random Test (Average of M executions)
		var totalRandomTime time.Duration
		for i := 0; i < sampleM; i++ {
			randArray := generator.GenerateRandom(currentSize)
			startRand := time.Now()
			sort.Algorithm(randArray)
			totalRandomTime += time.Since(startRand)
		}
		avgRandomTime := totalRandomTime / time.Duration(sampleM)

		// 3. Expected Output (Printing the table row)
		fmt.Printf("%-18d | %-20v | %-20v | %-25v\n", currentSize, timeAsc, timeDesc, avgRandomTime)
	}
	fmt.Println("-------------------------------------------------------------------------------------------------")
}
