import logging
from pathlib import Path, PurePath

from lxml import objectify
from settings import ENCODING, GAME_PATH


def load_xml(file_dir: Path):
    full_path = GAME_PATH / file_dir
    try:
        with open(full_path, encoding=ENCODING) as f:
            parser_recovery = objectify.makeparser(recover=True, encoding=ENCODING, collect_ids=False)
            objectify.enable_recursive_str()
            objfy = objectify.parse(f, parser_recovery)
        file = PurePath(full_path)
        logging.info(f'{file.parts[-1]} файл готов к обработке.')
        return objfy.getroot()
    except Exception as e:
        logging.error('Ошибка при загрузке XML файла: %s', str(e))

def get_attr(attr: str, prototype: objectify.ObjectifiedElement, importantly: bool = True):
    parse = prototype.get(attr)
    if not parse and importantly:
        logging.warning(f'Атрибут {attr} должен существовать, но не обнаружен в {prototype.get('Name')}')
    return parse
