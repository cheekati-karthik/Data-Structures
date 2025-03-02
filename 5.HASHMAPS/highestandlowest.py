def find_highest_lowest_frequency(arr):
    freq_map = {}  # Dictionary to store frequency of elements

    # Counting frequency of each element
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Finding elements with highest and lowest frequency
    max_freq = max(freq_map.values())
    min_freq = min(freq_map.values())

    max_freq_elements = [key for key, value in freq_map.items() if value == max_freq]
    min_freq_elements = [key for key, value in freq_map.items() if value == min_freq]

    return max_freq_elements, min_freq_elements

# Example usage
arr = [1, 3, 2, 3, 1, 3, 2, 2, 2, 4, 4, 4, 4]
highest, lowest = find_highest_lowest_frequency(arr)

print(f"Elements with highest frequency: {highest}")
print(f"Elements with lowest frequency: {lowest}")