from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.nubbin_year_need_service = 2

    def needs_service(self):
        year_diff = self.current_date.year - self.last_service_date.year
        print(year_diff)
        if year_diff >= self.nubbin_year_need_service:
            return True
        else:
            return False
