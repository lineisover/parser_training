import logging

import converter
import utils
from settings import LOG_FILE, PATH_TO_VEH_PATHS

logging.basicConfig(handlers=[logging.FileHandler(LOG_FILE, 'w', 'utf-8')],
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

def main():
    prototypes_list = []
    vehicleparts = utils.load_xml(PATH_TO_VEH_PATHS)
    utils.parse_object(vehicleparts, prototypes_list)
    converter.convert_to_json(prototypes_list)

if __name__ == '__main__':
    main()
