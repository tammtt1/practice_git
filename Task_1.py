import math
class Triangle:
    try:
        def __init__(self,a,b,c):
            self.a = a
            self.b = b
            self.c = c
        def peremeter_triangle(self):
            P=(self.a+self.b+self.c)/2
            return P
        def area_triangle(self):
            S= math.sqrt((self.a+self.b+self.c)/2*((self.a+self.b+self.c)/2-self.a)
                         *((self.a+self.b+self.c)/2-self.b)*((self.a+self.b+self.c)/2-self.c))
            return S
    except: Exception
def main():
    try:
        a = int(input("Nhap canh a:"))
        b= int(input("Nhap canh b: "))
        c= int(input("Nhap canh c: "))
        new_trangle = Triangle(a,b,c)
        print("P = {}".format(new_trangle.peremeter_triangle()))
        print(("S = {}".format(new_trangle.area_triangle())))
    except: Exception
if __name__ == '__main__':
    main()
