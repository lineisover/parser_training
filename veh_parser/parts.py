import logging

from lxml import objectify
from settings import RESOURCE_TYPE_POSTFIX


class VehiclePart():
    def __init__(self, object) -> None:
        self.cls = get_attr('Class', object)
        self.name = get_attr('Name', object)
        self.model_file = get_attr('ModelFile', object)
        self.resource_type = get_attr('ResourceType', object, False)
        self.node_scale = get_attr('NodeScale', object)
        self.mass = get_attr('Mass', object)
        self.encyclopedia = get_attr('VisibleInEncyclopedia', object, False)
        self.loadpoints = get_attr('LoadPoints', object, False)

    def group_defination(self):
        for element in RESOURCE_TYPE_POSTFIX:
            if element in self.resource_type:
                patrition = self.resource_type.rpartition(element)
                group = patrition[0]
        return group.capitalize()

class Chassis(VehiclePart):
    def __init__(self, object) -> None:
        super().__init__(object)
        self.max_health = get_attr('MaxHealth', object)
        self.max_fuel = get_attr('MaxFuel', object)
        self.braking_sound = get_attr('BrakingSound', object)
        self.pneumo_sound = get_attr('PneumoSound', object)
        self.gear_shift_sound = get_attr('GearShiftSound', object)

    def type_defination(self):
        return 'ResourceChassis'

class Cabin(VehiclePart):
    def __init__(self, object) -> None:
        super().__init__(object)
        self.durability = get_attr('Durability', object)
        self.coeffs_damage = get_attr('DurCoeffsForDamageTypes', object)
        self.max_power = get_attr('MaxPower', object)
        self.max_torque = get_attr('MaxTorque', object)
        self.engine_high_sound = get_attr('EngineHighSound', object)
        self.price = get_attr('Price', object)
        self.repair_coef = get_attr('RepairCoef', object, False)
        self.max_speed = get_attr('MaxSpeed', object)
        self.blow_effect = get_attr('BlowEffect', object)
        self.fuel_consumption = get_attr('FuelConsumption', object, False)

    def type_defination(self):
        return 'ResourceCabin'

class Cargo(VehiclePart):
    def __init__(self, object) -> None:
        super().__init__(object)
        self.durability = get_attr('Durability', object)
        self.coeffs_damage = get_attr('DurCoeffsForDamageTypes', object)
        self.blow_effect = get_attr('BlowEffect', object)
        self.price = get_attr('Price', object)
        self.repair_coef = get_attr('RepairCoef', object)

    def type_defination(self):
        return 'ResourceCargo'

class Wheel(VehiclePart):
    def __init__(self, object) -> None:
        super().__init__(object)
        self.suspension_model = get_attr('SuspensionModelFile', object)
        self.suspension_cfm = get_attr('SuspensionCFM', object)
        self.suspension_erp = get_attr('SuspensionERP', object)
        self.suspension_range = get_attr('SuspensionRange', object)
        self.mu = get_attr('mU', object)
        self.effect_type = get_attr('EffectType', object)

    def type_defination(self):
        return 'ResourceWheel'

    def group_defination(self):
        patrition = self.name.rpartition('Wheel')
        print(patrition[0].capitalize())
        return patrition[0].capitalize()


def get_attr(attr: str, prototype: objectify.ObjectifiedElement, importantly: bool = True):
    parse = prototype.get(attr)
    if not parse and not importantly:
        logging.debug(f'Атрибут {attr} может существовать, но не обнаружен в {prototype.get('Name')}')
    elif not parse and importantly:
        logging.warning(f'Атрибут {attr} должен существовать, но не обнаружен в {prototype.get('Name')}')
    return parse
