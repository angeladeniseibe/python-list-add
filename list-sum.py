number_input = input("Enter numbers separated by commas: ")
numbers_list = number_input.split(",")

num_sum = 0
valid_input = True

for num_str in numbers_list:
    try:
        num = int(num_str.strip())
        num_sum += num
    except ValueError:
        print("Invalid input. Please input numbers only.")
        valid_input = False
        break

if valid_input:
    print("Sum:", num_sum)
