from shopping_list import ShoppingList

# Создание объекта класса ShoppingList
my_shopping_list = ShoppingList()

# Добавление предметов в список
my_shopping_list.add_item('Хлеб', 2)
my_shopping_list.add_item('Молоко')
my_shopping_list.add_item('Яйца', 10)

# Просмотр текущего списка
print("\nТекущий список:")
my_shopping_list.view_list()

# Удаление молока из списка
my_shopping_list.remove_item('Молоко')

# Просмотр измененного списка
print("\nИзменённый список после удаления 'Молока':")
my_shopping_list.view_list()

# Изменение количества яиц
my_shopping_list.edit_quantity('Яйца', 7)

# Просмотр окончательного списка
print("\nОкончательный список после изменения количества яиц:")
my_shopping_list.view_list()