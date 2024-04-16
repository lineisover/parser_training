from pathlib import Path

LOG_FILE = 'parser.log'
ENCODING = 'windows-1251'

GAME_PATH = Path('C:/Games/Hard Truck PARSE')
PATH_TO_VEH_PATHS = Path('data/gamedata/gameobjects/vehicleparts.xml')
PATH_TO_ANIMMODELS = Path('data/models/animmodels.xml')
PATH_TO_MODELS = Path('models/vehicle')

OUTPUT_FILE = 'vehicleparts.json'

DEFAULT_MASS = {'Chassis': 1000, 'Cabin': 1000, 'Basket': 1000, 'Wheel': 80}
MASS_FACTOR = {'Chassis': 10, 'Cabin': 10, 'Basket': 10, 'Wheel': 10}

DEFAULT_BENDING = {'Chassis': [5.0, 5.0, 5.0],
                   'Cabin': [5.0, 0.0, 5.0],
                   'Basket': [5.0, 0.0, 5.0],
                   'Wheel': 'Unavailable'}

DEFAULT_STIFFNESS = {'Chassis': 10,
                   'Cabin': 3,
                   'Basket': 3,
                   'Wheel': 'Unavailable'}

DEFAULT_MASS_CENTER = {'Chassis': [0.0, -1.0, 0.0],
                       'Cabin': [0.0, 0.0, 0.0],
                       'Basket': [0.0, 0.0, 0.0],
                       'Wheel': [0.0, 0.0, 0.0]}

RESOURCE_TYPE_POSTFIX = {'_CHASSIS',
                         '_TRAILER',
                         '_CABIN',
                         '_BASKET',
                         '_BIGBASKET',
                         }
