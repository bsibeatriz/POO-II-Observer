class MotorVehicleFactory:
    def create(self):
        return self.createMotorVehicle()

    def createMotorVehicle(self):
        pass

class MotorVehicle:
    def build(self):
        pass

class Motorcycle(MotorVehicle):
    def build(self):
        print("Construindo uma motocicleta.")

class Car(MotorVehicle):
    def build(self):
        print("Construindo um carro.")

class MotorcycleFactory(MotorVehicleFactory):
    def createMotorVehicle(self):
        return Motorcycle()

class CarFactory(MotorVehicleFactory):
    def createMotorVehicle(self):
        return Car()

