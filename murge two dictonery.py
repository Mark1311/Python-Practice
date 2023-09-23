dict1 = {"name": 1, "Fname": 2}
dict2 = {"boss": 100, "gost": 215}

#1st Solution

print(dict1 | dict2)

#Solution 2nd

print({**dict1, **dict2})

#Solution 3rd

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)