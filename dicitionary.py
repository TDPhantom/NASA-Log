from collections import Counter
import matplotlib.pyplot as plt


fruits = [
    'apples', 'apples', 'apples',
    'bananas', 'bananas','bananas' ,
    'oranges', 'oranges', 'oranges',
    'pear' , 'pear', 'pear' ,'pear'
 ]



fruit_counter = Counter(fruits)

newDict = dict()
for (key, value) in fruit_counter.items():
    if value % 2 :
        newDict[key] = value


print(newDict)


print(fruit_counter.keys)
print(fruit_counter.values)

plt.bar(newDict.keys(), newDict.values()) 

plt.show()









# dct ={'pear': 4, 'apples': 3, 'bananas': 3, 'oranges': 3}

# lst = [4,3,2,1]

# print (dct)