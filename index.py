import logging
import os
from datetime import datetime
import random


def setup_logger(name, log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    handler = logging.FileHandler(os.path.join('logs', log_file), encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

    logger.addHandler(handler)
    return logger


# Пузырьковая сортировка

def bubble_sort(nums):
    logger = setup_logger('bubble_sort', 'bubble_sort.log')
    logger.info(f"Начало сортировки пузырьком с массивом: {nums}")
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                logger.info(f"Замена {nums[i]} и {nums[i + 1]}")
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    logger.info(f"Сортировка пузырьком завершена. Результат: {nums}")


random_list_of_nums = [round(random.uniform(1.0, 10.0), 2) for _ in range(5)]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

# Сортировка выборкой

def selection_sort(nums):
    logger = setup_logger('selection_sort', 'selection_sort.log')
    logger.info(f"Начало сортировки выбором с массивом: {nums}")
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        if lowest_value_index != i:
            logger.info(f"Замена {nums[i]} и {nums[lowest_value_index]}")
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    logger.info(f"Сортировка выбором завершена. Результат: {nums}")


random_list_of_nums = [random.randint(60, 100) for _ in range(5)]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

# Сортировка вставками

def insertion_sort(nums):
    logger = setup_logger('insertion_sort', 'insertion_sort.log')
    logger.info(f"Начало сортировки вставками с массивом: {nums}")
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        logger.info(f"Текущий элемент для вставки: {item_to_insert}")
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            logger.info(f"Перемещение {nums[j]} на одну позицию вперед")
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    logger.info(f"Сортировка вставками завершена. Результат: {nums}")


random_list_of_nums = [random.randint(18, 65) for _ in range(5)]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)

# Пирамидальная сортировка

def heapify(nums, heap_size, root_index, logger):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
        logger.info(f"Левый потомок {nums[left_child]} больше корня {nums[root_index]}")

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
        logger.info(f"Правый потомок {nums[right_child]} больше текущего наибольшего {nums[largest]}")

    if largest != root_index:
        logger.info(f"Замена {nums[root_index]} и {nums[largest]}")
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest, logger)


def heap_sort(nums):
    logger = setup_logger('heap_sort', 'heap_sort.log')
    logger.info(f"Начало пирамидальной сортировки с массивом: {nums}")
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i, logger)

    for i in range(n - 1, 0, -1):
        logger.info(f"Перемещение наибольшего элемента {nums[0]} в конец")
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0, logger)

    logger.info(f"Пирамидальная сортировка завершена. Результат: {nums}")


random_list_of_nums = [random.randint(-10, 40) for _ in range(5)]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

# Сортировка слиянием

def merge(left_list, right_list, logger):
    logger.info(f"Слияние списков: {left_list} и {right_list}")
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                logger.info(f"Добавление {left_list[left_list_index]} из левого списка")
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                logger.info(f"Добавление {right_list[right_list_index]} из правого списка")
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            logger.info(f"Добавление оставшегося {right_list[right_list_index]} из правого списка")
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            logger.info(f"Добавление оставшегося {left_list[left_list_index]} из левого списка")
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    logger.info(f"Результат слияния: {sorted_list}")
    return sorted_list


def merge_sort(nums):
    logger = setup_logger('merge_sort', 'merge_sort.log')
    logger.info(f"Начало сортировки слиянием с массивом: {nums}")

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    logger.info(f"Разделение массива по индексу {mid}")

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    result = merge(left_list, right_list, logger)
    logger.info(f"Результат сортировки слиянием: {result}")
    return result


random_list_of_nums = [random.randint(30000, 120000) for _ in range(5)]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)

# Быстрая сортировка

def partition(nums, low, high, logger):
    pivot = nums[(low + high) // 2]
    logger.info(f"Разделение с опорным элементом {pivot}")
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            logger.info(f"Разделение завершено на индексе {j}")
            return j

        logger.info(f"Замена {nums[i]} и {nums[j]}")
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    logger = setup_logger('quick_sort', 'quick_sort.log')
    logger.info(f"Начало быстрой сортировки с массивом: {nums}")

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high, logger)
            logger.info(f"Рекурсивная сортировка левой части: {items[low:split_index + 1]}")
            _quick_sort(items, low, split_index)
            logger.info(f"Рекурсивная сортировка правой части: {items[split_index + 1:high + 1]}")
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    logger.info(f"Быстрая сортировка завершена. Результат: {nums}")


random_list_of_nums = [random.randint(100, 10000) for _ in range(5)]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

