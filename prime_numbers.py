#a prime number is a number only divisible by itself and 1

#version 1: I'm going try out the logic using the first number to see if it works before iterating for all the numbers
n = 20 #upper limit of numbers we want to pick from
number_range = set(range(2, n+1))
primes_list = []

prime = number_range.pop() #we want to extract the first prime number from the list so we can remove it by using pop
primes_list.append(prime)
multiples = set(range(prime*2, n+1, prime))
number_range.difference_update(multiples)

#version 2
#upper limit of numbers we want to pick from
n = 20

#number range to be checked: I use the range function to set it. 
number_range = set(range(2, n+1))

#create an empty list that I can append the discovered primes to
primes_list = []

#Using the while loop to put in conditions for what is needed in the loop
while number_range:
    prime = number_range.pop() #we want to extract the first prime number from the list so we can remove it by using pop
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    
#I want to print the list of primes to see if the logic works as intended
print(primes_list)

#I can use the length function to see number of primes that were found in the set range
prime_count = len(primes_list)

#Playing around with the data: Using the max function to see the Largest prime number in the range
largest_prime = max(primes_list)

#Customizing the output summary to give a statement of the results
print(f" There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")    

#Using the same logic above, I can change the sample size
n = 100

#Setting the range
number_range = set(range(2, n+1))

#empty list to append discovered primes to
primes_list = []

#while loop
while number_range:
    prime = number_range.pop() #we want to extract the first prime number from the list so we can remove it by using pop
    primes_list.append(prime)
    multiples = set(range(prime*2, n+1, prime))
    number_range.difference_update(multiples)
    
#print the list of primes
print(primes_list)

#number of primes that were found
prime_count = len(primes_list)

#Largest prime
largest_prime = max(primes_list)

#summary
print(f" There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")    

#version 3 : Creating a function to use for the logic

def primes_finder(n):
  
    #number range to be checked
    number_range = set(range(2, n+1))

    #empty list to append discovered primes to
    primes_list = []

    #while loop
    while number_range:
        prime = number_range.pop() #we want to extract the first prime number from the list so we can remove it by using pop
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples)
        
    #print the list of primes
    print(primes_list)

    #number of primes that were found
    prime_count = len(primes_list)

    #Largest prime
    largest_prime = max(primes_list)

    #summary
    print(f" There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}")    

    return primes_list

primes_finder(100)   
primes_list = primes_finder(100)
print(primes_list) 


#Creating the function enables us to be able to just plug in any random number and get the prime numbers in that range. 

primes_finder(1000)  
primes_list = primes_finder(1000)
print(primes_list) 

#Try this out with any number range and see it return you a complete list. Have fun, and thanks for following along! 
