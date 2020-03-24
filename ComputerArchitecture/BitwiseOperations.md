## Answers should be viewed raw - formatted funny

# Q1: How would you perform an NOR operation between two numbers x and y if you didn’t have an NOR operator?How could you use the other bitwise operators to the same effect?

Determine whether x or y is true and return the inverse of that result.
If you're working with boolean values x NOR y will be: !(x || y)
If you're working with bitwise operators x NOR y will be: ~(x | y)

# Q2: How would you perform an XOR operation between two numbers x and y if you didn’t have an XOR operator? How could you use the other bitwise operators to the same effect?

Determine whether x or y is true but only return true if both of them aren't true (true if x is true or y is true but not both).
If you're working with boolean values x XOR y will be: (x || y) && (x && y)
If you're working with bitwise operators x XOR y will be: x ^ y

# Q3: What is the result of 11011111 NOR 00010111?

       11011111
NOR    00010111
---------------
>       00100000

# Q4: What is the result of 10101010 XOR 11110000?

       10101010
XOR    11110000
---------------
>       01011010

# Q5: What is the result of 11011 AND 101?
       00011011
AND    00000101
---------------
>       00000001