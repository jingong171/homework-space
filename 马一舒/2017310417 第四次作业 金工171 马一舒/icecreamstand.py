from restuarant import Restuarant
 
class IceCreamStand(Restuarant):
    """创建一家冰淇淋店"""
    def __init__(self,restuarant_name,cuisine_type):
        """初始化调用父类属性"""
        super().__init__(restuarant_name,cuisine_type)
        self.flavors= "chocolate"
    def describe_flavor(self):
        """描述冰淇淋的口味"""
        print("The flavor of this ice-cream is "+ str(self.flavors) +".")

print("\n")
my_icecream=IceCreamStand('apple','dessert shop')
print(my_icecream.describe_restuarant())
my_icecream.describe_flavor()

