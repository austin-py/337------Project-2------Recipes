import nltk
data = ['    ½ green bell pepper, finely chopped    ', '    1 (4.5 ounce) can mushrooms    ', '    2 (7 ounce) packages shirataki noodles, drained    ', '    1 (12 ounce) package tofu, cut into chunks    ', '    ½ cup lemon juice    ', '    2 eggs    ', '    ½ cup chopped cashews, divided    ', '    1 cup bean sprouts    ', '    1  jar sausage flavored spaghetti sauce    ', '    1 teaspoon dried oregano    ', '    3 cups Burgundy wine    ', '    3 tablespoons all-purpose flour    ', '    2 eggs, beaten (Optional)   ', '    1 (1 ounce) square semisweet chocolate    ']
for x in data:
    y = list(filter(('').__ne__, x.split(' ')))
    z = ' '.join(y)
    print(z)
    text = nltk.word_tokenize(z)
    pos_tagged = nltk.pos_tag(text)
    print(pos_tagged)
    name = ''
    for tpl in pos_tagged:
        if tpl[1] == 'NN' or tpl[1] == 'JJ' or tpl[1] == 'NNS' or tpl[1] == 'VB' or tpl[1] == 'NNP':
            if name == '':
                name += f'{tpl[0]}'
            else:
                name += f' {tpl[0]}'
    print(name)
    print('\n')

'''
#clean: ',', '(', ')', '(Optional)'
print(y[0][0])
z = '    1 (4.5 ounce) can mushrooms    '
print(list(filter(('').__ne__, z.split(' '))))
'''