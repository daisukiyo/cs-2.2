def max_sub_array_sum(a, size):

    # base case
    max_so_far = a[0]
    current_max = a[0]

    # iterate through the given array
    for i in range(1, size):
        # build sum contiguous segments
        current_max = max(a[i], current_max + a[i])
        # keep track of maximum sum contiguous segments
        max_so_far = max(max_so_far, current_max)
    return max_so_far

if __name__ == "__main__": 
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    print('Solution:')
    print('For this input: ', a)
    print('The optimal solution is: ', max_sub_array_sum(a,len(a)) )
    print('\nReasoning:')
    print('Contiguous Subarray: {4, -1, 2, 1}') 
    