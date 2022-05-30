class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.steps = []

    def print_recipe(self):
        res = ''
        res += 'Recipe for {}:\n'.format(self.name)
        res += '   Ingredients:\n'
        for i in self.ingredients:
            res += '      '
            res += '{} {} {} {}, {}'.format(str(i.quantity), i.measurement, i.descriptor, i.name, i.preparation)
            res += '\n'

        res += '   Tools:\n'
        for t in self.tools:
            res += '      '
            res += t
            res += '\n'

        res += '   Methods:\n'
        for m in self.methods:
            res += '      '
            res += m
            res += '\n'

        res += '   Steps:\n'
        for s in self.steps:
            res += '      '
            res += 'Step {}: '.format(str(s.step_number))
            res += s.description
            res += '\n'

        print(res)
        return res

class Ingredient:
    def __init__(self, name):
        self.name = name
        self.quantity = 0
        self.measurement = ''
        self.descriptor = ''
        self.preparation = ''

class Step:
    def __init__(self, number):
        self.step_number = 0
        self.ingredients = []
        self.tools = []
        self.methods = []
        self.time = 0
        self.description = ''

def main():
    recipe1 = Recipe('Omellete')

    ingredient1 = Ingredient('Eggs')
    ingredient1.quantity = 4
    ingredient1.descriptor = 'fresh'
    ingredient1.preparation = 'cleaned'
    recipe1.ingredients.append(ingredient1)

    ingredient2 = Ingredient('Olive oil')
    ingredient2.quantity = 1
    ingredient2.measurement = 'table spoon'
    ingredient2.descriptor = 'uncooked'
    recipe1.ingredients.append(ingredient2)

    recipe1.tools = ['Whisk', 'Bowl', 'Pan', 'Spatula']
    recipe1.methods = ['Fry', 'Whisking']

    step1 = Step(1)
    step1.description = 'Crack the eggs into the bowl. Whisking for 2 minutes until mixed'
    step2 = Step(2)
    step2.description = 'Put 1 table spoon of olive oils into the pan. Put the whisked eggs from the bowl to the pan. Cook for 5 minutes.'
    recipe1.steps = [step1, step2]

    recipe1.print_recipe()


if __name__ == '__main__':
    main()