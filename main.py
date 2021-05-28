listb=[]
listc=[]
print('Number display program')
val = input("Enter the number of lines: ")

val = int(val)
value = val
for i in range(val):
    listb=[]
    value = val
    counter = val-i-1
#    print(counter)
    for y in range(counter):
        listb.append("")
    while value > counter:
        listb.append(value)
        value-=1
#    print(listb)
    listc.append(listb)
#     val-=1
for line in listc:
     print(('{:>3}'*val).format(*line))
