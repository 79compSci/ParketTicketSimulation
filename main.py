"""Demonstrate collaboration among the parking ticket simulator classes."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Create sample objects and demonstrate a parking inspection."""
    car = ParkedCar("Toyota", "Camry", "Blue", "ABC123", 121)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("John Smith", "5678")

    ticket = officer.inspect_car(car, meter)

    if ticket is None:
        print("No parking violation. No ticket was issued.")
    else:
        print(ticket)


if __name__ == "__main__":
    main()
