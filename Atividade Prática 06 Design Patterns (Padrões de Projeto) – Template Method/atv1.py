class StringTransformer:
    def read_string(self, input_string):
        self.string = input_string

    def transform_string(self):
        pass

    def print_string(self):
        print(self.string)

    def process_string(self, input_string):
        self.read_string(input_string)
        self.transform_string()
        self.print_string()

class UpperCaseStringTransformer(StringTransformer):
    def transform_string(self):
        self.string = self.string.upper()

class LowerCaseStringTransformer(StringTransformer):
    def transform_string(self):
        self.string = self.string.lower()

class ReverseStringTransformer(StringTransformer):
    def transform_string(self):
        self.string = self.string[::-1]


input_string = "Olá, Mundo!"

upper_case_transformer = UpperCaseStringTransformer()
upper_case_transformer.process_string(input_string)  

lower_case_transformer = LowerCaseStringTransformer()
lower_case_transformer.process_string(input_string)  

reverse_transformer = ReverseStringTransformer()
reverse_transformer.process_string(input_string)  
