import random
import os
print("猜数字，从1000到9999")
correctanswer = random.randint(1000, 9999)
answerset = {str(correctanswer)[0], str(correctanswer)[1], str(correctanswer)[2], str(correctanswer)[3]}
numbers = {"1","2","3","4","5","6","7","8","9","0"}
matchcount = 0
for i in range(1, 16):
    inputanswer = input("请输入答案（你还有"+str(16-i)+"次机会）：")
    for j in inputanswer:
        if j not in numbers:
            print("你输入了一个非法的字符！请立即停止！")
            break
        elif int(inputanswer)<1000:
            print("你输入的不是四位数！重来！")
            break
        else:
            a2 = str(inputanswer)[0]
            b2 = str(inputanswer)[1]
            c2 = str(inputanswer)[2]
            d2 = str(inputanswer)[3]
            if a2 in answerset:
                matchcount += 1
            if b2 in answerset:
                matchcount += 1
            if c2 in answerset:
                matchcount += 1
            if d2 in answerset:
                matchcount += 1    
            if int(inputanswer) == correctanswer:
                print("正确！你只用了", i, "次就猜出了正确答案！")
                break
            if int(inputanswer) > correctanswer:
                print("你的答案太大了！你输入的答案中，有",matchcount,"个数字与正确答案相同")
                matchcount = 0
                break
            if int(inputanswer) < correctanswer:
                print("你的答案太小了！你输入的答案中，有",matchcount,"个数字与正确答案相同")
                matchcount = 0
                break
if i == 15 and inputanswer != str(correctanswer):
    print("失败，你太菜了！")
os.system('pause')
