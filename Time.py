import time

exp = time.asctime( time.localtime(time.time()))
def show():
    print(exp)
    return 2

show()


class filler:
    def __init__(self):
        self.x = "mr. X"
        self.y = exp
        self.z = show()
        print("class filler in console")
        
ob = filler()
print(ob.x,ob.y,ob.z)
