# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

# Решеине из интернета, для понимания

# names = ['str', 'int', 'bool', 'None', 'float', 'list', 'tuple', 'set']
# vals = ['abc', 24, True, None, 3.14, [1, 2, 3], (1, 2, 3), {1, 2, 3}]
#
# def form_dict(name_list, val_list):
#     res_dict = {}
#     for name, val in zip(name_list, val_list):
#         try:
#             res_dict[val] = name
#         except TypeError:
#             res_dict[str(val)] = name
#     return res_dict
#
#
# print(form_dict(names, vals))

values = input('Введите ключевые параметры в виде "значение"|"значение"|...: ').split('|')
res_dict = {}

for value in values:
    try:
        res_dict[int(value)] = int
        continue
    except:
        pass
    try:
        res_dict[float(value)] = float
        continue
    except:
        pass
    if value.replace(' ', '') == 'None':
        res_dict[value] = None
        continue
    if '[' and ']' in value:
        res_dict[value] = list
        continue
    if '{' and '}' in value:
        sym1 = value.find('{')
        sym2 = value.find('}')
        raw_set = value[sym1 + 1:sym2].replace(' ', '').split(',')
        if len(raw_set) == len(set(raw_set)):

            res_dict[value] = set
            continue
    if '(' and ')' in value:
        res_dict[value] = tuple
        continue
    if value == 'True' or value == 'False':
        res_dict[value] = bool
        continue
    else:
        res_dict[value] = type(value)

print(res_dict)
