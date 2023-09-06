# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_dubl(my_list):
    uniq_list = set()
    recurring_list = set()

    for i in my_list:
        if i in uniq_list:
            recurring_list.add(i)
        else:
            uniq_list.add(i)

    return list(recurring_list)


my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 7, 8, 9, 8]
result = find_dubl(my_list)
print(result)



