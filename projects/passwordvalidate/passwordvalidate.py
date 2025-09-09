import random

def validate(password): 
	""" Analyzes an password to determine if it is "Secure", "
	Insecure", or "Invalid" based on the assignment description criteria.

	Arguments:
		password (string): a string of characters

	Returns:
		result (string): either "Secure", "Insecure", or "Invalid".

	"""
	
	has_upper = False
	has_lower = False
	has_digit = False
	has_special = False

	special_char_list = ["!", "-", "$", "%", "'", "(", ")", "*", "+", ",",
						 ".", "/", ":", ";", "<", "=", ">", "?", "_", "[", 
						 "]", "^", "`", "{", "|", "}", "~"]

	if len(password) < 8:
		return "Invalid"

	# Loops through the string input and sets the value
	# of if a variable to true if they belong 		
	# to a certain group of characters

	for p in password:
		if p in [' ', '','@', '#', ]:
			return "Invalid"
		elif p.isupper():
			has_upper = True
		elif p.islower():
			has_lower = True
		elif p.isdigit():
			has_digit = True
		elif p in special_char_list:
			has_special = True

	# If any of the four variables evaluate to false
	# the password is Insecure
	# If none of the variables evaulte to false
	# then the string contains all of the four
	# charactesr required and is secure
	if has_upper == False:
		return "Insecure"
	elif has_lower == False:
		return "Insecure"
	elif has_digit == False:
		return "Insecure"
	elif has_special == False:
		return "Insecure"
	else:
		return "Secure"


def generate(n):
	""" Generates a password of length n which is guaranteed to be Secure
	according to the given criteria.

	Arguments:
		n (integer): the length of the password to generate, n >= 8.

	Returns:
		secure_password (string): a Secure password of length n.
	"""

	password = ""

	lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
				  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'	
					  'w', 'x', 'y', 'z']
					  
	upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
				  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
				  'W', 'X', 'Y', 'Z']
		
	digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	special_char_list = ["!", "-", "$", "%", "'", "(", ")", "*", "+", ",",
						 ".", "/", ":", ";", "<", "=", ">", "?", "_", "[", 
						 "]", "^", "`", "{", "|", "}", "~"]

	# Loops n number of times and choose a random character from
	# the four different groups of characters to ensure the password
	# is secure 
	for i in range(0, n):
		if i % 4 == 1:
			password += random.choice(lower_list)
		elif i % 4 == 2:
			password += random.choice(upper_list)
		elif i % 4 == 3:
			password += random.choice(digit_list)
		else:
			password += random.choice(special_char_list)

	return password


if __name__ == "__main__":
	pass