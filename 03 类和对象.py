"""
yanshi
"""
from IPython.utils.timing import clock
# 设计一个闹钟类
class Clock:
    id =None
    price =None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id="003032"
clock1.price=29.99
print(f"闹钟ID是{clock1.id}，闹钟价格是{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id="323032"
clock2.price=21.66
print(f"闹钟ID是{clock2.id}，闹钟价格是{clock2.price}")
clock2.ring()
# 想构建多少个对象都可以，