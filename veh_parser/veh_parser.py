import logging

from parts import Cabin, Cargo, Chassis
from settings import LOG_FILE, PATH_TO_VEH_PATHS
from utils import load_xml

logging.basicConfig(handlers=[logging.FileHandler(LOG_FILE, 'w', 'utf-8')],
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def get_attr(attr: str | None, necessarily: bool = True, default: str = 'None'):
    if necessarily and not attr:
        raise print()

def main():
    prototypes_list = []
    vehicleparts = load_xml(PATH_TO_VEH_PATHS)
    for folder in vehicleparts.iterchildren():
        print(folder.get('Name'))
        for prototype in folder.iterchildren():
            print(prototype.get('Name'))
            logging.info(f'Загружает прототип: {prototype.get('Name')}')
            if prototype.get('Class') == 'Chassis':
                chassis_part = Chassis(prototype)
                prototypes_list.append(chassis_part)
                logging.info(f'Class: {chassis_part.cls} Name: {chassis_part.name} - Загружен.')
            elif prototype.get('Class') == 'Cabin':
                cabin_part = Cabin(prototype)
                prototypes_list.append(cabin_part)
                logging.info(f'Class: {cabin_part.cls} Name: {cabin_part.name} - Загружен.')
            elif prototype.get('Class') == 'Basket':
                cargo_part = Cargo(prototype)
                prototypes_list.append(cargo_part)
                logging.info(f'Class: {cargo_part.cls} Name: {cargo_part.name} - Загружен.')
            elif prototype.get('Class') == 'Wheel':
                wheel_part = Cargo(prototype)
                prototypes_list.append(wheel_part)
                logging.info(f'Class: {wheel_part.cls} Name: {wheel_part.name} - Загружен.')
            else:
                logging.warning(f'{prototype.get('Class')} - Неподходящий класс')
    logging.info('Обработка завершена.')



if __name__ == '__main__':
    main()
