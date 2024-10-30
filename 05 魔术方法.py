"""
演示魔术方法
"""

# 1.
class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
    def __str__(self):
        return f"Student类对象，name={self.name},age={self.age},tel={self.tel}"
student=Student("zhou",32,"181652999")
print(student)
print(str(student))         #假设没有__str__函数，则会输出如下的结果（内存地址） 有这个函数，
                            #输出了字符串

# 2.__lt__
class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
    def __lt__(self, other):
        return self.age < other.age # 这里比较的是两个数字 所以可以正常使用<符号
stu1=Student("zhou",32,"181652999")
stu2=Student("long",36,"181652489")
print(stu1<stu2)
print(stu1>stu2)