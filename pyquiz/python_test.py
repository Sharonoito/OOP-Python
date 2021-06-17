x=[100,110,120,130,140,150]
y=[a for a in x]
y=x*5
print(y)

def divisible_by_three(n):
    number=range(1,n)
    for x in number:
        if x%3==0:
            print(x)

(divisible_by_three(100))

# x=[[1,2],[3,4][5,6]]
# y=[]

def smallest(numbers):
    
    min=numbers[0]
    for i in numbers:
        if i<min:
            min=i
    return min 
print(smallest([2,70,5,9]))

def duplicate():
    x=["a","b","a","e","d","b","c","e","f","g","h"]
    x=list(set(x))
    print(x)

duplicate()

def divisible_by_seven():
    num=range(100,200)
    for y in num:
        if y%7==0:
            print(y)

divisible_by_seven()

# def greetings():
#     students=[{"age":19,"name":"Eunice","age":21,"name":"Agnes","age":18,"name":"Teresa"}]
#     s1=students["age":19,"name":"Eunice"]
#     s2=students["age":21,"name":"Agness"]
#     s3=students["age":18,"name":"Teresa"]
# print (f"Hello {name},you were born in the year {2020}-{age}") 

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self,area):
        self.width=10
        self.length=20
        area=self.width*self.length

    print(area)  

    def perimeter(self,perimeter):
        self.width=10
        self.length=20
        perimeter=2(self.length+self.width)
    print(perimeter)    



        
   
