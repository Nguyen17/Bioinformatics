# @nguyen17.github
# Assignment #4: Rabbits and Recurrence Relations


"""
A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π)(π,−2,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…)(1,3,5,7,9,…). We use the notation anan to represent the nn-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if FnFn represents the number of rabbit pairs alive after the nn-th month, then we obtain the Fibonacci sequence having terms FnFn that are defined by the recurrence relation Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 (with F1=F2=1F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the nn-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of nn. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

	Given: Positive integers n≤40 and k≤5.

	Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).

Test case:
input: 5 3
output: 19

"""

# MAIN CODE HERE

def rabbitPairs(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        current = previous1 + k * previous2
        previous2 = previous1
        previous1 = current
    return current

x = int(input("Enter Months: "))
y = int(input("Enter number of offsprings: "))
result = rabbitPairs(x,y)
print(result)



# - -
# Alternative
"""
#1:
@Vladislav
	fibocache = {}
	
	def fibo(n,k):
	    if n == 2 or n == 1:
	        return 1
	    if (n,k) not in fibocache:
	        fibocache[(n,k)] = fibo(n-1,k) + fibo(n-2,k) * k
	    return fibocache[(n,k)]

print ( fibo( 40, 3) )


"""