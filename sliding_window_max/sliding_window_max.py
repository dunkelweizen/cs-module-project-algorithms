'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    windows = len(nums) - (k - 1)
    window_nums = []
    result = []
    start = 0
    stop = k
    for i in range(windows):
        window_nums.append(nums[start:stop])
        start += 1
        stop += 1
    window_nums = list(map(sorted, window_nums))
    for subl in window_nums:
        result.append(subl[-1])

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
