'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    productArr = [1] * len(arr)
    # loop 1st against all others
    for i in range(0, len(arr)):
        for k in range(0, len(arr)):
            # do not multiply by self
            if i != k:
                productArr[i] = productArr[i] * arr[k]
                print(productArr[i])
    return productArr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr1 = [12, 2, 7, 2, 8]
    arr2 = [1, 7, 3, 4]  # [84, 12, 28, 21]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr2)}")
