"""
不定⻓参数：不定⻓参数也叫可变参数。⽤于不确定调⽤的时候会传递多少个参数(不传参也可以)的场景。
此时，可⽤包裹(packing)位置参数，或者包裹关键字参数，来进⾏参数传递，会显得⾮常⽅便。
注意：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为⼀个元组(tuple)，args是元组类型，这就是包裹位置传递。
综上：⽆论是包裹位置传递还是包裹关键字传递，都是⼀个组包的过程。
"""


# 包裹关键字传递
def user_info2(**kwargs):
    print(kwargs)

j
user_info2()
user_info2(name='TOM')
user_info2(name='TOM', age=20)
user_info2(name='TOM', age=20, gender='男')
