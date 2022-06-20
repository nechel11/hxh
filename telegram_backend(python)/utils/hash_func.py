import math
import string

def hash_func(st : string):
	res_string = ""
	for character in st:
		ascii_value = ord(character)
		tmp = math.isqrt(ascii_value)
		res_string += str(tmp)
	return res_string