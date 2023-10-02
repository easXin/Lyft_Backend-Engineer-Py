import unittest
from tires.type.octoprime_tires import OctoprimeTires
from tires.type.carrigan_tires import CarriganTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_false(self):
        octoprime_tires = OctoprimeTires([1.0, 1.0, 1.0])
        self.assertTrue(octoprime_tires.needs_service())

    def test_needs_service_true(self):
        octoprime_tires = OctoprimeTires([1.0, 1.0, 1.2])
        self.assertTrue(octoprime_tires.needs_service())

    def test_needs_service_empty(self):
        octoprime_tires = OctoprimeTires([])
        self.assertFalse(octoprime_tires.needs_service())


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_false(self):
        carrigan_tires = CarriganTires([0.8, 0.85, 0.88])
        self.assertFalse(carrigan_tires.needs_service())

    def test_needs_service_true(self):
        carrigan_tires = CarriganTires([0.8, 0.95, 0.88])
        self.assertTrue(carrigan_tires.needs_service())

    def test_needs_service_empty(self):
        carrigan_tires = CarriganTires([])
        self.assertFalse(carrigan_tires.needs_service())