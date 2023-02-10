def find_index(arr1, arr2):
    for i in arr1:
        if i in arr2:
            print(i, ":", arr2.index(i))
        else:
            print(i, ": NA")

arr1 = ['a','b','c','d']
arr2 = ['p','q','a','d']
find_index(arr1, arr2)
