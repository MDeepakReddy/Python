import collections
# name = "Deepak"
# age = 24
"""print("Hai {} you turned {}".format(name,age))
print(f"Hai {name} you turned {age}")
print("Hai %s you turned %s"%(name,age))
print("Hai "+name+" you turned "+str(age))"""

# if elif else

"""
location = "hyderabad"
if location == "chennai":
    print("the location is chennai")
elif location == "hyderabad":
    print("the location is Hyderabad")
else:
    print("invalid location")
"""

# for loop with continue statement
"""
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
"""

# while loop with break statement
# can also use pass statement
"""
val = 1
while val < 6:
    print(val)
    val += 1
    if val == 5:
        break
"""

# function creation with return statement
"""
def test_para(x, y=2):  # default argument y=2 should always on the last of all arguments
    ans = x ** y
    return ans


sol = test_para(10)
print(sol)
"""


# function with variable arguments * for non kywrded and ** for kywrded
"""
def test_args(*args):
    for arg in args:
        print("arg: {}".format(arg))


test_args(1, 2, 3, 4, 4)
"""

# sequence examples
"""
Name = "Mr Deepak Reddy "
print(Name)
print(Name[0:2])
print(Name[3:9])
print(Name*2)
print(len(Name))
print(Name.upper())
print(Name.lower())
"""
# collection as  Dictionary
"""
stdlist = {'suman':'20','raj':'25','mohan':'19'}
stdlist['suman']=45
stdlist['john']=50
print(stdlist)
"""

# collection as set
"""
a={1,5,4,2,6,8,4}
a.add(9)
print(a)  #duplicates are not printed
c=frozenset({1,2,6})
c.add(9)  #frozenset cannot be edited
print(c)
"""

# collections counter
"""
c=collections.Counter(['a','b','a','v','r','r','h','e','i','s','a','i'])
print(c)
print(c.elements())
print(c.most_common())

a=collections.Counter('abcd')
b=collections.Counter('aaabb')
print(a-b)
print(a+b)
"""

dq=collections.deque(['a','b','a','v','r','r','h','e','i','s','a','i'])
dq.append('g')
print(dq)
dq.appendleft('f')
print(dq)
dq.append('k')
print(dq)
dq.pop()
dq.popleft()
print(dq)
dq.extend('agf')
print(dq)
dq.rotate(2)
print(dq)

# default_dictionaries

scores = [('deepak',84),('vinay',73),('goutham',81)]
# namedtuple
# ordereddict

