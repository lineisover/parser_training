import json
import logging
from pathlib import PurePath

from settings import DEFAULT_BENDING, DEFAULT_MASS, OUTPUT_FILE, PATH_TO_MODELS


def type_defination(cls):
    match cls:
        case 'Chassis':
            return 'ResourceChassis'
        case 'Cabin':
            return 'ResourceCabin'
        case 'Basket':
            return 'ResourceCargo'
        case 'Wheel':
            return 'ResourceWheel'


# TODO: Нужно как то определять имя папки ^o^
def convert_model_path(path: str):
    new_filename = PurePath(path).with_suffix('.glb')
    new_path = PATH_TO_MODELS / new_filename
    new_path_str = str(new_path).replace('\\', '/')
    return new_path_str


def weight_defination(mass):
    if not mass:
        return DEFAULT_MASS
    else:
        return float(mass)


def bending_defination(cls):
    match cls:
        case 'Chassis':
            return DEFAULT_BENDING.get('Chassis')
        case 'Cabin':
            return DEFAULT_BENDING.get('Cabin')
        case 'Basket':
            return DEFAULT_BENDING.get('Cargo')
        case 'Wheel':
            return None


def convert_to_json(prototypes: list):
    logging.info(f'Обнаружено {len(prototypes)} прототипов.')
    json_parts = []
    for prototype in prototypes:
        part = {'type': type_defination(prototype.cls),
                'token': prototype.name,
                'group': prototype.resource_type,
                'model': convert_model_path(prototype.model_file),
                'weight': weight_defination(prototype.mass),
                'bending': bending_defination(prototype.cls)}
        json_parts.append(part)
    with open(OUTPUT_FILE, 'w') as json_file:
        json.dump(json_parts, json_file, indent=4)
