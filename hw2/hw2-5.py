set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

set1_2 = set1.union(set2)
final_set = set1_2.union(set3)
not_in_sets = list(final_set - (set1 | set2 | set3))

print("Элементы, которые не вошли в множества:", not_in_sets)
print("Разница всех элементов множества и списка:", final_set.difference(set(not_in_sets)))
