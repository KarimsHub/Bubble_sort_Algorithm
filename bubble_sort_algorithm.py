import random
import time


def random_numbers_generator():
    l = []
    for i in range(999):
        l.append(random.randint(0,999))
    return l

unsorted_l = random_numbers_generator()

start = time.time()

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(0, len(unsorted_list) - 1 - i): # have to stop one element before the end because of changing the elements and we can shorten the list
            if unsorted_list[j] > unsorted_list[j + 1]: # if the first element is bigger than the next element we have to sort
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j] # changing the values of both elements
    return unsorted_list

print(bubble_sort(unsorted_l))
end = time.time()
print(end - start) # checks the amount of time the algorithm needs to sort the list