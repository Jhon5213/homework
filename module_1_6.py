#Работа со словарями:

my_dict = {'Evgeniy':1994, 'Alex': 1991, 'Misha': 1995}
print(my_dict)
print(my_dict['Evgeniy'])
print(my_dict.get('Igor'))
my_dict = {'Evgeniy':1994, 'Alex': 1991, 'Misha': 1995,'Mashs': 1999, 'Oleg': 1997}
a = my_dict.pop('Alex')
print(a)
print(my_dict)

# Работа с множествами:

my_set = {11, 22, 3, 44, 11, 22, 3, 44,  'Число', 'Число', True}
print(my_set)
my_set.update({12}, (0,123))
print(my_set)
list_ = [11, 22, 3, 44, 11, 22, 3, 44,  'Число', 'Число', True]
list_ = set(list_)
print(list_)
print(list_.remove(1))
print(list_)