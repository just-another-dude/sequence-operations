'''

Background information:
You can choose the programming language you feel the most comfortable with.
We expect that you can solve this within 1 hour.



Task:
For any positive integer n we define two rules:
if even: divide by two
if odd: multiply by three, then add one, and repeat until the result is the number 1



This will generate sequences of numbers like below, converging to 1:



3, 10, 5, 16, 8, 4, 2, 1



7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1



For each number n we can now count the number of steps in this sequence until we reach 1.



So the sequence above, starting with 3, has a length of 8 (including the starting point and the final one).
The second sequence has a length of 17.



Challenge:
Find the second-longest sequence of all the integers smaller or equal than 10 Million.



Some calibration help:
The longest sequence for input <= 1000 has a length of 179
The longest sequence for input <= 10000 has a length of 262



Calculate the sum of all the elements of the above mentioned second-longest sequence and share your result. Also, please include your source code.
'''

'''
positive_integer = int(input("Enter a positive integer: "))


if positive_integer < 0:
    raise Exception
'''

length_list = []
sum_list = []

for positive_integer in range(1, 10000000):
    integer_list = []
    while True:
        integer_list.append(positive_integer)
        # print(positive_integer)
        if positive_integer == 1:  # If the integer equals 1
            print(integer_list)
            sum_list.append(sum(integer_list))  # Append the sum of the sequence to the sum list.
            length_list.append(len(integer_list))  # Append the length of the sequence to the length list.
            break
        if positive_integer % 2 == 0:  # if even
            positive_integer = positive_integer // 2
        else:  # If odd
            positive_integer = (positive_integer * 3) + 1

print("Sum list: ", length_list)

# Sort the list from short to long
sorted_length_list = sorted(length_list)
print("Sorted list: ", sorted(sorted_length_list))

# Second longest sequence length
second_longest_length = sorted_length_list[-2]
print("Second longest sequence has {} elements!".format(second_longest_length))

# The element index of the second longest sequence in the length list.
length_index = length_list.index(second_longest_length)

# The sum of the second longest sequence in the range.
second_longest_sum = sum_list[length_index]

print("Sum of second longest sequence is: ", second_longest_sum)
