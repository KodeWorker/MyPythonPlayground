import pickle
from Player import Player

items = ['axe', 'sword', 'gun']

myObject = Player(1, 'Jeff', 100, items)
print(myObject)

with open('save2.pkl', 'wb') as outfile:
    pickle.dump(myObject, outfile, pickle.HIGHEST_PROTOCOL)
    
print('----------------------------------------------------------------------')

newObject = None

with open('save2.pkl', 'rb') as infile:
    newObject = pickle.load(infile)

print(newObject)