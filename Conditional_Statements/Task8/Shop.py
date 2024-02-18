class Shop:

    def __init__(self):
        self.goods = []

    def add_good(self, good):
        self.goods.append(good)

    def show_menu(self):
        print("Выберите товар:")
        for good in self.goods:
            print(f"{good.id}. {good.name} - Цена: {good.price}")

    def select_good(self, selected_good_id, money):
        for good in self.goods:
            if int(good.id) == selected_good_id:
                if money < good.price:
                    print("Денег не хватает!")
                    break
                elif money == good.price:
                    print("Спасибо за покупку!")
                else:
                    change = money - good.price
                    print(f"Ваша сдача: {change}")
        if selected_good_id > len(self.goods):
            print("Товар не найден в магазине.")
