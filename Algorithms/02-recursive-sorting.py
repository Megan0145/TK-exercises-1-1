# CHALLENGE ONE 
# 1.Write a recursive search function that receives as input an array of 
# integers and a target integer value. 
# This function should return True if the target element exists in the array, and False otherwise.

# binary search

def bin_search(arr, target, l, r):
    l = 0
    r = len(arr) - 1

    # base case
    if r >= l :

        # get index of middle element
        mid =  l + r // 2
        
        # <- conditions ->
        # if element at middle of array == target, target has been found
        if arr[mid] == target:
            return True

        # if element at middle index smaller than target, target must be on RHS -> eliminate LHS 
        # recur passing in mid + 1 as value of l, so that it will only search from index of mid + 1 (RHS of array)
        elif arr[mid] < target:
            return bin_search(arr, target, mid + 1, r)

        # if element at middle index larger than target, target must be on LHS -> eliminate RHS 
        # recur passing in mid - 1 as value of r, so that it will only search from l to index of mid - 1 (LHS of array)
        if arr[mid] > target:
            return bin_search(arr, target, l, mid - 1)
    
    # else must not be present in array
    else:
        return False

#2.What would be the base case(s) we’d have to consider for implementing this function?
    -> The way I have implemented it above, using l and r variables corresponding to the 
    indexes the function should be searching from and to (effectively the range), the value of r must always be larger than l. 
    If the value of r is equal to or less than r, it means that the array is of length 0 and the target
    element must not have been found; return False
    ->Alternatively I could have written the base case to be directly checking that the length of the array was more than 0.
    For example, only running the main loop while len(arr) > 0 and breaking out of the loop and returning False if not

#3.How should our recursive solution converge on our base case(s)?
    The recursive solution gradually converges on the base case by setting l equal to the value of the middle index of the array plus 
    one if the element at the middle index is less than the target OR by setting the value or r equal to the value of the middle index of the array minus 
    one if the element at the middle index is more than the target. This essentially decreases the range of values the function is searching over - halving them each time. 
    Naturally the function will reach a point that it has found the target element or the len of array is not bigger than 1, at which point it returns False


# CHALLENGE TWO
#1. What will the contents of the array below be after each pass of the Merge Sort algorithm?

-> | 39 | 51 | 7 | 14 | 3 | 86 |

-> | 39 | 51 | 7 |      | 14 | 3 | 86 |

-> | 39 | 51 |      | 7 |      | 14 | 3 |      | 86 |

-> | 39 |    | 51 |    | 7 |    | 14 |    | 3 |    | 86 |

-> | 39 | 51 |      | 7 |      | 3 | 14 |      | 86 |

-> | 7 | 39 | 51 |      | 3 | 14 | 86 |

-> | 3 | 7 | 14 | 39 |51 | 86 |


#2. What will the contents of the array below be after each pass of the Quick Sort algorithm? (assume the first element is chosen as the pivot)

 ->  24 | 44 | 12 | 99 |  3 | 56
 ->  12 |  3 | 24 | 44 | 99 | 56
 ->  3 |  12 | 24 | 44 | 99 | 56
 ->  3 |  12 | 24 | 44 | 99 | 56
 ->  3 |  12 | 24 | 44 | 56 | 99