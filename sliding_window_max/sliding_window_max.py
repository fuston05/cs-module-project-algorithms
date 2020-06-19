'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    maxList = []
    # set window range
    windowFirst = 0
    windowLast = windowFirst+(k-1)
    while windowLast != len(nums):
        curMax = nums[windowFirst]
        print(f'1st: {windowFirst}')
        print(f'lasst: {windowLast}')

        # iterate through window
        for i in range(windowFirst, windowLast+1):
            print(f'i: {i}')
            if nums[i] > curMax:
                curMax = nums[i]
                print(f'curMax: {curMax}')
        maxList.append(curMax)
        # move the window by 1
        windowFirst += 1
        windowLast += 1
    return maxList

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    # Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Expected Output: [3,3,5,5,6,7]

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
