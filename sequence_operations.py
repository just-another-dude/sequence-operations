length_list = []
sum_list = []

for positive_integer in range(1, 10000001):
    integer_list = []
    while True:
        integer_list.append(positive_integer)

        # If the integer equals 1 then append different values to two lists and break out of the loop.
        if positive_integer == 1:
            sum_list.append(sum(integer_list))  # Append the sum of the sequence to the sum list.
            length_list.append(len(integer_list))  # Append the length of the sequence to the length list.
            break
            
        # If even - divide by 2 with an integer type result (not float as opposed to using "/").
        # Else (if odd) - multiply by 3 and add 1.
        if positive_integer % 2 == 0:
            positive_integer = positive_integer // 2
        else:  # If odd
            positive_integer = (positive_integer * 3) + 1

print("Sum list: ", length_list)

# Sort the list from small to big in terms of values.
sorted_length_list = sorted(length_list)
print("Sorted list: ", sorted(sorted_length_list))

# Second longest sequence length.
second_longest_length = sorted_length_list[-2]
print("Second longest sequence has {} elements!".format(second_longest_length))

# The element index of the second longest sequence in the length list.
length_index = length_list.index(second_longest_length)

# The sum of the second longest sequence in the range.
second_longest_sum = sum_list[length_index]

print("Sum of second longest sequence is: ", second_longest_sum)
