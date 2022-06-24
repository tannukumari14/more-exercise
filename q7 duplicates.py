# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# f=[]
# i=0
# while i<len(string_list):
#     if string_list[i] not in f:
#         f.append(string_list[i])
#     i=i+1
# print(f)

# string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# i=0
# b=[]
# while i<len(string_list):
#     if string_list[i] not in b:
#         b.append(string_list[i])
#     i=i+1
# print(b)

# string_list = ["Empathy", "Empathy", "Kindness", "Kindness", 
# "Compassion", "Humble", "Humble"]
# i=0
# b=[]
# while i<len(string_list):
#     if string_list[i] not in b:
#         b.append(string_list[i])
#     i=i+1
# print(b)

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
b=[]
while i<len(list1):
    if list1[i] not in list2:
        b.append(list1[i]) 
    else:
        b.append(list1[i])
    i=i+1
print(b)


