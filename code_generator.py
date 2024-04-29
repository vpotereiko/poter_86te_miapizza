from datetime import datetime


class CodeGenerator:
    __counter = 0
    __items = []

    # @property
    # def valid_keys(self):
    #     keys = []
    #     for key in os.listdir(FILES_PATH):
    #         keys.append(key)
    #     return keys
    #
    # @staticmethod
    # def generate_new_key():
    #     dt = datetime.now()
    #     ts = datetime.timestamp(dt)
    #     return str(int(ts))  # string.digits
    #
    # @staticmethod
    # def get_date_fromtimestamp(ts_str):
    #     ts = int(ts_str)
    #     date_obj = datetime.fromtimestamp(ts)
    #     return str(date_obj)
    def __new__(cls):
        cls.__counter += 1
        dt = datetime.now()
        value = int(datetime.timestamp(dt))
        cls.__items.append(value)
        return super().__new__(cls)

    def __init__(self):
        self.__id = self.__items[-1]

    def __str__(self):
        return str(self.__id)
