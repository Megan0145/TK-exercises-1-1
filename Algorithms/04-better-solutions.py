# 1 What are some of the tradeoffs exhibited between the recursive Nth Fib solution 
# that utilizes memoization and the iterative Nth Fib solution?

# Recursive: 
#     Using memoization to store (or 'cache') the result of an operation that's performed 
#     repeatedly so that it won't be evaluated on every recursive call to the function (eg in the Fib solution, as n gets smallers, 
#     before it reaches the base case (0 or 1) many operations will be repeated)
#     means that we must allocate a space in memory to store the results and on every recursive call of the function, 
#     search through this space in memory and see if it has already been evaluated (if not, continue to rest of function to 
#     evaluate result) -> more overhead, creates a call stack
# Iterative:
#     As explained above, it's possible that with an iterative approach you'll end up making multiple calls for the same number.
#  eg fib(4):
# 1st call: fib(4 - 1) + fib(4 - 2) = fib(3) + fib(2)
# 2nd call: fib(3 - 1) + fib(0) = fib(2) + fib(0)
# The value of fib(2) will already have been calculated in the 1st call but (without using memoization) will need to be evaluated in the second call again


# 2 Our memoized recursive solution is quite space-inefficient due to the fact that 
# we’re now caching every single answer up to the input n. Could we improve upon our 
# recursive solution even further such that it’s more space efficient?