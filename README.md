# Sort Benchmark Go

A Go project for benchmarking and testing sorting algorithms with different input distributions.

## Overview

This project provides a framework to implement, test, and benchmark custom sorting algorithms in Go. It includes utilities for generating test data in different scenarios (ascending, descending, and random order) and validates the correctness of sorting implementations.

## Features

- 🔧 Modular architecture for easy algorithm implementation
- 📊 Multiple data generation strategies (ascending, descending, random)
- ✅ Sorting verification utility
- 📈 Benchmark-ready structure
- 🚀 Written in Go for high performance

## Project Structure

```
sort-benchmark-go/
├── main.go              # Entry point with benchmark runner
├── sort/
│   └── sort.go          # Sorting algorithm implementation
├── generator/
│   └── generator.go     # Test data generators
├── go.mod               # Module definition
└── README.md
```

## Installation

Prerequisites:
- Go 1.26.2 or higher

Clone the repository:

```bash
git clone https://github.com/EGS-software/sort-benchmark-go.git
cd sort-benchmark-go
```

## Usage

### Running the Benchmark

```bash
go run main.go
```

This will execute the sorting algorithm against different input distributions and verify correctness.

### Implementing a Custom Algorithm

Edit `sort/sort.go` and implement your sorting algorithm in the `Algorithm` function:

```go
func Algorithm(arr []int) {
    // Your sorting implementation here
}
```

### Generating Test Data

The `generator` package provides three data generation strategies:

- **GenerateAscending(size)** - Creates a sorted array (best-case scenario)
- **GenerateDescending(size)** - Creates a reverse-sorted array (worst-case scenario)
- **GenerateRandom(size)** - Creates a shuffled array (average-case scenario)

## Building

```bash
go build
```

This creates an executable binary that can be run with:

```bash
./sort-benchmark-go
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by [@jvbenetti](https://github.com/jvbenetti)
