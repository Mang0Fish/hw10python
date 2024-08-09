#1
ilDict = {'name':"Israel", 'birth':1948, 'population_millions':9.3, 'capital':"Jerusalem", 'language':"Hebrew", 'cities':["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion" ,"Petah Tikva", "Ashdod"], 'currency':"ILS", 'area_kilometer':22145, 'gdp_billion':450}
print(ilDict.get('capital'))
print(ilDict.keys())
keysCap = [i.upper() for i in ilDict.keys()]
print(keysCap)
print(ilDict.values())
valuesLen = [len(str(i)) for i in ilDict.values()]
print(valuesLen)
print(ilDict.items())
ilDict2 = ilDict.copy()
ilDict2.clear()
ilDict3 = ilDict.fromkeys(ilDict.keys())
print(ilDict3)
del ilDict3['currency']
print(ilDict3.pop('area_kilometer'))
ilDict3.update({"national_sport":"Soccer", "population_millions":9.4})

#2
def performAction(action):
    actions = {'add':'adding item', 'delete':'deleting item', 'update':'updating item','_':'unknown action'}
    return actions.get(action)
    
print(performAction("add"))

#3
def getStats(numbers: list[int]) ->dict:
    return {'sum':sum(numbers), "biggest number":max(numbers), "Smallest number":min(numbers), "list's length":len(numbers), "list's average":sum(numbers)/len(numbers)}
   
print(getStats([2,7,2,4,8,2,3,0,15,6,3]))

#4 bonus
operDict = {'lower':lambda x:x.lower(), 'upper':lambda x:x.upper(), 'len':lambda x:len(x), 'reverse':lambda x:x[::-1]}
word = input("Enter a word")
action = input('Enter operation name (lower, upper, len, reverse): ')
print(operDict.get(action)(word))

#5
def removeKeyFromDict(dictionary: dict):
    dictionary.popitem()
def clear_all(dictionary :dict):
    dictionary = {}

a = {'x': 1, 'y': 2}
removeKeyFromDict(a)
print(a)
#It will change because popitems removes the last item of the dict
clear_all(a)
print(a)
#It will not work because the dictionary points at another location in the memory and not changing the dict itself
#You can clear a dict in a function by using the clear method

#6
#The dict is mutable and because of that we can access and change values in the dict with the square brackets,
#for example, in coordinates = { 'x': 10, 'y': 20 }, coordinates['x'] will differ to its value: 10,
#we can change the key's value like in a list (coordinates['x'] = 15)
#and contrary to a list, we can even add items to the dict with the brackets (coordinates['z'] = 30)

#7
countries = [ {'name': 'Israel', 'population': 9.3, 'birth': 1948}, 
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan', 
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901}, 
{'name': 'Canada', 'population': 38.0, 'birth': 1867} ]
print(list(filter(lambda x: x['population'] > 30, countries)))
print(list(filter(lambda x: x['birth'] > 1800, countries)))
print(list(map(lambda x: x['name'], countries)))
print(list(map(lambda x: x['birth'], countries)))
print(sorted(countries, key=lambda x:x["birth"]))
print(sorted(countries, key=lambda x:x["population"]))
