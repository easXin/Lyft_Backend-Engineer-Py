from battery.battery import Battery


class NubbinBattery(Battery):
    def __int__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.nubbin_year_need_service = 2

    def needs_service(self):
        year_diff = self.current_date - self.last_service_date.year
        if year_diff >= self.nubbin_year_need_service:
            return True
        else:
            return False
