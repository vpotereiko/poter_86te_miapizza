import datetime

from dmenu import DynamicMenu, COLOR, COLOR_OFF, COLOR_YELLOW
from filedb import FileDB
from food_menu import MenuItem


def insert_curr_time(part1, part2):
    return f"{part1}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{part2}"


def insert_login_registered(part1, part2, part3):
    return f"{part1}{datetime.datetime.now().strftime('%Y-%m-%d')}{part2}{datetime.datetime.now().strftime('%H:%M:%S')}{part3}"


def get_orders_key():
    return f'1#){COLOR_OFF}\n\t{COLOR["cyan"]}готові(#2#)\n\t{COLOR_YELLOW}робимо(#3#)\n\t{COLOR["green"]}оплачені(#4#)\n\t{COLOR["red"]}відмінені(#5#)\n\t{COLOR_OFF}виконані(#6'


class Account(DynamicMenu, FileDB):
    _
    @staticmethod
    def preprint(m_value):
        first_hash_founded = m_value.find("#")
        last_hash_founded = m_value.rfind("#")
        if first_hash_founded == -1:
            return m_value
        else:
            new_m_value = ''
            new_m_value = str(''.join(m_value))
            while first_hash_founded != 1 or last_hash_founded != 1:
                key = new_m_value[first_hash_founded + 1:last_hash_founded]
                match key:
                    case "time":
                        l_value = insert_curr_time(new_m_value[:first_hash_founded],
                                                   new_m_value[last_hash_founded + 1:])
                        new_m_value = str(''.join(l_value))
                    case "0":
                        l_value = insert_login_registered(new_m_value[:first_hash_founded],
                                                          'кіл-ть активних блюд',
                                                          new_m_value[last_hash_founded + 1:])
                        new_m_value = str(''.join(l_value))
                    case "7#) / Register (#8":  # 2 параметри одночасно
                        first_hash_founded = new_m_value.find("#")
                        last_hash_founded = new_m_value.rfind("#")
                        l_value = insert_login_registered(new_m_value[:first_hash_founded],
                                                          ') / Register (',
                                                          new_m_value[last_hash_founded + 1:])
                        new_m_value = str(''.join(l_value))
                    case "9":
                        l_value = insert_login_registered(new_m_value[:first_hash_founded],
                                                          'кіл-ть перезапусків меню',
                                                          new_m_value[last_hash_founded + 1:])
                        new_m_value = str(''.join(l_value))
                    case _:
                        if key.count('#') == 10:  # всі замовлення
                            l_keys = key.split('#')
                            new_m_value = [new_m_value[:first_hash_founded], ]
                            l_value = ''
                            for i, kk in enumerate(l_keys):
                                match kk:
                                    case "1":
                                        new_m_value.append(kk)
                                    case "2":
                                        new_m_value.append(kk)
                                    case "3":
                                        new_m_value.append(kk)
                                    case "4":
                                        new_m_value.append(kk)
                                    case "5":
                                        new_m_value.append(kk)
                                    case "6":
                                        new_m_value.append(kk)
                                        new_m_value.append(m_value[last_hash_founded + 1:])
                                    case _:
                                        new_m_value.append(kk)
                            return ''.join(new_m_value)
                        else:
                            return new_m_value
                first_hash_founded = new_m_value.find("#")
                last_hash_founded = new_m_value.rfind("#")
                #
            return l_args[-1]


class Customer(Account):
    pass


class User(Customer):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def mia_pizza_pronta(self, *args, **kwargs):
        if kwargs['menu_id'] == int(0) and kwargs['menu_option'] == 'main_app_menu':
            m_items = {
                -1: f"Тип об'єкту: {self.__class__.__name__}(DEBUG)",
                0: f'{COLOR["darkblue"]}Вітаємо в кафе "La mia pizza - PRONTA! (#time#)"{COLOR_OFF}',
                1: f'{COLOR["yellow"]}Наші страви{COLOR_OFF}'
                   f'{COLOR["green"]}(#0#){COLOR_OFF}',
                2: f'{COLOR["green"]}Замовлення (#1#){COLOR_OFF}'
                   f'\t{COLOR["green"]}нові(#2#)'
                   f'\t{COLOR["red"]}відмінені(#3#)'
                   f'\t{COLOR_YELLOW}робимо(#4#)'
                   f'\t{COLOR["green"]}оплачені(#5#)'
                   f'\t{COLOR_OFF}виконані(#6#)',
                #     f'{COLOR["green"]}готові',
                #     f'{COLOR_YELLOW}робимо',
                #     f'{COLOR["green"]}оплачені',
                #     f'{COLOR["red"]}відмінені',
                #     f'{COLOR["red"]}виконані',
                # ],
                3: f'{COLOR_YELLOW}Log_in (#7#) / Register (#8#){COLOR_OFF}',
            }
            self.loop_dmenu(m_items, -1, p1="add_new_food")  # self.show_dmenu(m_items, -1)
            return

    def dynamic_menu_option_1(self, *args, **kwargs):
        from food_menu import MenuItem
        m = MenuItem(instance=self, menu_item_name="Акційна страва")  # .get_method()
        m.get_method('food_menu', menu_id=1, menu_option="food_menu")

    def get_method(self, *args, **kwargs):
        method_name = 'mia_pizza_pronta'
        args = args or []
        if len(args) > 0:
            method_name = list(args).pop()
        kwargs = kwargs or {}
        # якщо не передали жодних параметрів
        if "selected_item" in kwargs:
            selected_item = kwargs['selected_item']
            if selected_item:
                if kwargs['menu_id'] == int(0) and kwargs['menu_option'] == 'main_app_menu':
                    match selected_item:
                        case 1:
                            self.show_user_food_menu()
                        case 2:
                            pass
                        case 3:
                            pass
                elif kwargs['menu_id'] == int(1) and kwargs['menu_option'] == 'food_menu':
                    match selected_item:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
        method_params = kwargs or {
            'menu_id': 0,
            'menu_option': 'main_app_menu'
        }
        if 'method_params' in kwargs:
            pass
        method = getattr(self, method_name)
        return method(**method_params)
