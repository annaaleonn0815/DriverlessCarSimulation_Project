import time
from collections import deque

class DriverlessCar:                     # Parent class
    def __init__(self, speed, location, destination):
        self._speed = speed
        self._location = location
        self._destination = destination
        self._data = {}
        self._obstacle_detected = False
        self._location_history = []
        self._location_queue = deque()  # Initializes the location queue as a deque

    def add_location_to_history(self, location):
        self._location_history.append(location)

    def get_location_history(self):
        return self._location_history

    def push_location_to_queue(self, location):
        self._location_queue.append(location)

    def pop_location_from_queue(self):
        if len(self._location_queue) > 0:
            return self._location_queue.popleft()  # Uses and returns the leftmost item from the deque
        else:
            return None

    def __str__(self):
        return f"DriverlessCar(speed={self._speed}, location={self._location}, destination={self._destination})"

    def _simulate_data(self):
        self._data["speed"] = self._speed
        self._data["location"] = self._location
        self._data["destination"] = self._destination

    def get_data(self):
        self._simulate_data()
        return self._data

    def update_speed(self, new_speed):
        self._speed = new_speed
        self._simulate_data()

    def update_location(self, new_location):
        self._location = new_location
        self._simulate_data()

    def update_destination(self, new_destination):
        self._destination = new_destination
        self._simulate_data()

    def navigate(self):
        print(f"{self} is navigating...")
        time.sleep(2)
        print(f"{self} has arrived at {self._destination}.")

    def navigate_async(self):
        print(f"{self} is navigating asynchronously...")
        time.sleep(1)
        print(f"{self} has reached {self._location}.")
        time.sleep(1)
        print(f"{self} is speeding up to {self._speed} mph.")
        time.sleep(1)
        while self._location != self._destination:
            if self._obstacle_detected or self._speed > 100:
                self.emergency_brake()
                break
            self._location = self.pop_location_from_queue()  # gets the next location from the deque
            if self._location is None:
                break
            print(f"{self} is now at {self._location}.")
            time.sleep(1)
        if not self._obstacle_detected:
            print(f"{self} has arrived at {self._destination}.")

    def emergency_brake(self):
        print(f"{self} is applying the emergency brake...")
        time.sleep(1)
        print(f"{self} has stopped.")
        self._speed = 0

    def detect_obstacle(self):
        print(f"{self} is detecting obstacle...")
        time.sleep(1)
        self._obstacle_detected = True
        print(f"{self} has detected an obstacle and applied the emergency brake.")

#This child class inherits all of the attributes and methods of the SelfDrivingCar (parent) class 
class SelfDrivingCar(DriverlessCar):         
    def __init__(self, speed, location, destination):
        super().__init__(speed, location, destination)

    def navigate(self):
        print(f"{self} is navigating with self-driving mode...")
        time.sleep(2)
        print(f"{self} has arrived at {self._destination}.")

#Assert statements are used to test the class and its associated methods to see if it behaves as intended (Phillips, 2018).
def test_DriverlessCar():
    car = DriverlessCar(60, "A", "B")
    assert car.get_data() == {"speed": 60, "location": "A", "destination": "B"}

    car.update_speed(80)
    car.update_location("C")
    car.update_destination("D")
    assert car.get_data() == {"speed": 80, "location": "C", "destination": "D"}

    car.push_location_to_queue("B")
    car.push_location_to_queue("C")
    car.push_location_to_queue("D")
    car.navigate_async()

    car2 = DriverlessCar(50, "X", "Y")
    car2.push_location_to_queue("Z")
    car2.detect_obstacle()

def main():
    speed = int(input("Enter the speed of the car: "))
    location = input("Enter the location of the car: ")
    destination = input("Enter the destination of the car: ")
    car = DriverlessCar(speed, location, destination)
    print("Initial car data: ", car.get_data())

    user_input = input("Do you want to update the speed, location, or destination of the car (enter 'speed', 'location', 'destination', or 'exit' to exit)? ")
    while user_input != "exit":
        if user_input == "speed":
            new_speed = int(input("Enter the new speed: "))
            car.update_speed(new_speed)
            print("Updated car data: ", car.get_data())

            if new_speed > 100:
                print("WARNING: Speed limit exceeded. Applying emergency brake...")
                car.emergency_brake()

        elif user_input == "location":
            new_location = input("Enter the new location: ")
            car.update_location(new_location)
            print("Updated car data: ", car.get_data())

        elif user_input == "destination":
            new_destination = input("Enter the new destination: ")
            car.update_destination(new_destination)
            print("Updated car data: ", car.get_data())

        elif user_input == "obstacle":
            print("WARNING: Obstacle detected. Applying emergency brake...")
            car.detect_obstacle()

        else:
            print("Invalid input, try again.")

        user_input = input("Do you want to update the speed, location, or destination of the car (enter 'speed', 'location', 'destination', 'obstacle', or 'exit' to exit)? ")

if __name__ == "__main__":
    test_DriverlessCar()
    main()

#References
# Phillips, D. (2018) Python 3 Object-Oriented Programming. 3rd ed. Birmingham: Packt Publishing.

