"""task_1.py"""


class Pizza:
    """Класс Пиццерии"""

    def __init__(self, dough, sauce, toppings):
        """ Инициализация

        Args:
            dough (str): Тесто
            sauce (str): Соус
            toppings (_type_): Начинка
        """
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        """Подготовка"""
        print("Подготовка")

    def bake(self):
        """Запекание"""
        print("Запекание...")

    def cut(self):
        """Разрезание"""
        print("Разрез...")

    def box(self):
        """Упакование"""
        print("Упаковка...")


class PepperoniPizza(Pizza):
    """Класс пиццы Пепперони"""

    def __init__(self):
        """Инициализация"""
        super().__init__("Тонкое", "Томатный", ["Пепперони", "Сыр"])


class BBQPizza(Pizza):
    """Класс пиццы Барбекю"""

    def __init__(self):
        """Инициализация"""
        super().__init__("Тонкое", "Барбекю", ["Курица", "Лук", "Сыр"])


class SeafoodPizza(Pizza):
    """Класс пиццы SeaFood"""

    def __init__(self):
        """Инициализация"""
        super().__init__("Толстое", "Белый соус", [
            "Кревета", "Cheese"])


class Order:
    """Класс заказа"""

    def __init__(self):
        """Инициализация"""
        self.pizzas = []

    def add_pizza(self, pizza):
        """Добавление пиццы в список заказов

        Args:
            pizza (str): Пицца
        """
        self.pizzas.append(pizza)

    def calculate_total(self):
        """Расчет суммы заказа"""
        total = 0
        for pizza in self.pizzas:
            if isinstance(pizza, PepperoniPizza):
                total += 2500
            elif isinstance(pizza, BBQPizza):
                total += 1500
            elif isinstance(pizza, SeafoodPizza):
                total += 3000
        return total


class Terminal(Pizza):
    """Класс терминала"""

    def __init__(self):
        """Инициализация"""
        self.menu = {
            "1": PepperoniPizza(),
            "2": BBQPizza(),
            "3": SeafoodPizza()
        }
        self.current_order = None

    def display_menu(self):
        """отображение меню в терминале"""
        print("Добро пожаловать")
        print("Меню")
        print("1. Pepperoni Pizza (2500)")
        print("2. BBQ Pizza (1500)")
        print("3. Seafood Pizza (3000)")

    def take_order(self):
        """Взятие заказа"""
        self.display_menu()
        choice = input(
            "Пожалуйста выберите пиццу: ")
        pizza = self.menu.get(choice)
        if pizza:
            if not self.current_order:
                self.current_order = Order()
            self.current_order.add_pizza(pizza)
            print("Пицца добавлена")
        else:
            print("Неверный выбор, выберите пиццу")

    def confirm_order(self):
        """Подтверждение заказа"""
        if self.current_order:
            total_cost = self.current_order.calculate_total()
            print(f"Ваша сумма: {total_cost} тенге")
            confirmation = input(
                "Хотите подтвердить заказ? (Да/Нет): ")
            if confirmation.lower() == "Да".lower():
                self.current_order = None
                self.current_order = None
                Pizza.prepare(self)
                Pizza.bake(self)
                Pizza.cut(self)
                Pizza.box(self)
                print("Спасибо за заказ")

            else:
                print("Заказ отменен")
                self.current_order = None
        else:
            print("Заказ пуст")

    def main(self):
        """Основной метод"""
        while True:
            print("\nУслуги:")
            print("1. Взять заказ")
            print("2. Подтвердить заказ")
            print("3. Выход")
            choice = input("Выберите услугу: ")
            if choice == "1":
                self.take_order()
            elif choice == "2":
                self.confirm_order()
            elif choice == "3":
                print("Спасибо за выбор!")
                break
            else:
                print("Неверный ответ, выберите пиццу")


if __name__ == "__main__":
    terminal = Terminal()
    terminal.main()
