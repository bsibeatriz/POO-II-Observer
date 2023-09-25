# Classe Drink (interface)
class Drink:
    def get_nome(self):
        pass

    def get_preco(self):
        pass

# Classe DrinkDecorator (abstrata)
class DrinkDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

    def get_nome(self):
        return self.drink.get_nome()

    def get_preco(self):
        return self.drink.get_preco()

# Classe DrinkBase (implementação concreta)
class DrinkBase(Drink):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco_base

# Exemplo de Uso
caipira = DrinkBase("Caipira", 20.0)
print(f"Drink: {caipira.get_nome()}, Preço: R${caipira.get_preco()}")

caipira_personalizada = DrinkDecorator(DrinkDecorator(DrinkDecorator(DrinkDecorator(caipira, "Saquê"), "Abacaxi"), "Kiwi"), "Açúcar")
print(f"Drink Personalizado: {caipira_personalizada.get_nome()}, Preço: R${caipira_personalizada.get_preco()}")
