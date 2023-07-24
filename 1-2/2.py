# Найти последнее вхождение числа Х или -1, если оно не встречалось


def solution_1(nums, x):  # Сложность O(N)
    ans = -1
    p = len(nums) - 1
    while p >= 0:
        if nums[p] == x:
            ans = p
            break
        p -= 1
    return ans


def solution_2(nums, x):  # Сложность O(N)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == x:
            return i
    else:
        return -1


print("Test alg 1")
print(solution_1([1, 2, 1, 3, 2], 2) == 4)
print(solution_1([1, 2, 1, 3, 2], 5) == -1)
print(solution_1([1, 2, 1, 3, 2], 1) == 2)
print(solution_1([1, 2, 1, 3, 20], 20) == 4)
print(solution_1([1], 1) == 0)
print(solution_1([], 1) == -1)

print("\nTest alg 2")
print(solution_2([1, 2, 1, 3, 2], 2) == 4)
print(solution_2([1, 2, 1, 3, 2], 5) == -1)
print(solution_2([1, 2, 1, 3, 2], 1) == 2)
print(solution_2([1, 2, 1, 3, 20], 20) == 4)
print(solution_2([1], 1) == 0)
print(solution_2([], 1) == -1)