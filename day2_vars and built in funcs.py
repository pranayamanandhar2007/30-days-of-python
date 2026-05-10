string1 = "this is a string"
string2 = "this is another string"

length = len(string1)
print("string 1: ", string1, "\n so this is a string of len", length)

arr = [string1,string2]
arrlen =[]

for i in arr:
    j = len(i)
    print(j)
    arrlen.append(j)

print("the minium size string is of len" , min(arrlen))

num_int1,num_int2 = 1,8
num_int3 = num_int1 + num_int2
str_int1 = str(num_int1)
str_int2 = str(num_int2)
str_int3 = str_int1 +  str_int2
print('num_int is: ',num_int3)
print('str_int is: ',str_int3)

