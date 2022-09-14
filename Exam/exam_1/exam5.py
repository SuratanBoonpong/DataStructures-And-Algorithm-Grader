
class MyInt:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        ans = self.val + other.val
        ans += (self.val + other.val)/2
        ans = int(ans)
        return ans
    def toRoman(self):
        num = self.val
        d4 = ["","M","MM","MMM","MMMM","MMMMM"]
        d3 = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        d2 = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        d1 = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        dd4 = d4[num//1000]
        dd3 = d3[(num%1000)//100]
        dd2 = d2[(num%100)//10]
        dd1 = d1[num%10]
        ans = (dd4+dd3+dd2+dd1)
        return ans

print(" *** class MyInt ***")
num1,num2 = input("Enter 2 number : ").split()
a = MyInt(int(num1))
b = MyInt(int(num2))
print(str(num1)+" convert to Roman : "+a.toRoman())
print(str(num2)+" convert to Roman : "+b.toRoman())
print(num1+" + "+num2+" = "+str(a+b))