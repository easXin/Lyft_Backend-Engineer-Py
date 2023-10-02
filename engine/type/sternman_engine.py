from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
