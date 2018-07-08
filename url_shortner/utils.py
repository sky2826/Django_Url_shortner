import random
import string


def gen_6_digit_random_code(instance):
	allchar = string.ascii_letters  + string.digits
	code = "".join([random.choice(allchar) for i in range(6)])
	klass = instance.__class__
	if klass.objects.filter(code=code).exists():
		code=gen_6_digit_random_code(instance)
	return code 