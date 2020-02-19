# CHALLENGE 1
# Given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, 
# write a function rotate_image that receives a matrix as input and rotates the image by 90 degrees in the 
# counter-clockwise direction.

A = [
    [12, 7, 8],
	[ 4, 5, 6],
	[ 1, 7, 8]
    ]

T = [
    [0,0,0],
	[0,0,0],
	[0,0,0]
    ]
# loop from 0 - 2 inclusive    
for k in range(len(A)):
    # loop from 0 - 2 inclusive
    for j in range(len(A[0])):
        # transpose elements at cur index
        T[j][k] = A[k][j]



# T[0][0] = A[0][1]
# T[0][1] = A[0][2]
# T[0][2] = A[1][2]
# T[1][0] = A[0][0]
# T[1][1] = A[1][1]
# T[1][2] = A[2][2]
# T[2][0] = A[1][0]
# T[2][1] = A[2][0]
# T[2][2] = A[2][1]

for r in T:
	print(r)

# This rotates clockwise ^. More work to be done.



# CHALLENGE 2:
# Classify the runtimes of each of the following functions:

# 1
def foo(n):
  sq_root = int(math.sqrt(n)) 
  for i in range(0, sq_root): 
    print(i)

# Logarithmic: 
# as the size of n increases, so too will the amount of times the loop runs, 
# but only slightly as it it only prints sqrt(n) times 
# O(log n)

# 2
def bar(x):
  sum = 0
  for i in range(0, 1463):
    i += sum
    for j in range(0, x):
      for k in range(x, x + 15):
        sum += 1

# 3
def baz(array):
  print(array[1])
  midpoint = len(array) // 2
  for i in range(0, midpoint):
    print(array[i])
  for _ in range(1000):
    print('hi')