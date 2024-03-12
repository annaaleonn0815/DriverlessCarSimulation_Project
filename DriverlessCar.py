class DriverlessCar:
    def __init__(self, speed, location, destination):
        self.speed = speed
        self.location = location
        self.destination = destination
        self.data = {}

    def simulate_data(self):
        self.data["speed"] = self.speed
        self.data["location"] = self.location
        self.data["destination"] = self.destination
        return self.data

    def update_speed(self, new_speed):
        self.speed = new_speed
        self.simulate_data()
        return self.data

    def update_location(self, new_location):
        self.location = new_location
        self.simulate_data()
        return self.data

    def update_destination(self, new_destination):
        self.destination = new_destination
        self.simulate_data()
        return self.data

def test_DriverlessCar():
    car = DriverlessCar("60", "A", "B")
    assert car.simulate_data() == {"speed": "60", "location": "A", "destination": "B"}
    assert car.update_speed("80") == {"speed": "80", "location": "A", "destination": "B"}
    assert car.update_location("C") == {"speed": "80", "location": "C", "destination": "B"}
    assert car.update_destination("D") == {"speed": "80", "location": "C", "destination": "D"}

def main():
    speed = input("Enter the speed of the car: ")
    location = input("Enter the location of the car: ")
    destination = input("Enter the destination of the car: ")
    car = DriverlessCar(speed, location, destination)
    print("Initial car data: ", car.simulate_data())

    user_input = input("Do you want to update the speed, location, or destination of the car (enter 'speed', 'location', 'destination', or 'exit' to exit)? ")
    while user_input != "exit":
        if user_input == "speed":
            new_speed = input("Enter the new speed: ")
            print("Updated car data: ", car.update_speed(new_speed))
        elif user_input == "location":
            new_location = input("Enter the new location: ")
            print("Updated car data: ", car.update_location(new_location))
        elif user_input == "destination":
            new_destination = input("Enter the new destination: ")
            print("Updated car data: ", car.update_destination(new_destination))
        else:
            print("Invalid input, try again.")
        user_input = input("Do you want to update the speed, location, or destination of the car (enter 'speed', 'location', 'destination', or 'exit' to exit)? ")

if __name__ == "__main__":
    test_DriverlessCar()
    main()
