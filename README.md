# Leetcode

- Organizing my Leetcode solutions and notes in one repository 

### Running Solution
`$ python3 [filename]`


### Review Notes

List
```
arr = [i for i in range(5)]
print(arr)
# [0, 1, 2, 3, 4]

print(arr[1:3])
# [1, 2]

arr.append(7)
print(arr)
# [0, 1, 2, 3, 4, 7]

arr.remove(7)
print(arr)
# [0, 1, 2, 3, 4]

print(arr.pop(1))
# 1
print(arr)
# [0, 2, 3, 4]

arr.insert(1, 1)
print(arr)
# [0, 1, 2, 3, 4]

arr += [5, 6] # arr.extend([5, 6])
print(arr)
# [0, 1, 2, 3, 4, 5, 6]

arr = [-1] + arr 
print(arr)
# [-1, 0, 1, 2, 3, 4, 5, 6]
```
set() 
```
hashSet = set()
print(hashSet)
# set()
print(len(hashSet))
# 0

arr = [i for i in range(5)]
print(arr)
# [0, 1, 2, 3, 4]

arrSet = set(arr)
print(arrSet)
# {0, 1, 2, 3, 4}

arrSet.add(5)
print(arrSet)
# {0, 1, 2, 3, 4, 5}
arrSet.remove(4)
print(arrSet)
# {0, 1, 2, 3, 5}

arrSet.add(5) # No Error
print(arrSet)
# {0, 1, 2, 3, 5} # No change

print(5 in arrSet) 
# True
print(6 in arrSet) 
# False
```
Hashmap 
```
hash1 = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
hash2 = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
print(len(hash1)) # print(len(hash2))
# 5
hash3 = {}
print(len(hash3))
# 3

print(hash1 == hash2)
# True
print(hash1['a'])
# 3
print(hash1.get('a'))
# 3

print(hash1['z'])
# KeyError: 'z'
print(hash1.get('z')) # No Error
# None
print(hash1.get('z', 0)) # if None then 0 else hash1['z']
# 0
```
Boolean Logic
```
print(0 == True)
# False
print(1 == True)
# True

print(not 0)
# True
print(not 1)
# False

list = []
print(list)
# []
print(not list)
# True

list2 = [0, 1]
print(list2)
# [0, 1]
print(not list2)
# False
```

