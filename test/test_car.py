import unittest
from datetime import date, timedelta
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class EngineTests(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(40000, 30000)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        engine = CapuletEngine(25000, 30000)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())


class BatteryTests(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        last_service_date = date.today() - timedelta(days=365 * 3)  # 3 years ago
        current_date = date.today()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        last_service_date = date.today() - timedelta(days=365)  # 1 year ago
        current_date = date.today()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        last_service_date = date.today() - timedelta(days=365 * 5)  # 5 years ago
        current_date = date.today()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        last_service_date = date.today() - timedelta(days=365 * 3)  # 3 years ago
        current_date = date.today()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
