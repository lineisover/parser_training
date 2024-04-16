import json
import logging

from parts import VehiclePart
from settings import OUTPUT_FILE


def convert_to_json(prototypes: list[VehiclePart], animmodels):
    logging.info(f'Обнаружено {len(prototypes)} прототипов.')
    json_parts = []
    logging.info('Начинаем подготовку прототипов к экспорту.')
    for prototype in prototypes:
        try:
            print(prototype.name)
            part = {'type': prototype.type_defination(),
                    'token': prototype.name,
                    'group': prototype.group_defination(),
                    'model': prototype.convert_model_path(animmodels),
                    'weight': prototype.weight_defination(),
                    'bending': prototype.bending_defination(),
                    'stiffness': prototype.stiffness_defination(),
                    'mass_center':prototype.mass_center_defination(),
                    'skin': prototype.skin_defination(),
                    'materials': {},  # TODO: Нужно как то вытаскивать из glb, которых нет...
                    'is_power': prototype.is_power(),
                    'is_steer': prototype.is_steer(),
                    'is_brake': prototype.is_brake()}
            keys_to_remove = [key for key, value in part.items() if value == 'Unavailable']
            for key in keys_to_remove:
                del part[key]
        except Exception as e:
            logging.error(f'Ошибка при обработке прототипа {prototype.name}: {e}')
            raise
        json_parts.append(part)
        logging.info(f'Прототип {prototype.name} готов.')
    with open(OUTPUT_FILE, 'w') as json_file:
        json.dump(json_parts, json_file, indent=4)
        logging.info(f'Прототипы сохранены в {OUTPUT_FILE}')
