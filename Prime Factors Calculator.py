# Function to check if a number is prime
def check_prime(potential_prime):
    if potential_prime > 1:                       # proceeds with test if the number is not 1 or negative, which are by default not prime
        for i in range(2, potential_prime//2+1):    # creates loop for numbers that will be used to test for remainders
            if (potential_prime % i) == 0:                   # if any of these numbers returns a remanider of 0, number cannot be prime 
                return False  # declares the number as not prime.
                break                               # breaks out of the test loop when any number returns a remainder of 0
        else:                                       # if no number returned a remainder of 0...
            return True     # we can declare the number as a prime number
    else:                                           # accounts for input of 0, 1, and negatives, which are by default not prime.
        return False

check_prime(197)

# Function to check if a number is a factor of another
def check_factor(potential_factor, number):                                          
    if number % potential_factor == 0:          # if the number when divided by the potential factor has no remainders...
        return True                             # the potential factor is a factor
    else:                                       # otherwise...
        return False                            # it is not a factor

check_factor(19,85)

# Finding prime factors of a number
number = int(input("Enter a positive integer: "))                      # asks the user for the pos integer to test
for i in range(2,number//2+1):                        # creates loop for numbers 'i' that will be evaluated for prime and factor
    if check_prime(i) == True and check_factor(i, number) == True:     # if both tests return True for i
        print(i)                                                       # print it as a prime factor