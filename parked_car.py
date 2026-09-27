"""Define the ParkedCar class for the parking ticket simulator."""


class ParkedCar:
    """Represent a car parked at a parking meter."""

    def __init__(self, make, model, color, license_number, minutes_parked):
        """Initialize a parked car with identifying information and parked time."""
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @staticmethod
    def _validate_string(value, field_name):
        """Validate a required nonempty string value."""
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty")
        return value

    @property
    def make(self):
        """Return the car's make."""
        return self._make

    @make.setter
    def make(self, value):
        """Set the car's make to a nonempty string."""
        self._make = self._validate_string(value, "make")

    @property
    def model(self):
        """Return the car's model."""
        return self._model

    @model.setter
    def model(self, value):
        """Set the car's model to a nonempty string."""
        self._model = self._validate_string(value, "model")

    @property
    def color(self):
        """Return the car's color."""
        return self._color

    @color.setter
    def color(self, value):
        """Set the car's color to a nonempty string."""
        self._color = self._validate_string(value, "color")

    @property
    def license_number(self):
        """Return the car's license number."""
        return self._license_number

    @license_number.setter
    def license_number(self, value):
        """Set the license number to a nonempty string."""
        self._license_number = self._validate_string(value, "license_number")

    @property
    def minutes_parked(self):
        """Return the number of minutes the car has been parked."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        """Set minutes parked to a nonnegative integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_parked must be an integer")
        if value < 0:
            raise ValueError("minutes_parked cannot be negative")
        self._minutes_parked = value
