# variables

a_str = "This is an example of a string in quotes" # In python the word string is abbreviated to str
my_float = 5.5
an_integer = 5 # integer is abbreviated to int
shopping_list = ["apples", "oranges", "pears"]
a_dict = {"userId": "JBloggs"} # dictionary is abbreviated to dict
my_var = another_variable # variable is abbreviated to var
test_function = my_function() #function is abbreviated to func
example_tuple = ("apple", "orange", "pear")
boolean_values = True # boolean is abbreviated to bool

>>>first_name = "Monty"
>>>last_name = "Python"
# concatenate
>>>print(first_name+last_name)
MontyPython

# add space
>>>print(first_name + " " + last_name)
Monty Python

# .format()
>>>first_name = "John"
>>>surname = "Doe"
>>>print("My first name is {}. My family name is {}".format(first_name, surname))

# f-strings
firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")

#int variables in strings
my_int = 50
sentence = "The total comes to: "

print(sentence + my_int)
# convert int to str
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

# create dict
>>> user = {"first_name":"Ada"}
>>> print(user)
{'first_name': 'Ada'}

# read the value
>>> user = {"first_name":"Ada"}
>>> print(user["first_name"])
Ada

# update a key-value
>>>user["family_name"] = "Byron"
>>>print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}

# modify a value
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

# delete key-value pair
>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}

# read lists
>>>fruit = ["apples","oranges","bananas"]
>>>print(fruit[1])
oranges

# length of list
>>>len(fruit)
3

# negative index to return last value
>>>print(fruit[-1])
bananas
>>>print(fruit[-2])
oranges

# append list
>>> fruit.append("kiwi")
>>> print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']

# insert using index value
>>> fruit.insert(2, "passion fruit")
>>> print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

# sorted in original order
>>>print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
>>>print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

# to permanently sort
>>> fruit.sort()
>>> print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

# to reverse
>>>fruit.reverse()
>>> print(fruit)
['passion fruit', 'oranges', 'kiwi', 'bananas', 'apples']

# delete using index position
>>> del fruit[1]
>>> print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']

# to use value after removing it
>>>favorite_fruit = fruit.pop()
>>>print(favorite_fruit)
apples
# another example using index
>>> fresh_fruit = fruit.pop(1)
>>> print(fresh_fruit)
kiwi

# use remove and specify value
>>> fruit.remove('bananas')
>>> print(fruit)
['passion fruit']

# determining type
>>>my_variable = "A string"
>>>print(type(my_variable))
# should return: 
<class 'str'>

# example of a TypeError
>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
# fix
>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + str(my_number))
The number is 50




