# Найти максимальное число и второе после него

def solution_1(nums):
    max_n_p = 0
    second_max_n_p = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[max_n_p]:
            second_max_n_p = max_n_p
            max_n_p = i

        if second_max_n_p == 0 and max_n_p == 0:
            if nums[i] < nums[second_max_n_p]:
                second_max_n_p = i

    return (nums[second_max_n_p], nums[max_n_p])

def solution_2(nums):
    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])
    for i in range(3, len(nums)):
        if nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i] > max2:
            max2 = nums[i]

    return (max1, max2)


print(solution_1([1,2,3]) == (2, 3))
print(solution_1([2,2,3]) == (2, 3))
print(solution_1([3,2,3]) == (2, 3))
print(solution_1([3,3]) == (3, 3))
print(solution_1([3, 3, 2]) == (2, 3))
print(solution_1([-3,3]) == (-3, 3))
print(solution_1([-3,-9]) == (-9, -3))
