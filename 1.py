def check_numbers(numbers):
    positive_numbers = []
    negative_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)

    return positive_numbers, negative_numbers

# Misol uchun
numbers = [10, -5, 0, 23, -42, 7, -1]
positive, negative = check_numbers(numbers)
print("Musbat sonlar:", positive)
print("Manfiy sonlar:", negative)
