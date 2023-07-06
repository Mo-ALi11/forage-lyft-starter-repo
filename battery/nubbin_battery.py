from datetime import date, timedelta

class NubbinBattery:
    SERVICE_YEARS = 4

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        years_since_service = (self.current_date - self.last_service_date).days // 365
        return years_since_service >= NubbinBattery.SERVICE_YEARS
