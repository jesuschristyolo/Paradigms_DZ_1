import random
from random import randint
def sort_list_imperative(numbers):
    if len(numbers) <= 1:
        return numbers

    support_element = numbers[(len(numbers)- 1)//2]

    left_list = list(filter(lambda x: x > support_element, numbers))
    mid = list(filter(lambda x: x == support_element, numbers))
    right_list = list(filter(lambda x: x < support_element, numbers))

    return sort_list_imperative(left_list) + mid + sort_list_imperative(right_list)


def sort_list_declarative(numbers):
    return sorted(numbers, reverse= True)


for i in range(0, random.randint(0, 10)):
    coll = [randint(1, 100) for _ in range(1, randint(0, 20))]
    print(coll)
    print('В императивном стиле: ', sort_list_imperative(coll))
    print('В декларативном стиле: ', sort_list_declarative(coll))
    print('_-_' * 20)





















