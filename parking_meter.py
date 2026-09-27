"""Define the ParkingMeter class for the parking ticket simulator."""


class ParkingMeter:
    """Represent a parking meter and the number of minutes purchased."""

    def __init__(self, minutes_purchased):
        """Initialize the meter with purchased parking time.

        Args:
            minutes_purchased: Number of parking minutes purchased.

        Raises:
            TypeError: If minutes_purchased is not an integer.
            ValueError: If minutes_purchased is negative.
        """
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        """Return the number of purchased parking minutes."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        """Set purchased parking minutes to a nonnegative integer.

        Args:
            value: Number of parking minutes purchased.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_purchased must be an integer")
        if value < 0:
            raise ValueError("minutes_purchased cannot be negative")
        self._minutes_purchased = value
