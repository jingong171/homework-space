import json
fav_number=input("What's your favorate number?\n")#将用户输入的数值存储到变量里
try:
    number=eval(fav_number)#尝试将输入的数据转化为数字
except NameError:
    print("Please enter a number.")#转化错误报错
else:
    filename='fav_number.json'
    with open(filename,'w') as f_obj:#创建用于存储数值的文件
        json.dump(number,f_obj)#存储数值到文件里
