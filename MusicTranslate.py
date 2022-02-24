# 原神风花之羽琴 up主键盘谱转换为分3行的简谱
# 现在的是阿瑠之歌，括号里是一起按的

ori = """
（1 +3）5 +3 5 +3 5 +3 +4
（-7 +3）5 +3 5 +3 5 +1 +2
（-6 +3） 5 +3 5 +3 5 +4 +5
（-5 +5） 5 +4 5 +3 5 +2
（-4 +1） 5 +1 5 +1 5 +2 
（-3 +1） 5 +1 5 +1 5 +5
（-2 +1） 5 +1 +2 +3 +2 +3 +2 +1 5
（-5 +1） 5 +1 +2 +3 +2 +3 +2 +1 +2"""  # 雪山

"""(-3+1) +5 (-4+5) +4+3(-5+2)+1+2+3 (-6+1) 5
(-4+1) +2(-3+1) (-2+1)+2+3+4(-5+2)

(1+1)5(+3+5) (-7+5)5(+2+4)+3
(-6+2)(3+1)(6+2)+3 (-55)2 5
(-4+1)(15)3 +2(-3+1)13
(-2+1)(-6+2)(2+3)+4 (-524+2) (-5-72)

(-61)3(6+1) (-57)2 5
(-46)1(35)4 (-35)13
(-46)1(47)+1 (-35)-51
(-22)-4-63 (-5-72)

(-61)3(6+1) (-57)2 5
(-46)1(35)4 (-35)13 -5
(-21)(-42)(-63)4 (-5-72) 1
(-114)-5(13)2 3

1+1) +5 (-7+5) +4+3(-6+2)+1+2+3 (-5+1) 5
(-4+1) +2(-3+1) (-2+1)+2+3+4(-5+2)
(-1+1)-5(3+5) (-5-7+5) (-52+4)+3
(-4+2)(1+1)(5+2)+3 (-3-5-7+1) 5
(-2+1)-62 +3(-5-72+2) +1
(-1+1)-5 2 4 (-1-513)
"""

line1 = ""
line2 = ""
line3 = ""

spaceflag = 0
bracketflag = 0
flag = ""
line1flag = 0
line2flag = 0
line3flag = 0

spacechar = '-'

for w in ori:
    if w in ' \n\t':
        continue
    if w == '(' or w == '（':
        bracketflag = 1
        continue
    if w == ')' or w == '）':
        bracketflag = 0
    if w in "+-":
        flag = w
        # print("+++")
        continue

    if w in "1234567":
        if flag == "+":
            line1 += w
            line1flag += 1
        if flag == "":
            line2 += w
            line2flag += 1
        if flag == "-":
            # print("---")
            line3 += w
            line3flag += 1
        flag = ""
    if bracketflag == 0:
        while line1flag > 0:
            if line2flag > 0:
                line2flag -= 1
            else:
                line2 += spacechar
            if line3flag > 0:
                line3flag -= 1
            else:
                line3 += spacechar
            line1flag -= 1

        while line2flag > 0:
            if line1flag > 0:
                line1flag -= 1
            else:
                line1 += spacechar
            if line3flag > 0:
                line3flag -= 1
            else:
                line3 += spacechar
            line2flag -= 1
        while line3flag > 0:
            if line1flag > 0:
                line1flag -= 1
            else:
                line1 += spacechar
            if line2flag > 0:
                line2flag -= 1
            else:
                line2 += spacechar
            line3flag -= 1
        line1 += " "
        line2 += " "
        line3 += " "

print(line1)
print(line2)
print(line3)
# print()
