"""
演示面向对象类中的成员方法定义和使用
"""
# 定义一个带有成员方法的类
class Student:
    name=None

    def say_hi(self):
        print(f"大家好啊，我是{self.name},很高兴认识大家")
    def say_hello(self,msg):   # 个性化打招呼方式
        print(f"大家好，我是：{self.name},{msg}")

stu=Student()
stu.name="周杰伦"
stu.say_hi()  # 调用的时候就当作不存在
stu2=Student()
stu2.name="哥哥"
stu2.say_hello("我是大傻逼")  # 调用的时候就当作不存在