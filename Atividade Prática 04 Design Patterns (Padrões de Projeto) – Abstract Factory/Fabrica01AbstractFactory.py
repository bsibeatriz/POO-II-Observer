class Corporação:
    def criar_veículo_motor(self):
        pass

    def criar_veículo_elétrico(self):
        pass


class FutureVehicleCorporation(Corporação):
    def criar_veículo_motor(self):
        return MotorVehicle()

    def criar_veículo_elétrico(self):
        return ElectricVehicle()


class NextGenCorporation(Corporação):
    def criar_veículo_motor(self):
        return NextGenMotorcycle()

    def criar_veículo_elétrico(self):
        return NextGenElectricCar()


class MotorVehicle:
    pass

class ElectricVehicle:
    pass

class NextGenMotorcycle:
    pass

class NextGenElectricCar:
    pass
