# declaration of a function:
# arguments without default values must be declared first, and then arguments with default values.
# use pass for an empty function
def this_is_a_function(argument1, argument2, argument3, argument_with_default_value = 10):
	""" Title of the doc string (this is PEP 484 type annotations).

	Args:
		argument1: Describe this argument here.
		argument2: Describe this argument here.

	Returns:
		Describe what is returned

	"""
	print('Some operations inside a function')
	return 'Return something'


# calling a function
# ordinary arguments (or positional arguments) are called: 'arg'
# key-word arguments are called: 'kwarg'
# args must be supplied first, and then kwargs
# args are first read in according to their positions, and then kwarg are read in
# if all arguments are supplied as key-word arguments, then order doesn't matter.

positional_argument1 = 1
positional_argument2 = 2
key_word_argument = 3
this_is_a_function(positional_argument1, positional_argument2, argument3 = key_word_argument)

# functions as input
# you can use expansion (*args or **kwargs) to pass the input of the passed function

def function_as_input(passed_function, arguments_for_passed_function):
	print(passed_function(*arguments_for_passed_function))

def summation(a, b):
	return a+b
def multiplication(a, b):
	return a*b

function_as_input(summation, (2, 3)) # this performs summation
function_as_input(multiplication, (2, 3)) # this performs multiplication
