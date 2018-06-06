'''
Created on May 31, 2018

@author: Charan
'''
#1
# def sum_lists(items):
#     sum_number = 0
#     for k in items:
#         sum_number += k 
#     return sum_number
# print(sum_lists([1,2,3,4,-6]))

#2
# def product_lists(items):
#     product_value = 1
#     for k in items:
#         product_value *= k 
#     return product_value
# print(product_lists([1,2,3,4,-4]))
#3
# def maxim_value(items):
#     max = items[0]
#     for k in items[1:]:
#         if k>max:
#             max = k 
#         else:
#             pass
#     return max
# print(maxim_value([21,332,3,5436,65236,234233])) 

#4
# def minimum_value(items):
#     min = items[0]
#     for q in items[1:]:
#         if q<min:
#             min = q
#         else:
#             pass
#     return min
# print(minimum_value([-2343,23,23,423,345,-32]))  
#5
# def same_elements(items):
#     count = 0
#     for item in items:
#         if len(item)>2 and item[0]==item[-1]:
#             count += 1
#     return count
# print(same_elements(['aba', 'xyz', 'aba', '1221','charanc']))

#6
# def sorting_lists(items):
#     res = sorted(items,key=lambda x:x[1])
#     return res
# print(sorting_lists([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7
# def duplicates_remove(items):
#     empty = []
#     for item in items:
#         if item not in empty:
#             empty.append(item)
#     return set(empty)
# print(duplicates_remove([1,3,22,4,33,34,2,13,33,22,1,4]))

#8
# l = []
# if len(l) == 0:
#     print()

#10
# def words_length(text):
#     list = []
#     n = int(input('enter a number'))
#     data = text.split()
#     for word in data:
#         if len(word)>n:
#             list.append(word)
#     return list
# print(words_length("The quick brown fox jumps over the lazy dog"))

#11
# def compare_lists(list1,list2):
#     for k in list1:
#         for l in list2:
#             if l == k:
#                 return True
#     return False
# print(compare_lists([1,3,6,8],[4,6,2,9,7]))

#12
# items = ['apple','banana','carrot','dall','egg']
# result = [item for (i,item) in enumerate(items) if i not in (0,3,4)]
# print(result)


#14
# result = [item for item in [0,1,2,3,4,5,6,7,8] if item%2 != 0]
# print(result)






#19
# def differ(list1,list2):
#     li = []
#     for i in list1:
#         if i not in list2:
#             li.append(i)
#         else:
#             for k in list2:
#                 if k not in list1:
#                     li.append(k)
#     return li    
# print(differ([1,3,6,8],[4,6,2,9,7]))

# def count_in_range(list,x,y):
#     count = 0
#     for k in list:
#         if x<=k<=y:
#             count += 1
#     return count
# print(count_in_range([12,15,21,32,45,64,344,34,53,23], 16,53))

# def verifying(list):
#     for item in list:
#         if type(item) == 'list':
#             return True
# print(verifying([1,3,2,45,[12,43,53],33,'fd']))
 
def sub_lists(list):
    subs = [[]]
    for i in range(len(list)):
        n = i+1
        while n <= len(list):
            subs.append(list[i:n])
            n += 1 
    return subs
print(sub_lists([10,20,30,40,50]))












