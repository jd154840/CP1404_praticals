# # 1
#
# name = input("Name: ")
# out_file = open('name.txt', 'w')
#
# print(name, file=out_file)
# out_file.close()
#
# in_file = open('name.txt', 'r')
# name = in_file.read().strip()
# print(f"Hi {name}!")

# other_in_file = open('numbers.txt', 'r')
# numbers = other_in_file.readlines()
# first_number = int(numbers[0].strip())
# second_number = int(numbers[1].strip())
# sum_of_numbers = first_number + second_number
# print(sum_of_numbers)

other_in_file = open('numbers.txt', 'r')
total = 0
for line in other_in_file:
    numbers = int(line.strip())
    total = total + numbers
print(total)

other_in_file.close()
