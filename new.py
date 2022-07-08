my_list=[42,43]
my_dict={
    'foo':{
        'a':12,
        'b':(1,2,3,4,my_list)
    },
    'bar':
        {
        'c':12,
        'd':{5,6,7,8}
        },
    'moo':{
        'e':12,
        'f':{'Lol':['L','o','l']}
    },
}
# 4  Снова вывести на консоль значение ключа 'b'
# print(my_dict['foo']['b'])

# 5  Вывести множество
# print(my_dict)

# 6  Добавить во множество элемент 9
# my_dict.setdefault(9)
# print(my_dict)
# 8  Удалите из списка элемент 'o'
# my_dict['moo']={
#         'e':12,
#         'f':{'Lol':['L','l']}}
# print(my_dict)


# 9  Добавить в словарь,который явл значением ключа 'f' ключ 'K' со значением ['K', 'e', 'k']

# my_dict['moo']={
#          'e':12,
#        'f':{'Lol':['L','l'], 'k':['k','e','k'}}
# print(my_dict)
# my_dict['moo']['f']['Lol']={'L','l'},{'k':['k','e','k']}
# print(my_dict)
# 10 Очистить словарь my_dict
# my_dict.clear()
# print(my_dict)
