import typing
#1===================REmove duplicates from a list==================
def remove_duplicates(lst: list[int]) -> list[int]:
    return list(set(lst))

#2===================Count Occurrences of Each Word in a Sentence===========
def word_count(s: str) -> dict[str, int]:
    d={}
    l=s.split()
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1    
    return d

#3===============Find Common Elements in Two Lists==============================
def common_elements(a: list[int], b: list[int]) -> list[int]:
    return list(set(a)&set(b))

#4===================Merge Two Dictionaries====================================
def merge_dicts(d1: dict, d2: dict) -> dict:
    for i,j in d2.items():
        if i not in d1:
            d1[i]=j
    return d1

#5====================Convert List of Tuples to Dictionary==========================
def tuple_to_dict(pairs: list[tuple[str, int]]) -> dict[str, int]:
    d={}
    for i in pairs:
        d[i[0]]=i[1]
    return d



#==============================programming testing===============================
print(remove_duplicates([5,5,6,5,3,2,6,3,2]))
print(word_count("Hi arun , how are you arun"))
print(common_elements([2,3,4,5,6,7],[1,2,3,4,56,6]))
print(merge_dicts({'a':3,'b':4,'c':5},{'a':3,'e':6,'f':8}))
print(tuple_to_dict([("asd",3),("sdf",5),("hjg",7)]))



#===================================================================================================
  
#=================================optimize solutions===================================
#def remove_duplicates(lst: list[int]) -> list[int]:
#    return list(dict.fromkeys(lst))  # Maintains original order

#from collections import Counter

#def word_count(s: str) -> dict[str, int]:
#    return dict(Counter(s.split()))
#def common_elements(a: list[int], b: list[int]) -> list[int]:
 #   return list(set(a).intersection(b))  # Better readability
#def merge_dicts(d1: dict, d2: dict) -> dict:
 #   return {**d2, **d1}  # d1 has priority, d2 values only if key not in d1
#def tuple_to_dict(pairs: list[tuple[str, int]]) -> dict[str, int]:
 #   return dict(pairs)  # Direct conversion

