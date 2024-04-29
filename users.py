import datetime

from dmenu import DynamicMenu, COLOR, COLOR_OFF, COLOR_YELLOW
from filedb import FileDB


class Account(DynamicMenu, FileDB):

    def preprint(*args, **kwargs):
        first_hash_founded = args[-1].find("#")
        last_hash_founded = args[-1].rfind("#")
        if first_hash_founded == -1:
            return args[-1]
        else:
            l_args = list(args)
            while first_hash_founded != 1 and last_hash_founded != 1:
                key = l_args[-1][first_hash_founded+1:last_hash_founded]
                match key:
                    case "time":

                        l_args[-1] = str(args[-1][:first_hash_founded+1]) \
                                   + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")\
                                   + str(args[-1][last_hash_founded:])
                    case _:
                        return args[-1]
                        # return args[len(args) - 1] + " "+id(self)+"AccountInfo"
                first_hash_founded = l_args[-1].find("#")
                last_hash_founded = l_args[-1].rfind("#")
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
                2: f'{COLOR["green"]}Замовлення (#1#){COLOR_OFF}\n'
                   f'\t{COLOR["cyan"]}готові(#2#)\n'
                   f'\t{COLOR_YELLOW}робимо(#3#)\n'
                   f'\t{COLOR["green"]}оплачені(#4#)\n'
                   f'\t{COLOR["red"]}відмінені(#5#)\n'
                   f'\t{COLOR_OFF}виконані(#6#)',
                #     f'{COLOR["green"]}готові',
                #     f'{COLOR_YELLOW}робимо',
                #     f'{COLOR["green"]}оплачені',
                #     f'{COLOR["red"]}відмінені',
                #     f'{COLOR["red"]}виконані',
                # ],
                3: f'{COLOR_YELLOW}Log_in (#7#) / Register (#8#){COLOR_OFF}',
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
        if "selected_item" in kwargs:
            selected_item = kwargs['selected_item']
            if selected_item:
                if kwargs['menu_id'] == int(0) and kwargs['menu_option'] == 'main_app_menu':
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
