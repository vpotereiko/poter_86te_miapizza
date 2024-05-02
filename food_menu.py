from dmenu import DynamicMenu, COLOR, COLOR_OFF, COLOR_YELLOW
from filedb import FileDB


###from users import User


class MenuItem(DynamicMenu, FileDB):
    _items = []

    @staticmethod
    def preprint(m_value):
        from users import Account
        # додаткова обробка якщо э список
        if isinstance(m_value,list):
            m_value = ''.join(m_value)
        return Account.preprint(m_value)  # заглушка
    #
    # def __new__(cls, *args, **kwargs):
    #     # from users import User
    #     # if not cls._items.index(kwargs.get('instance', User())):
    #     #     cls._items.append(kwargs.get('instance', User()))
    #     return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        # from users import User
        self.creator = self._items[-1]
        self.menu_item_name = kwargs.get('menu_item_name', "Перша страва")
        self.menu_item_desc = kwargs.get('menu_desc_name', "інгредієнти в страві")
        # super().__init__(self, *args, **kwargs)

    def food_menu(self, *args, **kwargs):
        if kwargs['menu_id'] == int(1) and kwargs['menu_option'] == 'food_menu':
            m_items = {
                -1: f"Тип об'єкту: {self.__class__.__name__}(DEBUG)",
                0: f'{COLOR["darkblue"]}Вітаємо в кафе "La mia pizza - PRONTA! (#time#)"{COLOR_OFF}\n'
                   f'\t{COLOR["yellow"]}Наше меню:{COLOR_OFF}',
                1: f'{COLOR["green"]}Додати нову страву{COLOR_OFF}',
                2: f'{COLOR["yellow"]}Приховати страву (#1#){COLOR_OFF}',
                3: f'{COLOR["red"]}Відновити приховану страву (#2#){COLOR_OFF}\n'
                   f'{COLOR["green"]*100} ',
                #     f'{COLOR_YELLOW}робимо',
                #     f'{COLOR["green"]}оплачені',
                #     f'{COLOR["red"]}відмінені',
                #     f'{COLOR["red"]}виконані',
                # ],
            }
        self.loop_dmenu(m_items, -1, **kwargs)  # self.show_dmenu(m_items, -1)
        return

        # menu_id = 3, menu_option = 5

    def save_new_item(self, *args, **kwargs):
        new_item_obj = MenuItem(str(kwargs['input_items']['new_item_name']),str(kwargs['input_items']['new_item_desc']))
        _input_items = {
            'new_item_name': new_item_obj.menu_item_name,
            'new_item_desc': new_item_obj.menu_item_desc,
        }
        m_items = {
            -1: f"Тип об'єкту: {self.__class__.__name__}(DEBUG)",
            0: f'{COLOR["darkblue"]}Вітаємо в кафе "La mia pizza - PRONTA! (#time#)"{COLOR_OFF}\n'
               f"{COLOR_YELLOW}Збереження нової страви:{COLOR_OFF}",
            1: [
                f"{COLOR_YELLOW}Назва страви:{COLOR['blue']}",
                kwargs['input_items']['new_item_name'],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],
            # 2: f"{COLOR_YELLOW}Опис проекту:{COLOR['blue']}{kwargs.get('new_proj_desc', '')}{COLOR['green']}(
            # змінити){COLOR_OFF}",
            2: [
                f"{COLOR_YELLOW}Опис інгрердієнтів:{COLOR['blue']}",
                kwargs['input_items']['new_item_desc'],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],
            3: f"{COLOR['blue']}Додати нову страву{COLOR_OFF}",
        }
        # input_items = kwargs.get('input_items', _input_items)
        # selected_item = kwargs.get('selected_item', None)
        # list_items = kwargs.get('list_items', None)
        # first_item = kwargs.get('first_item', 1)
        # last_item = kwargs.get('last_item', 5)
        # # ###############################################
        # # # m_items = m_items,\
        # # # item = 0,\
        # # # first_item = 1,\
        # # # last_item = 6,
        # # # menu_id = 3,\
        # # # menu_option = 'proj_new_create',
        # # # input_items = _input_items,
        # # # list_items = new_proj_obj._task_items)
        # self.loop_dmenu(m_items, -1)  # self.show_dmenu(m_items, -1)
        self.loop_dmenu(new_item_obj, m_items=m_items, item=0, first_item=1, last_item=4,
                        menu_id=3, menu_option='item_new_create',
                        # new_proj_name=_input_items["new_proj_name"],
                        # new_proj_desc=_input_items['new_proj_desc'],
                        input_items=_input_items)
        return

    def add_new_food(self, *args, **kwargs):
        _input_items = {
            'new_item_name': '',
            'new_item_desc': '',
        }
        new_item_obj = MenuItem(_input_items['new_item_name'], _input_items['new_item_desc'])
        print(f"{COLOR_YELLOW}Створення нової страви:{COLOR_OFF}")
        print(f"{COLOR_YELLOW} 1: Назва страви:{COLOR['blue']}")
        _input_items["new_item_name"] = input('>')
        print(f"{COLOR_YELLOW} 2: Опис інгрердієнтів:{COLOR['blue']}")
        _input_items['new_item_desc'] = input('>')
        #
        m_items = {
            -1: f"Тип об'єкту: {self.__class__.__name__}(DEBUG)",
            0: f'{COLOR["darkblue"]}Вітаємо в кафе "La mia pizza - PRONTA! (#time#)"{COLOR_OFF}'
               f"{COLOR_YELLOW}Створення нової страви:{COLOR_OFF}",
            1: [
                f"{COLOR_YELLOW}Назва страви:{COLOR['blue']}",
                _input_items["new_item_name"],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],
            # 2: f"{COLOR_YELLOW}Опис проекту:{COLOR['blue']}{kwargs.get('new_proj_desc', '')}{COLOR['green']}(
            # змінити){COLOR_OFF}",
            2: [
                f"{COLOR_YELLOW}Опис інгрердієнтів:{COLOR['blue']}",
                _input_items['new_item_desc'],
                f"{COLOR['green']}(змінити){COLOR_OFF}",
            ],
            3: f"{COLOR['green']}Зберегти страву {COLOR_OFF}",
        }
        self.loop_dmenu(new_item_obj, m_items=m_items, item=-1, first_item=1, last_item=4,
                        menu_id=2, menu_option='item_new_create',
                        new_item_name=_input_items["new_item_name"],
                        new_item_desc=_input_items['new_item_desc'],
                        input_items=_input_items)

    def dynamic_menu_option_1(self, *args, **kwargs):
        self.add_new_food(self, *args, **kwargs)

    def dynamic_menu_option_3(self, *args, **kwargs):
        self.save_new_item(self, *args, **kwargs)

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
                            self.add_new_food()
                        case 2:
                            pass  # remove active
                        case 3:
                            pass  # hide active
                        case 4:
                            pass  # m_atems (act/hiden)
                elif kwargs['menu_id'] == int(2) and kwargs['menu_option'] == 'food_menu':
                    match selected_item:
                        case 1:
                            self.add_new_food()
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
        return method(*args, **method_params)
