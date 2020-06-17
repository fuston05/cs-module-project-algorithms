'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # take one index at a time, and check through the list
    for i in range(0, len(arr)-1):
        appeared= 1
        for k in range(0, len(arr)-1):
            # dont check against self
            if i != k:
                # does i have a pair?
                if arr[i] == arr[k]:
                    # if we find it's mate
                    appeared+=1
        if appeared != 2:
            return arr[i]
                


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr1= [555, 827, 555, 827, 654]

    print(f"The odd-number-out is {single_number(arr1)}")