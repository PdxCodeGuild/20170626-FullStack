
# lab 8: check if a number is prime
# a number is prime if it can only be divided by 1 and itself


# returns true if 'a' is divisiable by 'b'
# the modulus a%b returns the remainder of a/b
# e.g. is_divisible(16,4) would be 'true'
# but is_divisable(17,4) would be 'false' because 17%4 == 1
def is_divisible(a, b): 
	return a%b == 0

def is_prime(v):
	for i in range(2,v): # check all numbers from 2 to v-1
		if is_divisable(v,i): # if v is divisible by i, v is not prime, return false
			return False
	return True

value = int(input('what is the number? ')) #get the number from the user
print(is_prime(value)) #print whether the value is prime

