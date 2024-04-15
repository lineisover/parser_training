from pathlib import Path

LOG_FILE = 'parser.log'
ENCODING = 'windows-1251'
GAME_PATH = Path('C:/Games/Hard Truck PARSE')
PATH_TO_VEH_PATHS = Path('data/gamedata/gameobjects/vehicleparts.xml')
OUTPUT_FILE = 'vehicleparts.json'
PATH_TO_MODELS = Path('models/vehicle')
DEFAULT_MASS = 1000
DEFAULT_BENDING = {'Chassis': [5.0, 5.0, 5.0], 'Cabin': [5.0, 0.0, 5.0], 'Cargo': [5.0, 0.0, 5.0]}
RESOURCE_TYPE_POSTFIX = {'_CHASSIS',
                         '_TRAILER',
                         '_CABIN',
                         '_BASKET',
                         '_BIGBASKET',
                         }
