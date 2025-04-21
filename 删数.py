Num=eval(input())
a_list=[]
b_list=[]
for i in str(Num):
    a_list.append(int(i))
first_min=a_list[0]
first_num=0
for i in range(5):
    if first_min>a_list[i]:
        first_min=a_list[i]
        first_num=i
b_list.append(first_min)
second_min=a_list[first_num+1]
for i in range(first_num+1,6):
    if second_min>a_list[i]:
        second_min=a_list[i]
b_list.append(second_min)
print(b_list)