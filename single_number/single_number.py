'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# first pass
def single_number(nums):
    # first-pass solution
    # we'll keep an array, call it `no_dups` to hold numbers we see in the nums array
    no_dups = []
    # interate through nums
    for x in nums:
        # check to see if the number is already in the `no_dups` array
        if x not in no_dups:
            no_dups.append(x)
        # if it is, remove it from the `no_dups` array
        else:
            no_dups.remove(x)
    # when we're done iterating, the only number in our `no_dups` array is the 
    # odd number out
    # return it
    return no_dups

# improved version
def single_number(nums):
    # first-pass solution
    # we'll keep an array, call it `no_dups` to hold numbers we see in the nums array
    no_dups = []
    # interate through nums
    for x in nums:
        # check to see if the number is already in the `no_dups` array
        if x not in no_dups:
            no_dups.append(x)
        # if it is, remove it from the `no_dups` array
        else:
            no_dups.remove(x)
    # when we're done iterating, the only number in our `no_dups` array is the 
    # odd number out
    # return it
    return no_dups

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")