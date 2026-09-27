"""Define the ParkingTicket class for the parking ticket simulator."""


class ParkingTicket:
    """Represent a citation issued to an illegally parked car.

    The ticket stores references to the collaborating car and officer rather
    than copying their identifying data. This avoids duplicating source data.
    """

    def __init__(self, car, officer, illegal_minutes):
        """Initialize a parking ticket for a violation.

        Args:
            car: ParkedCar associated with the violation.
            officer: PoliceOfficer issuing the ticket.
            illegal_minutes: Minutes beyond purchased parking time.

        Raises:
            TypeError: If illegal_minutes is not an integer.
            ValueError: If illegal_minutes is less than one.
        """
        self._car = car
        self._officer = officer
        self.illegal_minutes = illegal_minutes

    @property
    def car(self):
        """Return the parked car associated with the ticket."""
        return self._car

    @property
    def officer(self):
        """Return the police officer who issued the ticket."""
        return self._officer

    @property
    def illegal_minutes(self):
        """Return the number of illegally parked minutes."""
        return self._illegal_minutes

    @illegal_minutes.setter
    def illegal_minutes(self, value):
        """Set illegal minutes to a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("illegal_minutes must be an integer")
        if value < 1:
            raise ValueError("illegal_minutes must be at least 1")
        self._illegal_minutes = value

    @property
    def fine(self):
        """Return the fine using the required partial-hour rounding rules."""
        hours = (self.illegal_minutes + 59) // 60
        return 25 + (hours - 1) * 10

    def report(self):
        """Return a readable report containing citation information."""
        return (
            "PARKING TICKET\n"
            f"Make: {self.car.make}\n"
            f"Model: {self.car.model}\n"
            f"Color: {self.car.color}\n"
            f"License Number: {self.car.license_number}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Officer: {self.officer.name}\n"
            f"Badge Number: {self.officer.badge_number}"
        )

    def __str__(self):
        """Return the readable ticket report."""
        return self.report()
