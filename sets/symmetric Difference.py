#
# a=input()
# lis=a.split()
# print(lis) ##PRINT STRING TYPE OF VALIUES
# new_lis=list(map(int,lis)) #CONVERT STRING TO INT
# print(new_lis)

#input
M=int(input())
m=input()
N=int(input())
n=input()

#splitting and mapping(string to int_list)
x=list(map(int,m.split()))
y=list(map(int,n.split()))

#creation of sets
a=set(x)
b=set(y)

#difference in each sets
c=a.difference(b)
d=b.difference(a)
#print(c)
#print(d)

#union of difference
e=c.union(d) #differencet sets ko single set mein merge kiya hai
#print(e)
#converting set to a list
result=list(e)  #set ko list mein convert kara hai
#print(result)
#sorting
result.sort() #list ko sort kar diya hai

#iteration
for i in range(len(result)):
    print(result[i])

