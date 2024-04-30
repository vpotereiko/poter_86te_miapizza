from dmenu import DynamicMenu, COLOR, COLOR_OFF, COLOR_YELLOW
from filedb import FileDB


class MenuItem(DynamicMenu, FileDB):
    _items = []

    def food_menu(self, *args, **kwargs):
        if kwargs['menu_id'] == int(1) and kwargs['menu_option'] == 'food_menu':
            m_items = {
                -1: f"Тип об'єкту: {self.__class__.__name__}(DEBUG)",
                0: f'{COLOR["darkblue"]}Вітаємо в кафе "La mia pizza - PRONTA! (#time#)"{COLOR_OFF}\n'
                    f'\t{COLOR["yellow"]}Наше меню:{COLOR_OFF}',
                1: f'{COLOR["yellow"]}Додати нову страву{COLOR_OFF}',
                2: f'{COLOR["red"]}Приховати страву (#1#){COLOR_OFF}',
                3: f'{COLOR["red"]}Відновити приховану страву (#2#){COLOR_OFF}',
                #     f'{COLOR["green"]}готові',
                #     f'{COLOR_YELLOW}робимо',
                #     f'{COLOR["green"]}оплачені',
                #     f'{COLOR["red"]}відмінені',
                #     f'{COLOR["red"]}виконані',
                # ],
                }
        self.loop_dmenu(m_items, -1)  # self.show_dmenu(m_items, -1)
        return

    def get_method(self, *args, **kwargs):
        method_name = 'food_menu'
        args = args or []
        if len(args) > 0:
            method_name = list(args).pop()
        kwargs = kwargs or {}
        # якщо не передали жодних параметрів
        if "selected_item" in kwargs:
            selected_item = kwargs['selected_item']
            if selected_item:
                if kwargs['menu_id'] == int(1) and kwargs['menu_option'] == 'food_menu':
                    match selected_item:
                        case 1:
                            pass  # add new
                        case 2:
                            pass  # remove active
                        case 3:
                            pass  # hide active
                        case 4:
                            pass  # m_atems (act/hiden)
        method_params = kwargs or {
            'menu_id': 1,
            'menu_option': 'food_menu'
        }
        if 'method_params' in kwargs:
            pass
        method = getattr(self, method_name)
        return method(**method_params)

