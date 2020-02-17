# Test array
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19]

# CHALLENGE ONE:

#1: Try writing a Python function to perform a linear search on a set of data.

# start from leftmost element in arr and compare element with num.
# if element != num and i is less than length of array, move onto the next element and compare
# continue doing this so long as i < length of array. If element eventually == num, -> return element and index. If i = length of array - 1 and still the element hasn't been found -> return num not in list

def linear_search(num, array):
  for i in range(len(array)):
    if array[i] == num:
      return f'{array[i]}, idx = {str(i)}'
  return f'{num} not present in list'

# CHECK:
linear = linear_search(15, arr)
print(linear)



#2: Try writing a Python function to perform a binary search on a set of data.

def binary_search(num, array):
  left = 0
  right = len(array) - 1
  # if right ever becomes less than left, than we must have sorted through whole array -> number is not present in array
  while right >= left:
    # get middle element of array - has to be rounded to convert it to an int instead of float; can't reference something at index 2.5
    mid = round(left + (right - left)/2)
    # if element at index of middle of array == num: return element and its index
    if array[mid] == num:
      return f'{array[mid]}, idx = {str(mid)}'
    # if element at index of middle of array < num, num must be on RHS of element at index of middle of array. Therefore, set left to equal the value of mid + 1 to make sure we are only iterating over RHS of array 
    elif array[mid] < num:
      left = mid + 1
    # if element at index of middle of array > num, num must be on LHS of element at index of middle of array. Therefore, set right to equal the value of mid - 1 to make sure we are only iterating over LHS of array
    elif array[mid] > num:
      right = mid - 1
  # if nothing returned and left is no longer less than right, number must not be present in array -> return 'not in array'
  return f'{num} not present in list'

# CHECK
binary = binary_search(15, arr)
print(binary)


#3: Can you rewrite the above function so that it uses recursion?

def recursive_binary_search(array, left, right, num):
  while right >= left:
    mid = round(left + (right - left)/2)
    if array[mid] == num:
      return f'{array[mid]}, idx = {str(mid)}'
 
    elif array[mid] < num:
      return recursive_binary_search(array, mid + 1, right, num)

    elif array[mid] > num:
      return recursive_binary_search(array, left, mid - 1, num)

  return f'{num} not present in list'

#CHECK:
rec_binary = recursive_binary_search(arr, 0, len(arr) -1, 15)
print(rec_binary)


# CHALLENGE TWO

#1: What will the contents of the array below look like after each pass of the Selection Sort algorithm?

    ->  25 | 67 |  4 | 33 | 19 | 40
    ->   4 | 67 | 25 | 33 | 19 | 40
    ->   4 | 19 | 25 | 33 | 67 | 40
    ->   4 | 19 | 25 | 33 | 67 | 40
    ->   4 | 19 | 25 | 33 | 40 | 67
     ->  4 | 19 | 25 | 33 | 40 | 67

#2: What will the contents of the same array look like after each pass of the Insertion Sort algorithm?

    ->  25 | 67 |  4 | 33 | 19 | 40
    ->   4 | 25 | 67 | 33 | 19 | 40
    ->   4 | 19 | 25 | 67 | 33 | 40
    ->   4 | 19 | 25 | 33 | 67 | 40
    ->   4 | 19 | 25 | 33 | 67 | 40
    ->   4 | 19 | 25 | 33 | 40 | 67
