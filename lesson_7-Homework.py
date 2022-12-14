# 1. Условие: Дано целое число (int). Определить сколько нулей в этом числе.
number = 2312056100

total_zeros = str(number).count("0")

# 2. Условие: Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например, для числа 1002000 - три нуля
number = 2312056100
str_number = str(number)

total_zeros_in_the_end = len(str_number) - len(str(int(str_number[::-1])))

# 3. Условие: Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = [1, 2, "3", "Python", 3.9]
my_list_2 = ["8", "YES", False, "Django"]

# С первого списка [1, "3"], со второго - ["8", False], так как нужно сделать выборку по местам (1, 2, 3) элементов,
# а не их индексам (0, 1, 2).
my_result = my_list_1[1::2] + my_list_2[::2]

# 4. Условие: Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = ["Python", "-", "самый", "удобный", "инструмент"]

new_list = my_list[1:] + [my_list[0]]

# 5. Условие: Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
my_list = ["Python", "-", "самый", "удобный", "инструмент"]

my_list += [my_list.pop(0)]

# 6. Условие: Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
string = "43 больше чем 34 но меньше чем 56"
lst = string.split()

total_num = sum([int(i) for i in lst if i.isdigit()])

# 7. Условие: Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)
my_str = "Не живи одним днём. Строй своё будущее!"
l_limit = "е"
r_limit = " "

sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]

# 8. Условие: Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = "Сделай сегодня для лучшего завтра"

if len(my_str) % 2 != 0:
    my_str += "_"
lst = [my_str[i] + my_str[i+1] for i in range(0, len(my_str)-1, 2)]

# 9. Условие: Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
numbers = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0

for index, num in enumerate(numbers[1:-1]):
    sum_lnum_and_rnum = numbers[index] + numbers[index + 2]
    if num > sum_lnum_and_rnum:
        counter += 1

print(counter)

# 10. Условие: Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
my_list = ["Igor", 9, "Python", "community", 102]

new_list = [item for item in my_list if type(item) == str]

# 11. Условие: Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_str = "Сегодня был продуктивный день."

lst = [char for char in set(my_str) if my_str.count(char) == 1]

# 12. Условие: Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
str1 = "Сегодня был продуктивный день."
str2 = "Надеюсь завтра будет ещё продуктивней."
my_lst = [char for char in set(str1) if char in str2]

my_lst = list(set(str1).intersection(set(str2)))

# 13. Условие: Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
str1 = "Сегодня был продуктивный день."
str2 = "Надеюсь завтра будет ещё продуктивней."

new_lst = [char for char in set(str1) if str1.count(char) == str2.count(char) == 1]