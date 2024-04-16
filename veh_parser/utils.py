import logging
from pathlib import Path, PurePath

from lxml import objectify
from parts import Cabin, Cargo, Chassis, Wheel
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

def identify_class(class_name: str, object):
    if class_name == 'Chassis':
        return Chassis(object)
    elif class_name == 'Cabin':
        return Cabin(object)
    elif class_name == 'Basket':
        return Cargo(object)
    elif class_name == 'Wheel':
        return Wheel(object)


def parse_object(object, prototypes_list) -> list:
    part_classes = ['Chassis', 'Cabin', 'Basket', 'Wheel']
    for folder in object.iterchildren():
        for prototype in folder.iterchildren():
            logging.info(f'Загружает прототип: {prototype.get('Name')}')
            if prototype.get('Class') in part_classes:
                part = identify_class(prototype.get('Class'), prototype)
                prototypes_list.append(part)
                logging.info(f'Class: {part.cls} Name: {part.name} - Загружен.')
            else:
                logging.warning(f'{prototype.get('Class')} - Неподходящий класс')
    logging.info('Обработка завершена.')
