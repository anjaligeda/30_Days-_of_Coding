phonebook = dict() #Declare a dictionary
for _ in range(int(input())):
    key, value = input().split()
    
    phonebook[key] = value

#Trick - If there is no more input stop the program
try:
    # Code for query intake
    queries = []
    while True:
        line = input()
        if line == "":
            break
        queries.append(line)
except Exception:
    pass

# Code for query result
for i in range(0, len(queries)):
    if(queries[i] in phonebook):
        print(queries[i] + "=" + phonebook[queries[i]])
        # print(f"{queries[i]}={phonebook[queries[i]]}")
    else:
        print("Not found")
  
'''INPUT:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
OUTPUT:
am=99912222
Not found
harry=12299933'''
