# Classe IObserver
class IObserver:
    def update(self, noticias):
        pass

# Classe Observer
class Observer(IObserver):
    def __init__(self, nome):
        self.nome = nome

    def update(self, noticias):
        print(f"{self.nome} está transmitindo notícia de última hora: {noticias}")

# Classe IObservable
class IObservable:
    def subscribe(self, observador):
        pass

    def unsubscribe(self, observador):
        pass

    def notify(self, noticias):
        pass

# Classe Subject
class Subject(IObservable):
    def __init__(self):
        self.observadores = []
        self.noticias = ""

    def subscribe(self, observador):
        self.observadores.append(observador)

    def unsubscribe(self, observador):
        self.observadores.remove(observador)

    def notify(self):
        for observador in self.observadores:
            observador.update(self.noticias)

    def set_noticias(self, noticias):
        self.noticias = noticias
        self.notify()

# Exemplo de Uso
reuters = Subject()

fox_news = Observer("Fox News")
cnn = Observer("CNN")

reuters.subscribe(fox_news)
reuters.subscribe(cnn)

reuters.set_noticias("Atenção: Notícia de última hora!")

#end

