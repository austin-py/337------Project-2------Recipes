class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.steps = []

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.quantity = 0
        self.measurement = ''
        self.descriptor = ''
        self.preparation = ''

class Step:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.time = 0