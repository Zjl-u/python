a_list=[1,2,3,4,5]
b_list=a_list[0:2:]
b_list.reverse()
c_list=a_list[2::]
c_list.reverse()
b_list.extend(c_list)
print(b_list)