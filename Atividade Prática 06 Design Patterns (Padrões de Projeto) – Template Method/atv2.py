class PhoneOrderTemplate:
    def select_phone(self):
        pass

    def pack_phone(self):
        pass

    def make_payment(self):
        pass

    def deliver_phone(self):
        pass

    def process_order(self):
        self.select_phone()
        self.pack_phone()
        self.make_payment()
        self.deliver_phone()

class OnlineStore(PhoneOrderTemplate):
    def select_phone(self):
        print("Selecionando telefone no site da loja online.")

    def pack_phone(self):
        print("Embalando telefone para envio.")

    def make_payment(self):
        print("Pagamento online realizado.")

    def deliver_phone(self):
        print("Telefone entregue no endereço fornecido.")

class OfflineStore(PhoneOrderTemplate):
    def select_phone(self):
        print("Selecionando telefone na loja física.")

    def pack_phone(self):
        print("Embalando telefone na loja.")

    def make_payment(self):
        print("Pagamento realizado na loja.")

    def deliver_phone(self):
        print("Telefone entregue em mãos.")

print("Comprando telefone online:")
online_store = OnlineStore()
online_store.process_order()

print("\nComprando telefone offline:")
offline_store = OfflineStore()
offline_store.process_order()
