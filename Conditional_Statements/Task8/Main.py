from Conditional_Statements.Task8.Good import Good
from Conditional_Statements.Task8.Shop import Shop

good1 = Good(1, 'штаны', 530)
good2 = Good(2, 'кофта', 420)
good3 = Good(3, 'рубашка', 230)

shop = Shop()
shop.add_good(good1)
shop.add_good(good2)
shop.add_good(good3)

shop.show_menu()
shop.selected_good_id = int(input("Введите номер товара: "))
shop.money = int(input("Введите сумму денег, которой вы располагаете:"))
shop.select_good(shop.selected_good_id, shop.money)
