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


class Scheduled:
    """
    https://pravash-techie.medium.com/python-sched-for-automating-tasks-in-python-396618864658
    """
    pass


class DynamicMenu(Scheduled):
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

    def dynamic_menu_method_0(self, menu_id: int = 1, menu_option: str = '0'):
        pass

    def dynamic_menu_method_1(self, menu_id: int = 0, menu_option: str = '1'):
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
        # if item == -1:
        #     clear()
        title_item = len([k for k, _ in menu_items.items() if k < 0])
        if title_item == 0:
            if item < 0:
                item += 1
        last_item = len([k for k, _ in menu_items.items() if k >= 0])
        if item <= len(menu_items):
            if item == last_item:
                print(f"{COLOR_YELLOW}{last_item}: {COLOR['red']} Вихід з програми {self.preprint('(#9#)')}{COLOR_OFF}")
                pass
            else:
                curr_item = self.preprint(menu_items[item])
                if item <= 0:
                    print()
                    print(f"{self.preprint(menu_items[item])}")
                else:
                    print(f"{COLOR_YELLOW}{item}: {COLOR_OFF} "
                          f"{self.preprint(menu_items[item])}")
                if item < last_item:
                    return self.show_dmenu(menu_items, item + 1)
                else:
                    pass

    def mia_pizza_pronta(self, *args, **kwargs):
        if kwargs['menu_id'] == int(0) and kwargs['menu_option'] == 'main_app_menu':
            m_items = {
                -1: f"Тип об'єкту: {self.__class__.__name__}",
                0: f'{COLOR["cyan"]}Кафе "La mia pizza - PRONTA!"{COLOR_OFF}',
                1: f'{COLOR["green"]}Наше меню{COLOR_OFF}',
                2: f'{COLOR["green"]}Ваші замовлення / Зробити замовлення{COLOR_OFF}',
                3: f'{COLOR["green"]}готові(_)\n'
                   f'{COLOR_YELLOW}робимо(_)\n'
                   f'{COLOR["green"]}оплачені(_)\n'
                   f'{COLOR["red"]}відмінені(_)\n'
                   f'{COLOR["red"]}виконані(_)\n',
                #     f'{COLOR["green"]}готові',
                #     f'{COLOR_YELLOW}робимо',
                #     f'{COLOR["green"]}оплачені',
                #     f'{COLOR["red"]}відмінені',
                #     f'{COLOR["red"]}виконані',
                # ],
                4: f'{COLOR_YELLOW}Log_in / Register{COLOR_OFF}',
            }
            self.loop_dmenu(m_items, -1)  # self.show_dmenu(m_items, -1)
            return

    def get_method(self, *args, **kwargs):
        method_name = 'mia_pizza_pronta'
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
        return method(**method_params)
