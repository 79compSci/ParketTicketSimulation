"""Unit tests for the ParkedCar class."""

import unittest

from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    """Test construction, properties, reassignment, and validation."""

    def test_valid_construction_and_property_access(self):
        """A valid car should expose all constructor values."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60)

        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.color, "Blue")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 60)

    def test_valid_property_reassignment(self):
        """Public properties should accept valid replacement values."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60)

        car.make = "Honda"
        car.model = "Accord"
        car.color = "Black"
        car.license_number = "XYZ789"
        car.minutes_parked = 90

        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Accord")
        self.assertEqual(car.color, "Black")
        self.assertEqual(car.license_number, "XYZ789")
        self.assertEqual(car.minutes_parked, 90)

    def test_empty_string_values_raise_value_error(self):
        """Required string properties should reject empty strings."""
        with self.assertRaises(ValueError):
            ParkedCar("", "Camry", "Blue", "ABC123", 60)
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "   ", "Blue", "ABC123", 60)
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "", "ABC123", 60)
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "", 60)

    def test_incorrect_string_types_raise_type_error(self):
        """Required string properties should reject non-string values."""
        with self.assertRaises(TypeError):
            ParkedCar(123, "Camry", "Blue", "ABC123", 60)
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", None, "Blue", "ABC123", 60)
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", 5, "ABC123", 60)
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", 12345, 60)

    def test_zero_minutes_parked_is_valid(self):
        """Zero parked minutes should be accepted."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 0)
        self.assertEqual(car.minutes_parked, 0)

    def test_positive_minutes_parked_is_valid(self):
        """Positive parked minutes should be accepted."""
        car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 121)
        self.assertEqual(car.minutes_parked, 121)

    def test_negative_minutes_parked_raises_value_error(self):
        """Negative parked minutes should be rejected."""
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", -1)

    def test_noninteger_minutes_parked_raises_type_error(self):
        """Noninteger parked minutes should be rejected."""
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", 60.5)
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", "60")
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "ABC123", True)


if __name__ == "__main__":
    unittest.main()
