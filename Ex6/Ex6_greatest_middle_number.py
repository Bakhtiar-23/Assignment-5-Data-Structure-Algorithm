def find_greatest_number(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def find_middle_number(numbers):
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    return sorted_numbers[middle_index]

# Example Lists
numbers1 = [3, 7, 2, 9, 5]
numbers2 = [3, 7, 2, 9, 5]

# Task 1
greatest = find_greatest_number(numbers1)
print(f"The greatest number is: {greatest}")

# Task 2
middle = find_middle_number(numbers2)
print(f"The middle number is: {middle}")
