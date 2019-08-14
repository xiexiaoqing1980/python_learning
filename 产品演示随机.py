import random

a=input()
a_list=["欧阳经纶","吴小兵","徐杰","魏向阳","丁振华","于成刚","范朝华","刘浩","许诺","杨柳"]
b_list=random.sample(a_list,len(a_list))
print("输出",a)