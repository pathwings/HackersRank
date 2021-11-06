# #A set is an unordered collection of elements without duplicate entries.
# #Basically, sets are used for membership testing and eliminating duplicate entries.
# print (set([1,2,1,2,3,4,5,6,0,9,12,13,14]))
# print (set({'Hacker' : 'DOSHI', 'Rank' : 616 }))

########### map function
#
# def myfunc(a, b):
#   return a + b #string concate
#
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
#
# print(x) #printing map object
#
# #convert the map into a list, for readability:
# print(list(x))

###################### main problem ###############################

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input()) ##input 1
    print(f"number of input is {n}")
    arr1 =map(int, input().split())  ##input 2--created map object  #map syntex-- map(function, iterables)
#""""function- Required. The function to execute for each item
 #   iterable- Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable."""
    print(f"Input arr1 is {arr1}")  ## converting map object into list
    arr=list(arr1) ##
    print(f"number of array{arr}")
    result = average(arr)
    print(f"the result is {result}")

#I/p
#10
#161 182 161 154 176 170 167 171 170 174
