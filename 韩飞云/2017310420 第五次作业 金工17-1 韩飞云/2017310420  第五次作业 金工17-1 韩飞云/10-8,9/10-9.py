filename1="dogs.txt"
filename2="cats.txt"

try:#按列输出dogs
    with open(filename1,'r')as file1_obj:
       print("dogs里面有：")
       for line in file1_obj:
           print(line.rstrip())
except FileNotFoundError:
    pass

    

try:#按列输出cats
    with open(filename2,'r')as file2_obj:
        print("\ncats里面有：")
        for line in file2_obj:
            print(line.rstrip())
except FileNotFoundError:
    pass

