package sort

// Algorithm is the placeholder for your custom sorting algorithm.
func Algorithm(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				// Swaps the elements
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}
