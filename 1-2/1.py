#  Найти первое вхождение

def solution(nums, x):
    for i, n in enumerate(nums):
        if n == x:
            return i
    else:
        return -1


print(solution([1, 2, 1, 3, 2], 2) == 1)
print(solution([1, 2, 1, 3, 2], 5) == -1)
print(solution([1, 2, 1, 3, 2], 1) == 0)
print(solution([1, 2, 1, 3, 20], 20) == 4)
print(solution([1], 1) == 0)
print(solution([], 1) == -1)

