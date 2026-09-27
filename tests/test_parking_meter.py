"""Unit tests for the ParkingMeter class."""

import unittest

from parking_meter import ParkingMeter


class TestParkingMeter(unittest.TestCase):
    """Test ParkingMeter construction, properties, and validation."""

    def test_valid_construction_and_property_access(self):
        """A valid meter should expose its purchased minutes."""
        meter = ParkingMeter(60)
        self.assertEqual(meter.minutes_purchased, 60)

    def test_zero_minutes_purchased_is_valid(self):
        """Zero purchased minutes should be accepted."""
        meter = ParkingMeter(0)
        self.assertEqual(meter.minutes_purchased, 0)

    def test_positive_minutes_purchased_is_valid(self):
        """Positive purchased minutes should be accepted."""
        meter = ParkingMeter(120)
        self.assertEqual(meter.minutes_purchased, 120)

    def test_negative_minutes_purchased_raises_value_error(self):
        """Negative purchased minutes should be rejected."""
        with self.assertRaises(ValueError):
            ParkingMeter(-1)

    def test_noninteger_minutes_purchased_raises_type_error(self):
        """Noninteger purchased minutes should be rejected."""
        with self.assertRaises(TypeError):
            ParkingMeter(60.5)
        with self.assertRaises(TypeError):
            ParkingMeter("60")
        with self.assertRaises(TypeError):
            ParkingMeter(True)

    def test_valid_property_reassignment(self):
        """The property should accept a valid replacement value."""
        meter = ParkingMeter(30)

        meter.minutes_purchased = 90

        self.assertEqual(meter.minutes_purchased, 90)

    def test_invalid_property_reassignment_is_rejected(self):
        """The property setter should validate replacement values."""
        meter = ParkingMeter(30)

        with self.assertRaises(ValueError):
            meter.minutes_purchased = -5
        with self.assertRaises(TypeError):
            meter.minutes_purchased = 30.5


if __name__ == "__main__":
    unittest.main()
