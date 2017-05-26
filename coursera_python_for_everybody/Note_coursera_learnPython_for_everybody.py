# return vs. print
def greet(lang):
    if lang == 'es':
        print 'hola'
    elif lang == 'fr':
        print 'bonjour'
    else:
        print 'hello'

greet('es')

def greet(lang):
    if lang =='es':
        return 'hola'
    elif lang =='fr':
        return 'bonjour'
    else:
        return 'hello'

print greet('fr')

# find the minimum number in loop, using None if we don't know what numbers in the list
smallest = None
print 'before'
for value in [9, 41, 5.16, 1]:
    if smallest is None:   # happen at the very first. When there's no number exist, the first value is the smallest
        smallest = value
    elif value < smallest:
        smallest = value
    print 'smallest', smallest

print 'after', smallest

# "is" is stronger than "==", should only be using checking special operator "True", "False"