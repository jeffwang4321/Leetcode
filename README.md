# Leetcode

- Organizing my Leetcode solutions and notes in one repository 

### Running Solution
`$ python3 [filename]`


### Review Notes

List manipulation
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

