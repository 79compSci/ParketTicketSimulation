"""Unit tests for the ParkingTicket class."""

import unittest

from parked_car import ParkedCar
from parking_ticket import ParkingTicket


class OfficerStub:
    """Provide officer data needed to test ParkingTicket independently."""

    def __init__(self, name="Jordan Smith", badge_number="B123"):
        self.name = name
        self.badge_number = badge_number


class TestParkingTicket(unittest.TestCase):
    """Test ticket data, fine boundaries, reporting, and validation."""

    def setUp(self):
        """Create collaborating objects used by the ticket tests."""
        self.car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 121)
        self.officer = OfficerStub()

    def test_correct_car_and_officer_information(self):
        """A ticket should report the collaborating car and officer data."""
        ticket = ParkingTicket(self.car, self.officer, 61)

        self.assertEqual(ticket.car.make, "Toyota")
        self.assertEqual(ticket.car.model, "Camry")
        self.assertEqual(ticket.car.color, "Blue")
        self.assertEqual(ticket.car.license_number, "ABC123")
        self.assertEqual(ticket.officer.name, "Jordan Smith")
        self.assertEqual(ticket.officer.badge_number, "B123")

    def test_correct_illegal_minutes(self):
        """The ticket should retain the supplied violation duration."""
        ticket = ParkingTicket(self.car, self.officer, 61)
        self.assertEqual(ticket.illegal_minutes, 61)

    def test_fine_boundaries(self):
        """Fine calculation should round every partial illegal hour upward."""
        cases = ((1, 25), (60, 25), (61, 35), (120, 35), (121, 45))

        for illegal_minutes, expected_fine in cases:
            with self.subTest(illegal_minutes=illegal_minutes):
                ticket = ParkingTicket(self.car, self.officer, illegal_minutes)
                self.assertEqual(ticket.fine, expected_fine)

    def test_readable_report_contains_required_information(self):
        """The ticket report should contain required car, violation, and officer data."""
        ticket = ParkingTicket(self.car, self.officer, 61)
        report = ticket.report()

        self.assertIn("Toyota", report)
        self.assertIn("Camry", report)
        self.assertIn("Blue", report)
        self.assertIn("ABC123", report)
        self.assertIn("61", report)
        self.assertIn("$35.00", report)
        self.assertIn("Jordan Smith", report)
        self.assertIn("B123", report)
        self.assertEqual(str(ticket), report)

    def test_zero_illegal_minutes_raises_value_error(self):
        """A ParkingTicket should require an actual violation."""
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)

    def test_negative_illegal_minutes_raises_value_error(self):
        """Negative illegal minutes should be rejected."""
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, -1)

    def test_noninteger_illegal_minutes_raises_type_error(self):
        """Illegal minutes must be an integer rather than another type."""
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, 1.5)
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, "61")
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, True)


if __name__ == "__main__":
    unittest.main()
