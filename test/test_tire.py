import unittest
from datetime import date, timedelta
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from carFactory import CarFactory

class CarFactoryTests(unittest.TestCase):
    def setUp(self):
        self.factory = CarFactory()

    def test_spindler_battery_needs_service(self):
        last_service_date = date.today() - timedelta(days=365 * 3)  # 3 years ago
        current_date = date.today()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_carrigan_tires_needs_service(self):
        tire_wear = [0.8, 0.7, 0.6, 0.9]
        self.assertTrue(self.factory.needs_tire_service('Carrigan', tire_wear))

    def test_carrigan_tires_do_not_need_service(self):
        tire_wear = [0.5, 0.6, 0.7, 0.8]
        self.assertFalse(self.factory.needs_tire_service('Carrigan', tire_wear))

    def test_octoprime_tires_needs_service(self):
        tire_wear = [1, 1, 0.5, 0.7]
        self.assertTrue(self.factory.needs_tire_service('Octoprime', tire_wear))

    def test_octoprime_tires_do_not_need_service(self):
        tire_wear = [0.5, 0.6, 0.7, 0.8]
        self.assertFalse(self.factory.needs_tire_service('Octoprime', tire_wear))

if __name__ == '__main__':
    unittest.main()
