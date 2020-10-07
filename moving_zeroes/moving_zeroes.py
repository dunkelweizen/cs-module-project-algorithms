'''
Input: a List of integers
Returns: a List of integers
Need all non-zero integers on left side of array, all zeroes on right side
One traversal, O(1) space
'''


def moving_zeroes(arr):
    print(arr)
    pointer = len(arr) - 1
    while arr[pointer] == 0 and pointer >= 0:
        # if right is already zeroes, move pointer to left
        pointer -= 1
    if pointer < 0:
        # list is all zeroes, can stop
        return arr
    for i in range(pointer + 1):
        print("i",i)
        print("starting pointer", pointer)
        if i == pointer:
            # stop when pointers meet
            break
        # check if value is zero
        if arr[i] == 0:
            # if zero, swap value with pointer
            arr[i], arr[pointer] = arr[pointer], arr[i]
            print(arr)
            # then bring pointer backward
            pointer -= 1
        if i == pointer:
            # stop when pointers meet
            break
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
