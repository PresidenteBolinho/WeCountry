from Models.Entidade import Entidade
from Models.Comida import Comida

class Planta(Entidade, Comida):
    def __init__(self, temFruta, venenosa):
        self.temFruta = temFruta
        self.venenosa = venenosa

    temFruta = bool
    venenosa = bool