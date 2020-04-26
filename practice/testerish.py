print('penney lane')
n = [1,2,3,4]
print (n)
n.append(5)
print(n)



#def function

#change to test branch "test"


def function1():
    print_words('whateverr')


#strings and Lists

#.find for strings, .index for lists

age = '16'
name = 'megan'

list= [name, age]
':'.join(list)


#booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


first_name = 'megan'
last_name = 'gillen'

# Join the variables with a '_'
full_name = first_name + last_name
print(full_name)



# Capitalize first letters
full_name.title()

age = 16



# Lists

''' # Create a list that contains the `full_name` and `age` variables
my_list = [full_name, age]

# print the index for `age`
print(my_list.index(age))

seclist = ['bob', 20]
my_list.append(seclist)
print(my_list)

my_list.extend(seclist)
print(my_list)

del my_list[2:]
print(my_list) '''


#tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#turn lists (or other type?) into tuple
print(tuple(my_list))

#in keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#for loop
fruits = ["apple", "banana", "cherry"]
for t in fruits:
  print(t)

for x in "banana":
  print(x)

#sets
aset = {"the", "cat"}
print("the" in aset)

for x in aset:
    print(x)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#or
set1.update(set2)
print(set1)


#dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"]

thisdict["year"] = 2018
print(thisdict)


#nested dictionary

nestdict = {
    "first" : {"one":"uno" , "two":"dos",},
    "second" : {"three":"tres" , "four":"cuatro"}
}

nestdict['first']['two']

nestdict['second']['five'] = ['cinco']
print(nestdict)
nestdict['second']
nestdict['second']['four']


#Conditionals
def foo(word, adict):

    if word in adict.keys():
        print('In the if')
    elif word in adict.values():
        print('In the elif')
    else:
        print('In the else')

    print('The if is over')
