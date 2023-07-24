# Найти минимальное четное число в последовательности, вывести -1 если такого не существует

def solution(nums):
    min_n = -1

    for n in nums:
        if n % 2 == 0 and (n < min_n or min_n == -1):
            min_n = n

    return min_n


def solution_2(nums):
    isMeetChetNum = False
    min_n = None

    for n in nums:
        if n % 2 == 0 and (not isMeetChetNum or n < min_n):
            isMeetChetNum = True
            min_n = n

    return min_n if isMeetChetNum else -1

print(solution([2,4,8]) == 2)
print(solution([1,4,8]) == 4)
print(solution([1,4,2]) == 2)
print(solution([2]) == 2)
print(solution([1]) == -1)
print(solution([0]) == 0)
print(solution([9,-4,-2,6,7]) == -4)
print(solution([]) == -1)

print("\n Test alg2")
print(solution_2([2,4,8]) == 2)
print(solution_2([1,4,8]) == 4)
print(solution_2([1,4,2]) == 2)
print(solution_2([2]) == 2)
print(solution_2([1]) == -1)
print(solution_2([0]) == 0)
print(solution_2([9,-4,-2,6,7]) == -4)
print(solution_2([]) == -1)

