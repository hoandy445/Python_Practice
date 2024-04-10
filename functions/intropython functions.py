### NOTES ###
# def hello_name(name):
#     print(f"Hello, {name.title()}.")

# names = ['john','kate','mary']

# for name in names: # basic function usage
#     hello_name(name)

# hello_name() # TypeError without argument
    
# def hello_name2(name = 'everyone'): # set default value in the case there is no argument
#     print(f'Hello, {name.title()}.')

# for name in names:
#     hello_name2() # function runs without breaking


### EXERCISES 1 ###
# import random

# def game_opinion(game = 'video games'):
#     opinion = ['like','hate']
#     print(f'I {random.choice(opinion)} playing {game}!')

# games = ['Tetris','Mario','Sonic', None]

# for game in games:
#     if game is None:
#         game_opinion()
#     else:
#         game_opinion(game)


### NOTES ###

# personal_info = {
# 'John Smith':{'First name':'John','Last name':'Smith','Age':30},
# 'Mary Kate':{'First name':'Mary','Last name':'Kate','Age':25},
# 'Patrick Star':{'First name':'Patrick','Last name':'Star'}
# }

# def describe_person(first_name,last_name,age = 'N/A'):
#     print('First name:',first_name)
#     print('Last name: ',last_name)
#     print('Age: ',age)

# for person,info in personal_info.items():
#     first_name = info['First name']
#     last_name = info['Last name']
#     if not 'Age' in info:
#         describe_person(first_name,last_name)
#     else:
#         age = info['Age']
#         describe_person(first_name,last_name,age)


# def describe_person(first_name,last_name,age):
#     print('First name:',first_name)
#     print('Last name: ',last_name)
#     print('Age: ',age)

# positional arguments can be rearranged by using assignments statements with the keywords in the calling statement
# describe_person(last_name = "Smith",age = 24,first_name="John")

# def describe_person(first_name,last_name,age=None, blood_type=None,favorite_food=None):
#     print('First name:',first_name)
#     print('Last name: ',last_name)
#     if age:
#         print('Age: ',age)
#     if blood_type:
#         print('Blood type: ',blood_type)
#     if favorite_food:
#         print('Favorite food: ',favorite_food)
#     print('\n')

# describe_person("John","Smith",blood_type='O')
# describe_person("Mary","Kate", age = 21,favorite_food='Bananas')

### EXERCISE ###

# def country_language(country,language):
#     print('Country: ',country)
#     print('Language: ', language)
#     print('\n')

# country_language('Japan','日本語')
# country_language(language='English',country='USA')
# country_language(country='Mexico',language='Spanish')

# arbitrary number of arguments can be done by putting an asterisk in front of an argument. this stores all values for that argument in a tuple
# def multiply_numbers(value1,value2,*values):
#     result = value1 * value2
#     x = None
#     for value in values:
#         result = result * value
#     return result

# print(multiply_numbers(1,2,3,4))

# def multiply_numbers(value1,*values):
#     all_values = []
#     for value in values:
#         all_values.append(value)

#     result = value1
#     for i in all_values:
#         result = result * i
#     return result

# print(multiply_numbers(1,2,3,4,5,6,7,8,9,10))


# arbitrary number of keyword arguments can be used by putting two asterisks in front of an argument. this stores the values in key-value pairs in a dictionary
def store_random_info(**kwargs):
    for key,value in kwargs.items():
        key = key.title().replace('_',' ')
        print(f'{key}: {value}')

store_random_info(name = 'Andy', blood_type = 'O', age = 24)