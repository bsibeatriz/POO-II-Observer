class Product:
    def __init__(self, color, width, height, depth):
        self.color = color
        self.width = width
        self.height = height
        self.depth = depth

    def GetColor(self):
        return self.color

    def ToString(self):
        pass

class Armchair(Product):
    def ToString(self):
        return f"Armchair: Color({self.color}), Width({self.width}), Height({self.height}), Depth({self.depth})"

class CoffeeTable(Product):
    def ToString(self):
        return f"CoffeeTable: Color({self.color}), Width({self.width}), Height({self.height}), Length({self.depth})"

class Sofa(Product):
    def ToString(self):
        return f"Sofa: Color({self.color}), Width({self.width}), Height({self.height}), Depth({self.depth})"

class FurnitureFactory:
    def MakeArmchair(self):
        pass

    def MakeCoffeeTable(self):
        pass

    def MakeSofa(self):
        pass

class RetroFurnitureFactory(FurnitureFactory):
    def MakeArmchair(self):
        return Armchair("Brown", 80, 90, 70)

    def MakeCoffeeTable(self):
        return CoffeeTable("Red", 120, 40, 60)

    def MakeSofa(self):
        return Sofa("Blue", 200, 100, 90)


if __name__ == "__main__":
    retro_factory = RetroFurnitureFactory()

    armchair = retro_factory.MakeArmchair()
    coffee_table = retro_factory.MakeCoffeeTable()
    sofa = retro_factory.MakeSofa()

    print(armchair.ToString())
    print(coffee_table.ToString())
    print(sofa.ToString())
