import logging

import converter
import utils
from settings import LOG_FILE, PATH_TO_ANIMMODELS, PATH_TO_VEH_PATHS

logging.basicConfig(handlers=[logging.FileHandler(LOG_FILE, 'w', 'utf-8')],
                    format='%(asctime)s: %(levelname)-8s - %(message)s',
                    level=logging.DEBUG)

def main():
    prototypes_list = []
    animmodels = utils.load_xml(PATH_TO_ANIMMODELS)
    vehicleparts = utils.load_xml(PATH_TO_VEH_PATHS)
    utils.parse_object(vehicleparts, prototypes_list)
    converter.convert_to_json(prototypes_list, animmodels)

if __name__ == '__main__':
    main()
