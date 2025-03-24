# list a numbers
numbers = [1,2,3]
print(numbers)

# list different types
my_list = [1, "hello", 2.3, "hi"]
print(my_list)

# access python list with index
languages = ["javascript", "python", "c#", "web"]
print(languages)
print(languages[1])
print(languages[3])

# slicing of python list
language= ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i']
print(language)
print(language[2:5])
print(language[5:])
print(language[:])
print(language[-3])

# add elements to list
number = [23,45,65,23,22]
print("before append :",number)
number.append(56)
print("after append:", number)

# using indexing

prime_number = [2,3,5]
print("list1:" , prime_number)

even_number = [4,6,5]
print("list2:", even_number)
prime_number.extend(even_number)
print("list after append:", prime_number)

# change list number
lang = ['python', 'swift', 'c++']
lang[2] = 'c#'
print(lang)

# remove an item from a list
langua = ['javascript', 'java', 'c#', 'swift', 'c']
del langua[1]
print(langua)

del langua[-1]
print(langua)
del langua[0 : 2]
print(langua)

# using remove
lan = ['java', 'python', 'css']
lan.remove('java')
print(lan)