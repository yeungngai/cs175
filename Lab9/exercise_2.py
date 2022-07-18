#******************
# Lab 9: Exercise 2
# Author: Yi Yang
# Collaborators/References: The recursive_merge_sort function is a reference from the exercise_1.py file.
#******************

class Student():
    def __init__(self, idNum, name, mark):
        '''Initialize the object properties'''
        self.__id = idNum
        self.__name = name
        self.__mark = mark

    def getMark(self):
        '''Returns the value of the Student's mark'''
        return self.__mark    

    def __str__(self):
        '''Informal string representation of Student'''
        return ' - {}, {}, {}'.format(self.__id, self.__name, self.__mark)

    def __lt__(self, anotherStudent):
        ''' 
        Checks if the mark of the student is less than the mark of another 
        Student object
        Input: anotherStudent (Student)
        Returns: boolean
        '''

        if self.__mark < anotherStudent.getMark():
            return True
        else:
            return False


def recursive_merge_sort(data):
    '''
    Uses MergeSort to sort the list of data in INCREASING order
    Returns: the sorted list of Students  
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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if  __name__== "__main__":
    # Read the data
    students_file = open('student_list.txt', 'r')
    students_data = students_file.readlines()
    student_list = []
    
    # Create a Student object corresponding to each line in input file
    for student in students_data:
        fields = student.split(', ')
        ID = fields[0]
        name = fields[1]
        mark = fields[2]
        student_list.append(Student(ID, name, int(mark)))

    # Print the original data
    print('Original data:')
    for student in student_list:
        print(student)

    # Sort the students
    sorted_students = recursive_merge_sort(student_list)

    studentMark = student_list[0].getMark()

    # Print the sorted data
    print('Sorted data:')
    for student in sorted_students:
        print(student)
