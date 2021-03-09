from Models.Entidade import Entidade


#classe Terra e suas propriedades
class Terra(Entidade):
    """
        Definição das propriedades da Terra
    """
    def __init__(self, nutrientes, tipo, minerais):
        self.nutrientes = nutrientes
        self.tipo = tipo
        self.minerais = minerais

    nutrientes = str
    tipo = str
    minerais = str