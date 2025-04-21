b_list=input()
a_list=[]
for i in b_list.split(','):
    a_list.append(i)
a_list.reverse()
print(a_list)