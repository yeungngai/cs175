#******************
# Lab 9: Exercise 1
# Author: Yi Yang
# Collaborators/References: C175-12-F20-Sorting.pdf file from eclass
#******************

import random
import time


def recursive_selection_sort(data, data_len, index = 0): 
    '''
    Use Selection Sort to arrange the integers in a list (data) in descending order
    Inputs:
       data (list) - list of integers to be sorted
       data_len (int) - number of elements in the data
       index (int) - index of starting element
    Returns: None
    '''

    bigIndex = index
    if index == data_len:
        return None
    else:
        for i in range(index, data_len):
            if data[i] > data[bigIndex]:
                bigIndex = i

        if bigIndex != index:
            temp = data[index]
            data[index] = data[bigIndex]
            data[bigIndex] = temp

        return recursive_selection_sort(data, data_len, index + 1)

  
def recursive_merge_sort(data): 
    '''
    Use MergeSort to arrange the integers in a list (data) in descending order
    Inputs:  data (list) - list of integers to be sorted
    Returns: sorted data list
    '''

    if len(data) <= 1:
        return data

    middle = len(data)//2

    left = recursive_merge_sort(data[:middle])
    right = recursive_merge_sort(data[middle:])

    return merge(left, right)


def merge(left, right):
    '''
    merges the split data to a new list and returns the result
    '''

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    start_sel = time.time()
    recursive_selection_sort(random_list, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))


    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    start_sel = time.time()
    recursive_selection_sort(ascending_list, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()

    # Print the rsults execution time to sort a list of intergers already sorted in ascending order
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))


    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    start_sel = time.time()
    recursive_selection_sort(descending_list, list_len)
    end_sel = time.time()

    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()

    # Print the results execution time to sort a list of intergers already sorted in descending order
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
