"""
Created By: Uee
Modified By:
"""

def MerseenePrime(n = 31):
	return pow(2, n) - 1

def LCG(a = 0, c = 0, pin = 0, prime = 1, iterations = 1):
	"""
	The Linear Congruential Number Generator computes random values using the Formula: X(n-1) = (aX(n) + c) mod m.
	It should be noted that LCGs are vulnerable to attacks if they are used to generate keys in a crypto-system or in
	similar situations because it is possible to recover the parameters of LCGs in polynomial time given several
	observed outputs.
	:param a:
	:param c:
	:param pin:
	:param prime:
	:param iterations:
	:return:
	"""
	values = [pin]  # List of randomly Generated Numbers

	for i in range(iterations):
		values.append(
			((a * values[i]) + c) % prime)  # Calculate a Random Number using the Linear Congruential Generator Formula

	return values

def Hash(pin = 0):
	"""
	The Hash Function will output a 16bit key from a Pin composed of 4 integers using the Linear Congruential Number
	Generator.
	:param pin:
	:return:
	"""

	# Check that pin satisfies the condition 0 < pin < 9999
	if pin < 0 or pin > 9999:
		return 0

	values = LCG(a, c, pin, prime, iterations)  # List of LCG numbers
	key = 1  # Default Hash Value
	div = 2  # Divisor for reducing the number of iterations.

	while True:
		for number in values:
			# Calculate a Hash
			key += number + pin

			# Check if the Hash is 16bits long
			if int(key).bit_length() == 16:
				return key

			# Check if the Hash is more than 16bits
			elif int(key).bit_length() > 16:
				# Recalculate LCG numbers
				values = LCG(a, c, pin, prime, int(iterations / div))
				div += 1
				key /= div

def BlumBlumGenerator(key = 0, BI = 0, n = 0):
	"""
	Blum Blum Generator is a random bit Generator using the simple form: X(n+1) = (Xn^2 mod M), where M is the product
	of 2 Large Distinct Primes and the Output is the Least Significant bit of X(n+1) or the Parity of X(n+1).
	:param key:
	:param BI:
	:param n:
	:return:
	"""
	cipher = [key]

	for i in range(n):
		cipher.append((cipher[i - 1] ** 2) % BI)

	return cipher

a = 2147483629
c = 2147483587

prime = MerseenePrime()

pin = 1234

iterations = pin

BI = (978349 * 823177)
N = len(str(pin))

# Calculate the Key
key = Hash(pin)
print("The key is: " + str(key))

# Do Blum Blum Generation
cipher = BlumBlumGenerator(key, BI, N)
print("The Cipher is: ", end = '')
print(cipher)
