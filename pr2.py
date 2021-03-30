def max_length_number(arr: list):
    unique_arr = set(map(lambda x : x[0], arr))
    final_arr = sorted([max(filter(lambda x : i in x, arr)) for i in unique])
    return [(i,len(i)) for i in final_arr]
    
arr1 = ["cc","cccc","aa","dd","dddddddd"]
arr2 = ["pp","pppp","ssssssssss","ss"]
arr3 = ["fff","f","ffffff","ffffffff","e","eeee","eeeeeeeee"]

print(max_length_number(arr1))
print(max_length_number(arr2))
print(max_length_number(arr3))
