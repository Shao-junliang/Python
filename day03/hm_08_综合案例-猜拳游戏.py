import random
"""
1.出拳：
    玩家出拳
    电脑出拳
2.判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""
# 1.出拳
# 玩家
player = int(input("请出拳(0--石头；1--剪刀；2--布)："))
# 电脑
computer = random.randint(0,2)

# 2.判断输赢
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print(f"电脑出拳为{computer}，玩家获胜")
elif player == computer:
    print(f"电脑出拳为{computer}，平局")
else:
    print(f"电脑出拳为{computer}，电脑获胜")




