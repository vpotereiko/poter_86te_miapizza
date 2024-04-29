import os
import pprint

APP_PATH = ''
from users import User

if __name__ == "__main__":
    # щось подібне до інсталаяції:
    # В папці з main.py  мають бути файли класів з репозиторію
    # При повторному запуску скануємо папки і вважаємо їх історією дій під користувачем
    # Папка як
    # users.json створені і збережені користувачі
    APP_PATH = __file__
    MAIN_PATH = os.environ['PYTHONPATH']
    # щось подібне до інсталаяції:
    # for i, env_item in enumerate(os.environ.items()):
    #    print(i, env_item)
    print(f"{os.path.dirname(os.path.dirname(__file__))=}")
    print(f"{os.environ['PYTHONPATH']=}")
    print(f"{__file__=}")
    u = User()
    u.get_method()
