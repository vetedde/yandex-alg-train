# Найти максимальное число в последовательности
"""
1. Полный проход и находим самое большое
2. Проход с двумя поинтерами
3. Отсортировать и взять последнее(n log n)
4.

"""


def solution_1(nums):
    max_n = nums[0]
    n_p = 0
    for i, n in enumerate(nums):
        if n > max_n:
            max_n = n
            n_p = i

    return max_n, n_p


def solution_2(nums):
    max_num_pointer = 0
    for i, n in enumerate(nums):
        if n > nums[max_num_pointer]:
            max_num_pointer = i

    return nums[max_num_pointer], max_num_pointer

print("Test alg 1")
print(solution_1([1,2,3]) == (3, 2))
print(solution_1([1,3,2]) == (3, 1))
print(solution_1([3,1,2]) == (3, 0))
print(solution_1([3,3,2]) == (3, 0))
print(solution_1([3]) == (3, 0))
print(solution_1([-3, -1, -9]) == (-1, 1))
print(solution_1([-3, 3]) == (3, 1))

print("\nTest alg 2")
print(solution_2([1,2,3]) == (3, 2))
print(solution_2([1,3,2]) == (3, 1))
print(solution_2([3,1,2]) == (3, 0))
print(solution_2([3,3,2]) == (3, 0))
print(solution_2([3]) == (3, 0))
print(solution_2([-3, -1, -9]) == (-1, 1))
print(solution_2([-3, 3]) == (3, 1))


# print(solution([1,2,3]) == (3, 2))
# print(solution([1,3,2]) == (3, 1))
# print(solution([3,1,2]) == (3, 0))
# print(solution([3,3,2]) == (3, 0))
# print(solution([3]) == (3, 0))
# print(solution([-3, -1, -9]) == (-1, 1))
# print(solution([-3, 3]) == (3, 1))
