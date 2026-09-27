"""Define the PoliceOfficer class for the parking ticket simulator."""

from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represent a police officer who inspects parked cars."""

    def __init__(self, name, badge_number):
        """Initialize an officer with a name and badge number."""
        self.name = name
        self.badge_number = badge_number

    @staticmethod
    def _validate_string(value, field_name):
        """Validate a required nonempty string value."""
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return value

    @property
    def name(self):
        """Return the officer's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the officer's name to a nonempty string."""
        self._name = self._validate_string(value, "name")

    @property
    def badge_number(self):
        """Return the officer's badge number."""
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value):
        """Set the officer's badge number to a nonempty string."""
        self._badge_number = self._validate_string(value, "badge_number")

    def inspect_car(self, car, meter):
        """Inspect a parked car and return a ticket when time has expired.

        Args:
            car: ParkedCar object containing the number of minutes parked.
            meter: ParkingMeter object containing purchased parking minutes.

        Returns:
            ParkingTicket: A ticket when the car exceeded purchased time.
            None: When the car is still legally parked.
        """
        illegal_minutes = car.minutes_parked - meter.minutes_purchased

        if illegal_minutes <= 0:
            return None

        return ParkingTicket(car, self, illegal_minutes)
