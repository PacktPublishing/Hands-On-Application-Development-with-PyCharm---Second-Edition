import random

# bubble sort is the slowest sort algorithm there is
def bubble_sort(input_array):
    length_of_array = len(input_array)

    for i in range(length_of_array):
        for j in range(0, length_of_array - i - 1):
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]


test_array = []
for x in range(100000):
    test_array.append(random.randint(1, 10000))


bubble_sort(test_array)
print("The result of the sort is:")
for i in range(len(test_array)):
    print(test_array[i])
