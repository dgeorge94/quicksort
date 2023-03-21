def partition(a, p, r):
    # choose last element as pivot
    x = a[r]

    # pointer for higher element
    i = p - 1

    # traverse and compare with pivot
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1

            # swap element i with j
            a[i], a[j] = a[j], a[i]

    # swap pivot with higher
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quick_sort(a, p, r):
    if p < r:
        # find pivot element where smaller elements on left and larger on right
        pivot = partition(a, p, r)

        # left side recursion
        quick_sort(a, p, pivot - 1)

        # right side recursion
        quick_sort(a, pivot + 1, r)


my_list = [6, 8, 4, 2, 9, 0, 1, 2, 76, 5]
list_size = len(my_list)

print('Unsorted List')
print(my_list)

quick_sort(my_list, 0, list_size - 1)
print('Sorted List')
print(my_list)


new_list = []
num_of_elements = int(input('Enter number of Elements to be sorted: ')) + 1

for i in range(1, num_of_elements):
    # take string input as int for sorting
    num = int(input(': '))
    new_list.append(num)

new_list_size = len(new_list)
print('Entered list')
print(new_list)
quick_sort(new_list, 0, new_list_size - 1)
print('Sorted list')
print(new_list)
