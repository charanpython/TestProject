

# sorted dictionary based on key and value are in two ways...

# deatails = {'name':342,'age':21,'branch':4233,'id':11}

# import operator
# example = {1:3,4:7,3:2,6:4,4:5,8:2,7:1}
# new = sorted(example.items(),key = operator.itemgetter(0))
# print(new)

# another = sorted(deatails.items(),key=lambda d:d[1])
# print(another)

#------------------------------------------------------------------------

# add a new element to a existing dictionary

# example = {'name':'charan','age':23,'branch':'ece'}
# example.update({'subject':['cs','vlsi','m3']})
# print(example)


#--------------------------------------------------------------------------

#concatenate two or more dictionaries into a new dictionary

# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# dic4 = {}
# 
# for k in (dic1,dic2,dic3):
#     dic4.update(k)
# print(dic4)


# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# 
# 
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


#------------------------------------------------------------------

# enquiring or verifying a key in a dictionary
#

#dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if 9 in dic:
#     print('key found')
# else:
#     print('not found')

# def key_verification(x):
#     if x in dic:
#         print('key found in dictionary')
#     else:
#         print('key not found')
# key_verification(4)
# key_verification(9)

#----------------------------------------------------------------------
#dict with keys and values as squares of keys
# dic = {}
# for k in range(1,6):
#     dic[k] = k*k
# print(dic)


# def square(n):
#     dic = {}
#     for k in range(1,n+1):
#         dic[k] = k*k
#     return dic
# print(square(5))

#---------------------------------------------------------------------------
#merging two dictionaries
        
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40}
# dic3 = {5:50,6:60,2:30}
# dic4 = {**dic1,**dic2,**dic3}
# print(dic4)

# dic4 = {}
# for k in (dic1,dic2,dic3):
#     dic4.update(k)
# print(dic4)

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# dic=dic1.copy()
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

#---------------------------------------------------------
# iterating over dictionaries
# d = {1: 10, 2: 30, 3: 30, 4: 40, 5: 50, 6: 60}
# for dic_key,dic_values in d.items():
#     print(dic_key,'--->',dic_values)


 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40}
# dic3 = {5:50,6:60,2:30}
# 
# for k in (dic1,dic2,dic3):
#     print(k)

# for k in d:
#     sum += k
# print(sum)

# for k in d.values():
#     sum += k
# print(sum)



# d.clear()
# print(d)

# list1 = ['a','b','c','d','e','f']
# list2 = [1,2,3,4,5]
# dictionary = dict(zip(list1,list2))
# print(dictionary)


# dic = {3: 10, 1: 20, 2: 30, 6: 40, 5: 50, 4: 60}
# 
# maximum = max(sorted(dic.values()))
# minimum = min(sorted(dic.values()))
# print(maximum)
# print(minimum)

# class dictObj:
#      def __init__(self):
#          self.x = 'red'
#          self.y = 'Yellow'
#          self.z = 'Green'
#      def do_nothing(self):
#          pass
# test = dictObj()
# print(test.__dict__)

# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }
# 
# result = {}
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)


# d = {1:2}
# if not bool(d):
#     print('this is an empty dictionary')
# else:
#     print(d)

#A = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# res = set(k for dict in A for k in dict.values())
# print(res)

# B = []
# for dict in A:
#     for value in dict.values():
#         B.append(value)
# print(set(B))


# def f(*args,**kwargs):
#     print(args,kwargs)



# def f2(arg1,arg2,*args,**kwargs):
#     print(arg1,arg2,args,kwargs)
# 
# l = [1,2,3]
# t = (4,5,6)
# d = {'a':1,'b':2,'c':3}
# 
# f2(1,2,3)
# f2(1,2,3,**d)
# f2(1,2,3,*l,*t,**d)
# f2(1,2,**d)
# 
# f2(*t,*l)
# f2(1,2,3,a=1,c=2,b=2,z='hi')
# f2(a=1,b=2,c=3)

# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# print(A0)
# print(A1)
# print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)

import re

# with open('E:\\charan\\my photos\\ed.txt') as f:
#     contents = f.read()
#     pattern = re.compile(r'^[a-z]+')
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# text = 'The quick brown fox jumps over the lazy dog.'
# result = re.finditer(r'(fox|dog|horse)',text)
# for k in result:
#     print(k.group(0))
#     
    

def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))

    
    
    
    
    
    
    
    
    
    



















































    






























    








































 







