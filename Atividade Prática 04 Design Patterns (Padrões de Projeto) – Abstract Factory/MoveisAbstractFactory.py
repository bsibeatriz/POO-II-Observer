class Móveis:
    def criar_cadeira(self):
        pass

    def criar_mesa(self):
        pass

    def criar_sofá(self):
        pass

    def criar_poltrona(self):
        pass

    def criar_luminária(self):
        pass

class MóveisClássicos(Móveis):
    def criar_cadeira(self):
        return CadeiraClássica()

    def criar_mesa(self):
        return MesaClássica()

    def criar_sofá(self):
        return SofáClássico()

    def criar_poltrona(self):
        return PoltronaClássica()

    def criar_luminária(self):
        return LumináriaClássica()


class MóveisContemporâneos(Móveis):
    def criar_cadeira(self):
        return CadeiraContemporânea()

    def criar_mesa(self):
        return MesaContemporânea()

    def criar_sofá(self):
        return SofáContemporâneo()

    def criar_poltrona(self):
        return PoltronaContemporânea()

    def criar_luminária(self):
        return LumináriaContemporânea()


class CadeiraClássica:
    pass

class MesaClássica:
    pass

class SofáClássico:
    pass

class PoltronaClássica:
    pass

class LumináriaClássica:
    pass

class CadeiraContemporânea:
    pass

class MesaContemporânea:
    pass

class SofáContemporâneo:
    pass

class PoltronaContemporânea:
    pass

class LumináriaContemporânea:
    pass
