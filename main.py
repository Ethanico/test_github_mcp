def calculate_average(numbers):
    total_sum = 0
    count = len(numbers)

    for num in numbers:
        total_sum += num

    average = total_sum / count
    return average

numbers = [10, 20, 30, 40, 50]

# Bug 1: Typo in function name
avg = calcualte_average(numbers)

# Bug 2: Incorrect argument type
avg_from_string = calculate_average("12345")

# Bug 3: Division by zero when the list is empty
empty_list_avg = calculate_average([])

print("Average of numbers:", avg)
print("Average from string:", avg_from_string)
print("Average of empty list:", empty_list_avg)