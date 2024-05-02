import json
import os
from code_generator import CodeGenerator

APP_FOLDER = "D:\\_\\Pizzz"
FILES_PATHS = [
    os.path.dirname(os.path.dirname(__file__)),
]


class FileDB:
    _items = []

    def __new__(cls, *args, **kwargs):
        if 'instance' in kwargs:
            cls._items.append(kwargs['instance'])
        return super().__new__(cls)

    def __init__(self, instance):
        self._items.append(instance)
        self.paths = FILES_PATHS
        try:
            self._id = str(CodeGenerator())
            self.file_name = f"{self._id}_{str(id(self))+self.__class__.__name__}.json"
        except Exception as e:
            print(e)
            self.proj_id = str(CodeGenerator())
            self.task_id = str(CodeGenerator())
            self.file_name = f"{self.proj_id}_{self.task_id}_{self._owner.name}.json"

    def __str__(self):
        return f"{self.file_name}"
