import json
import os
from code_generator import CodeGenerator

FILES_PATHS = [
    os.path.dirname(os.path.dirname(__file__)),
]


class FileDB:

    def __init__(self, instance):
        self._owner = instance
        self.paths = FILES_PATHS
        try:
            self.proj_id = str(CodeGenerator())
            self.file_name = f"{self.proj_id}_{self._owner.name}.json"
        except Exception as e:
            print(e)
            self.proj_id = str(CodeGenerator())
            self.task_id = str(CodeGenerator())
            self.file_name = f"{self.proj_id}_{self.task_id}_{self._owner.name}.json"

    def __str__(self):
        return f"{self.file_name}"

