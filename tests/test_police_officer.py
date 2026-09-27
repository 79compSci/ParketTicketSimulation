"""Unit tests for the PoliceOfficer class and object collaboration."""

import unittest

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    """Test officer properties and parking inspection behavior."""

    def setUp(self):
        """Create an officer used by the inspection tests."""
        self.officer = PoliceOfficer("John Smith", "5678")

    def test_valid_construction_and_property_access(self):
        """A valid officer should expose name and badge number."""
        self.assertEqual(self.officer.name, "John Smith")
        self.assertEqual(self.officer.badge_number, "5678")

    def test_invalid_officer_strings_are_rejected(self):
        """Officer name and badge number must be nonempty strings."""
        with self.assertRaises(ValueError):
            PoliceOfficer("", "5678")
        with self.assertRaises(ValueError):
            PoliceOfficer("John Smith", "   ")
        with self.assertRaises(TypeError):
            PoliceOfficer(123, "5678")
        with self.assertRaises(TypeError):
            PoliceOfficer("John Smith", 5678)

    def test_less_time_than_purchased_returns_none(self):
        """No ticket should be issued before purchased time expires."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 59)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNone(ticket)

    def test_exactly_purchased_time_returns_none(self):
        """No ticket should be issued at exactly the purchased time."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNone(ticket)

    def test_one_minute_over_returns_parking_ticket(self):
        """One minute beyond purchased time should produce a ticket."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 61)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNotNone(ticket)
        self.assertIsInstance(ticket, ParkingTicket)
        self.assertEqual(ticket.illegal_minutes, 1)
        self.assertEqual(ticket.fine, 25)

    def test_illegal_minutes_are_calculated_correctly(self):
        """The officer should calculate parked time minus purchased time."""
        car = ParkedCar("Honda", "Accord", "Black", "XYZ789", 181)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertEqual(ticket.illegal_minutes, 121)
        self.assertEqual(ticket.fine, 45)

    def test_ticket_contains_expected_car_and_officer_information(self):
        """Returned ticket should reference the inspected car and officer."""
        car = ParkedCar("Ford", "Mustang", "Red", "CAR007", 121)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIs(ticket.car, car)
        self.assertIs(ticket.officer, self.officer)
        self.assertEqual(ticket.car.make, "Ford")
        self.assertEqual(ticket.car.model, "Mustang")
        self.assertEqual(ticket.car.color, "Red")
        self.assertEqual(ticket.car.license_number, "CAR007")
        self.assertEqual(ticket.officer.name, "John Smith")
        self.assertEqual(ticket.officer.badge_number, "5678")


if __name__ == "__main__":
    unittest.main()
