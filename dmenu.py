COLOR = {
    'white': "\033[1;37m",
    'yellow': "\033[1;33m",
    'green': "\033[1;32m",
    'blue': "\033[1;34m",
    'cyan': "\033[1;36m",
    'red': "\033[1;31m",
    'magenta': "\033[1;35m",
    'black': "\033[1;30m",
    'darkwhite': "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen': "\033[0;32m",
    'darkblue': "\033[0;34m",
    'darkcyan': "\033[0;36m",
    'darkred': "\033[0;31m",
    'darkmagenta': "\033[0;35m",
    'darkblack': "\033[0;30m",
    'off': "\033[0;0m"
}
COLOR_YELLOW = "\033[1;33m"
COLOR_OFF = "\033[0;0m"


class DynamicMenu:
    """
    Клас для реалізації динамічного меню для будь яких класів, що наслідують цей клас.(<DynamicMenu>)
    Зручно перезавантажувати методи цього (Базового) класу у дочірніх класах що нослідують клас <DynamicMenu>, або
    виклику методу базового класу з екземпляром (self) ДОЧІРНЬОГО класу (напр.Project
    Наприклад.
    Метод по замовчуванню "def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd', *args, **kwargs):",
    який вкликається якщо жодних методів і додаткових параметрів не вказано або вказано невірно.

    Спрощений спосіб реалізації без додаткових параметрів та наслідування за посиланням нижче:
    https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
    class DynamicMenu():
        def method1(self):
            pass
        def method2(self):
            pass
        def method3(self):
            pass
        def get_method(self, method_name):
            method = getattr(self, method_name)
            return method()

    callbyname = DynamicMenu()
    method1 = callbyname.get_method(method_name)

    """

    def dynamic_menu_method_d(self, menu_id: int = 1, menu_option: str = 'd'):
        pass

    def dynamic_menu_method_0(self, menu_id: int = 1, menu_option: str = '0'):
        pass

    def dynamic_menu_method_1(self, menu_id: int = 1, menu_option: str = '1'):
        pass

    def dynamic_menu_method_2(self, menu_id: int = 1, menu_option: str = '2'):
        pass

    def dynamic_menu_method_3(self, menu_id: int = 1, menu_option: str = '3'):
        pass

    def dynamic_menu_method_4(self, menu_id: int = 1, menu_option: str = '4'):
        pass

    def dynamic_menu_method_5(self, menu_id: int = 1, menu_option: str = '5'):
        pass

    def dynamic_menu_method_6(self, menu_id: int = 1, menu_option: str = '6'):
        pass

    def dynamic_menu_method_7(self, menu_id: int = 1, menu_option: str = '7'):
        pass

    def dynamic_menu_method_8(self, menu_id: int = 1, menu_option: str = '8'):
        pass

    def dynamic_menu_method_9(self, menu_id: int = 1, menu_option: str = '9'):
        pass

    def dynamic_menu_method_10(self, menu_id: int = 1, menu_option: str = '10'):
        pass

    def loop_dmenu(self, menu_items, item):
        self.show_dmenu(menu_items, item)
        title_item = len([k for k, _ in menu_items.items() if k < 0])
        last_item = len([k for k, _ in menu_items.items() if k >= 0]) - title_item + 1
        try:
            print(f"{COLOR['darkblue']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
            selected_item = int(input("Зробіть свій вибір"))
            print(f"{COLOR['darkblue']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
            if 0 > selected_item > last_item:
                print(f"Ваш вибір за межами діапазону (0-{last_item}")
                return self.loop_dmenu(menu_items, item)
            else:
                if selected_item == last_item:
                    exit(selected_item)
                else:
                    print(f"{COLOR['darkgreen']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
                    method = getattr(self, 'dynamic_menu_option_' + str(selected_item))
                    method()
                    print(f"{COLOR['darkgreen']}{'-' * 5 * len(menu_items)}{COLOR_OFF}")
                    return self.loop_dmenu(menu_items, item)
        except Exception as e:
            print(f"Error - try again:{str(e)}")
            return self.loop_dmenu(menu_items, item)

    def show_dmenu(self, menu_items, item=0):
        """
        :param menu_items: dict of menu items
        :param item: integer
        :return: shows dynamic menu inside loop_dmenu() method
        """
        if item == -1:
            clear()
        title_item = len([k for k, _ in menu_items.items() if k < 0])
        last_item = len([k for k, _ in menu_items.items() if k >= 0]) - title_item + 1
        if item <= len(menu_items):
            if item == last_item:
                print(f"{COLOR_YELLOW}{last_item}: {COLOR['red']} Вихід{COLOR_OFF}")
                pass
            else:
                if item < 0:
                    print(f"{menu_items[item]}")
                else:
                    print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} {menu_items[item]}")
                if item < last_item:
                    return self.show_dmenu(menu_items, item + 1)
                else:
                    pass

    def dynamic_menu_method(self, menu_id: int = 1, menu_option: str = 'd'):
        if menu_id == int(0) and menu_option == 'main_linkedlist_menu':
            m_items = {
                -1: f"Тип об'єкту: {self.__class__.__CLASS__} {type(self)}",
                # 0: 'Виконувати в 1 одно-звязному списку( 1(head)->2->None(next))'
                0: f'{COLOR["cyan"]}Перемкнути на 2 дво-звязний список None(prev)<-1(head)<->(prev)2(next)<->3(tail)->None(next){COLOR["blue"]}',
                1: f'{COLOR["green"]}Додати нове число до списку{COLOR_OFF}',
                # (якщо таке число існує у списку, потрібно вивести повідомлення про
                # це користувачеві без додавання числа).
                2: f'{COLOR['red']}Видалити усi входження числа зi списку{COLOR_OFF}',
                # (користувач вводить з клавiатyри число для видалення).
                3: f'{COLOR["blue"]}Показати вмiст списку{COLOR_OFF}',
                # (залежно вiд выборy користyвача, показать список з початкy або з кiнця)
                4: f'{COLOR["blue"]}Перевiрити, чи є значення y спискy.{COLOR_OFF}',
                5: f'{COLOR_YELLOW}Замiнити значення y спискy{COLOR_OFF}',
                # (користyвач вызначає, чи замiнити тільки перше входження, чи всі).
            }
            self.loop_dmenu(m_items, -1)  # self.show_dmenu(m_items, -1)
            return

    def get_method(self, *args, **kwargs):
        method_name = 'dynamic_menu_method_d'  # (self, menu_id: int = 1, menu_option: str = 'd')
        args = args or []
        if len(args) > 0:
            method_name = list(args).pop()
        kwargs = kwargs or {}
        # якщо не передали жодних параметрів
        method_params = kwargs or {
            'menu_id': 0,
            'menu_option': 'main_app_menu'
        }
        if 'method_params' in kwargs:
            pass
        method = getattr(self, method_name)
        return method(**method_params)  # method(self)
