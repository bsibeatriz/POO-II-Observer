class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Criando o objeto')
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.exception_queue = []
        return cls._instance

    def log_exception(self, exception):
        self.exception_queue.append(exception)

    def get_exceptions(self):
        return self.exception_queue


class SingletonDriver:
    @staticmethod
    def run():
        logger1 = Logger()
        logger2 = Logger()

        
        print(logger1 is logger2)  

        
        logger1.log_exception("Exceção 1")
        logger2.log_exception("Exceção 2")

        
        print(logger1.get_exceptions())  
        print(logger2.get_exceptions()) 


SingletonDriver.run()
