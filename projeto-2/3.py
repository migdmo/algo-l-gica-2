def validate_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def find_most_frequent(numbers):
    if not numbers:  # Check if array is empty
        return None
        
    # Count occurrences of each number
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Find the maximum frequency
    max_count = max(count.values())
    
    # Find all numbers that appear max_count times
    most_frequent = [num for num, freq in count.items() if freq == max_count]
    
    # If more than one number has the maximum frequency, return None
    if len(most_frequent) > 1:
        return None
    
    return most_frequent[0]

def main():
    # Get array size
    size = validate_int_input("Enter the size of the array: ")
    while size <= 0:
        print("Error: Array size must be positive.")
        size = validate_int_input("Enter the size of the array: ")
    
    # Get array elements
    numbers = []
    print(f"\nEnter {size} integers:")
    for i in range(size):
        num = validate_int_input(f"Element {i + 1}: ")
        numbers.append(num)
    
    # Find and display the most frequent number
    result = find_most_frequent(numbers)
    
    if result is None:
        if not numbers:
            print("\nThe array is empty.")
        else:
            print("\nThere is no single most frequent number (there is a tie).")
    else:
        print(f"\nThe most frequent number is: {result}")

if __name__ == "__main__":
    main()