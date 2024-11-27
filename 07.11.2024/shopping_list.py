class ShoppingList:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, quantity=1):
        if item in self.items:
            print(f"Предмет '{item}' уже присутствует в списке.")
        else:
            self.items[item] = quantity
            print(f"Предмет '{item}' добавлен в список.")
        
    def remove_item(self, item):
        if item not in self.items:
            print(f"Предмета '{item}' нет в списке.")
        else:
            del self.items[item]
            print(f"Предмет '{item}' удален из списка.")
            
    def edit_quantity(self, item, new_quantity):
        if item not in self.items:
            print(f"Предмета '{item}' нет в списке.")
        else:
            self.items[item] = new_quantity
            print(f"Количество предмета '{item}' обновлено до {new_quantity}.")
    
    def view_list(self):
        if len(self.items) == 0:
            print("Список покупок пуст.")
        else:
            for key, value in self.items.items():
                print(f"{key} - {value}")