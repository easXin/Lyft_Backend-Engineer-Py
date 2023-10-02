from car import Car

from battery.type.nubbinBattery import NubbinBattery
from battery.type.spindlerBattery import SpindlerBattery

from engine.type.capulet_engine import CapuletEngine
from engine.type.sternman_engine import SternmanEngine
from engine.type.willoughby_engine import WilloughbyEngine
from tires.type.carrigan_tires import CarriganTires
from tires.type.octoprime_tires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on,tire):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tire):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tire)
        car = Car(engine, battery, tires)
        return car