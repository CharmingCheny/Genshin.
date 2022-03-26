#原神抽奖模拟器
import random
s1=[] #五星
s2=[] #四星
s3=[1,2] #保底五星记录
i1=0 #记录五星
i2=0#记录四星
p=[]#记录抽奖类容
I=0

while 1:
    i=0#记录单发随机数
    a=int(input("请选择单发还是十连：(1 or 10)"))
    
#单发情况
    if a==1:
        I+=1
        i1+=1
        i2+=1
    #记录五星概率
        if I>0 and I<=40:
            while i<6:
                b=random.randint(1,1000)
                if  b not in s1:
                    s1.append(b)
                    i+=1
        elif I>40 and I<=60:
            while i<20:
                b=random.randint(1,1000)
                if  b not in s1:
                    s1.append(b)
                    i+=1
        elif I>60 and I<=70:
            while i<80:
                b=random.randint(1,1000)
                if  b not in s1:
                    s1.append(b)
                    i+=1
        elif I>70 and I<=90:
            while i<100:
                b=random.randint(1,1000)
                if  b not in s1:
                    s1.append(b)
                    i+=1
        i=0
    #记录四星概率
        while i<50:
            b=random.randint(1,1000)
            if  b not in s2:
                s2.append(b)
                i+=1
        d=random.randint(1,1000)
        
    #五星保底机制
        if i1==90:
            e=random.randint(1,2) 
            if e  not in s3:
                e=1
                s3=[1,2]
            if e==1:
                print("五星:甘雨")
                print("恭喜你，第90发出金！")
            else:
                s3.clear()
                s3.append(1)
                h=random.randint(1,6)
                if h==1:
                    print("五星:迪卢克")
                    print("恭喜你，第90发出金！")
                elif h==2 or h==6:
                    print("五星:刻晴")
                    print("恭喜你，第90发出金！")
                elif h==3:
                    print("五星:七七")
                    print("恭喜你，第90发出金！")
                elif h==4:
                    print("五星:琴")
                    print("恭喜你，第90发出金！")
                elif h==5:
                    print("五星:莫娜")
                    print("恭喜你，第90发出金！")
            i1=0
            i2=0
            I=0
    #四星保底机制
        elif i2==10:
            g=random.randint(1,2)
            if g not in s3:
                g=1
                s3=[1,2]
            if g==1:
                h=random.randint(1,3)
                if h==1:
                    print("四星:行秋")
                elif h==2:
                    print("四星:北斗")
                elif h==3:
                    print("四星:烟绯")
            else:
                s3.clear()
                s3.append(1)
                h=random.randint(1,33)
                if h==1:
                    print("四星:云堇")
                if h==2:
                    print("四星:重云")
                if h==3:
                    print("四星:凝光")
                if h==4:
                    print("四星:九条裟罗")
                if h==5:
                    print("四星:早柚")
                if h==6:
                    print("四星:托马")
                if h==7:
                    print("四星:罗莎莉亚")
                if h==8:
                    print("四星:辛焱")
                if h==9:
                    print("四星:砂糖")
                if h==10:
                    print("四星:迪奥娜")
                if h==11:
                    print("四星:诺艾尔")
                if h==12:
                    print("四星:班尼特")
                if h==13:
                    print("四星:菲谢尔")
                if h==14:
                    print("四星:香菱")
                if h==15:
                    print("四星:雷泽")
                if h==16:
                    print("四星:弓藏")
                if h==17:
                    print("四星:祭礼弓")
                if h==18:
                    print("四星:绝弦")
                if h==19:
                    print("四星:西风猎弓")
                if h==20:
                    print("四星:昭心")
                if h==21:
                    print("四星:祭礼残章")
                if h==22:
                    print("四星:流浪乐章")
                if h==23:
                    print("四星:西风秘典")
                if h==24:
                    print("四星:西风长枪")
                if h==25:
                    print("四星:匣里灭辰")
                if h==26:
                    print("四星:雨裁")
                if h==27:
                    print("四星:祭礼大剑")
                if h==28:
                    print("四星:钟剑")
                if h==29:
                    print("四星:西风大剑")
                if h==30:
                    print("四星:匣里龙吟")
                if h==31:
                    print("四星:祭礼剑")
                if h==32:
                    print("四星:笛剑")
                if h==33:
                    print("四星:西风剑")
            i2=0
             
    #不到保底中奖
        else:
    #五星
            if d in s1:
                e=random.randint(1,2)
                if e  not in s3:
                    e=1
                    s3=[1,2]
                if e==1:
                    print("五星:甘雨")
                    print("恭喜你，第%d发出金！" % I)
                else:
                    s3.clear()
                    s3.append(1)
                    h=random.randint(1,6)
                    if h==1:
                        print("五星:迪卢克")
                        print("恭喜你，第%d发出金！" % I)
                    elif h==2 or h==6:
                        print("五星:刻晴")
                        print("恭喜你，第%d发出金！" % I)
                    elif h==3:
                        print("五星:七七")
                        print("恭喜你，第%d发出金！" % I)
                    elif h==4:
                        print("五星:琴")
                        print("恭喜你，第%d发出金！" % I)
                    elif h==5:
                        print("五星:莫娜")
                        print("恭喜你，第%d发出金！" % I)
                i1=0
                i2=0
                I=0
        #四星
            elif d in s2:
                g=random.randint(1,2)
                if g not in s3:
                    g=1
                    s3=[1,2]
                if g==1:
                    h=random.randint(1,3)
                    if h==1:
                        print("四星:行秋")
                    elif h==2:
                        print("四星:北斗")
                    elif h==3:
                        print("四星:烟绯")
                else:
                    s3.clear()
                    s3.append(1)
                    h=random.randint(1,33)
                    if h==1:
                        print("四星:云堇")
                    if h==2:
                        print("四星:重云")
                    if h==3:
                        print("四星:凝光")
                    if h==4:
                        print("四星:九条裟罗")
                    if h==5:
                        print("四星:早柚")
                    if h==6:
                        print("四星:托马")
                    if h==7:
                        print("四星:罗莎莉亚")
                    if h==8:
                        print("四星:辛焱")
                    if h==9:
                        print("四星:砂糖")
                    if h==10:
                        print("四星:迪奥娜")
                    if h==11:
                        print("四星:诺艾尔")
                    if h==12:
                        print("四星:班尼特")
                    if h==13:
                        print("四星:菲谢尔")
                    if h==14:
                        print("四星:香菱")
                    if h==15:
                        print("四星:雷泽")
                    if h==16:
                        print("四星:弓藏")
                    if h==17:
                        print("四星:祭礼弓")
                    if h==18:
                        print("四星:绝弦")
                    if h==19:
                        print("四星:西风猎弓")
                    if h==20:
                        print("四星:昭心")
                    if h==21:
                        print("四星:祭礼残章")
                    if h==22:
                        print("四星:流浪乐章")
                    if h==23:
                        print("四星:西风秘典")
                    if h==24:
                        print("四星:西风长枪")
                    if h==25:
                        print("四星:匣里灭辰")
                    if h==26:
                        print("四星:雨裁")
                    if h==27:
                        print("四星:祭礼大剑")
                    if h==28:
                        print("四星:钟剑")
                    if h==29:
                        print("四星:西风大剑")
                    if h==30:
                        print("四星:匣里龙吟")
                    if h==31:
                        print("四星:祭礼剑")
                    if h==32:
                        print("四星:笛剑")
                    if h==33:
                        print("四星:西风剑")
                i2=0
        #三星
            else:
                    h=random.randint(1,13)
                    if h==1:
                        print("三星:弹弓")
                    if h==2:
                        print("三星:神射手之誓")
                    if h==3:
                        print("三星:鸦羽弓")
                    if h==4:
                        print("三星:翡玉法球")
                    if h==5:
                        print("三星:讨龙英杰谭")
                    if h==6:
                        print("三星:魔导绪论")
                    if h==7:
                        print("三星:黑缨枪")
                    if h==8:
                        print("三星:以理服人")
                    if h==9:
                        print("三星:沐浴龙血的剑")
                    if h==10:
                        print("三星:铁影阔剑")
                    if h==11:
                        print("三星:飞天御剑")
                    if h==12:
                        print("三星:黎明神剑")
                    if h==13:
                        print("三星:冷刃")
        s1.clear()
        s2.clear()

        
#十连情况
    elif a==10:
        n=0  #记录10连次数
        while n<10:
            i1+=1
            i2+=1
            I+=1
    #记录五星概率
            if I>0 and I<=40:
                while i<6:
                    b=random.randint(1,1000)
                    if  b not in s1:
                        s1.append(b)
                        i+=1
            elif I>40 and I<=60:
                while i<20:
                    b=random.randint(1,1000)
                    if  b not in s1:
                        s1.append(b)
                        i+=1
            elif I>60 and I<=70:
                while i<80:
                    b=random.randint(1,1000)
                    if  b not in s1:
                        s1.append(b)
                        i+=1
            elif I>70 and I<=90:
                while i<200:
                    b=random.randint(1,1000)
                    if  b not in s1:
                        s1.append(b)
                        i+=1
            i=0
    #记录四星概率
            while i<50:
                b=random.randint(1,1000)
                if b not in s2:
                    s2.append(b)
                    i+=1
            d=random.randint(1,1000)
            
    #五星保底机制
            if i1==90:
                e=random.randint(1,2)
                if e  not in s3:
                    e=1
                    s3=[1,2]
                if e==1:
                    print("五星:甘雨")
                    print("恭喜你，第90发出金！")
                else:
                    s3.clear()
                    s3.append(1)
                    f=random.randint(1,6)
                    if f==1:
                        print("五星:迪卢克")
                        print("恭喜你，第90发出金！")
                    elif f==2 or f==6:
                        print("五星:刻晴")
                        print("恭喜你，第90发出金！")
                    elif f==3:
                        print("五星:七七")
                        print("恭喜你，第90发出金！")
                    elif f==4:
                        print("五星:琴")
                        print("恭喜你，第90发出金！")
                    elif f==5:
                        print("五星:莫娜")
                        print("恭喜你，第90发出金！")
                i1=0
                i2=0
                I=0
        #四星保底机制
            elif i2==10:
                g=random.randint(1,2)
                if g not in s3:
                    g=1
                    s3=[1,2]
                if g==1:
                    h=random.randint(1,3)
                    if h==1:
                        print("四星:行秋")
                    elif h==2:
                        print("四星:北斗")
                    elif h==3:
                        print("四星:烟绯")
                else:
                    s3.clear()
                    s3.append(1)
                    h=random.randint(1,33)
                    if h==1:
                        print("四星:云堇")
                    if h==2:
                        print("四星:重云")
                    if h==3:
                        print("四星:凝光")
                    if h==4:
                        print("四星:九条裟罗")
                    if h==5:
                        print("四星:早柚")
                    if h==6:
                        print("四星:托马")
                    if h==7:
                        print("四星:罗莎莉亚")
                    if h==8:
                        print("四星:辛焱")
                    if h==9:
                        print("四星:砂糖")
                    if h==10:
                        print("四星:迪奥娜")
                    if h==11:
                        print("四星:诺艾尔")
                    if h==12:
                        print("四星:班尼特")
                    if h==13:
                        print("四星:菲谢尔")
                    if h==14:
                        print("四星:香菱")
                    if h==15:
                        print("四星:雷泽")
                    if h==16:
                        print("四星:弓藏")
                    if h==17:
                        print("四星:祭礼弓")
                    if h==18:
                        print("四星:绝弦")
                    if h==19:
                        print("四星:西风猎弓")
                    if h==20:
                        print("四星:昭心")
                    if h==21:
                        print("四星:祭礼残章")
                    if h==22:
                        print("四星:流浪乐章")
                    if h==23:
                        print("四星:西风秘典")
                    if h==24:
                        print("四星:西风长枪")
                    if h==25:
                        print("四星:匣里灭辰")
                    if h==26:
                        print("四星:雨裁")
                    if h==27:
                        print("四星:祭礼大剑")
                    if h==28:
                        print("四星:钟剑")
                    if h==29:
                        print("四星:西风大剑")
                    if h==30:
                        print("四星:匣里龙吟")
                    if h==31:
                        print("四星:祭礼剑")
                    if h==32:
                        print("四星:笛剑")
                    if h==33:
                        print("四星:西风剑")
                i2=0
                
        #不到保底中奖
            else:
        #五星
                if d in s1:
                    e=random.randint(1,2)
                    if e  not in s3:
                        e=1
                        s3=[1,2]
                    if e==1:
                        print("五星:甘雨")
                        print("恭喜你，第%d发出金！" % I)
                    else:
                        s3.clear()
                        s3.append(1)
                        f=random.randint(1,4)
                        if f==1:
                            print("五星:迪卢克")
                            print("恭喜你，第%d发出金！" % I)
                        elif f==2:
                            print("五星:刻晴")
                            print("恭喜你，第%d发出金！" % I)
                        elif f==3:
                            print("五星:七七")
                            print("恭喜你，第%d发出金！" % I)
                        elif f==4:
                            print("五星:琴")
                            print("恭喜你，第%d发出金！" % I)
                        elif f==5:
                            print("五星:莫娜")
                            print("恭喜你，第%d发出金！" % I)
                    i1=0
                    i2=0
                    I=0
            #四星
                elif d in s2:
                    g=random.randint(1,2)
                    if g not in s3:
                        g=1
                        s3=[1,2]
                    if g==1:
                        h=random.randint(1,3)
                        if h==1:
                            print("四星:行秋")
                        elif h==2:
                            print("四星:北斗")
                        elif h==3:
                            print("四星:烟绯")
                    else:
                        s3.clear()
                        s3.append(1)
                        h=random.randint(1,33)
                        if h==1:
                            print("四星:云堇")
                        if h==2:
                            print("四星:重云")
                        if h==3:
                            print("四星:凝光")
                        if h==4:
                            print("四星:九条裟罗")
                        if h==5:
                            print("四星:早柚")
                        if h==6:
                            print("四星:托马")
                        if h==7:
                            print("四星:罗莎莉亚")
                        if h==8:
                            print("四星:辛焱")
                        if h==9:
                            print("四星:砂糖")
                        if h==10:
                            print("四星:迪奥娜")
                        if h==11:
                            print("四星:诺艾尔")
                        if h==12:
                            print("四星:班尼特")
                        if h==13:
                            print("四星:菲谢尔")
                        if h==14:
                            print("四星:香菱")
                        if h==15:
                            print("四星:雷泽")
                        if h==16:
                            print("四星:弓藏")
                        if h==17:
                            print("四星:祭礼弓")
                        if h==18:
                            print("四星:绝弦")
                        if h==19:
                            print("四星:西风猎弓")
                        if h==20:
                            print("四星:昭心")
                        if h==21:
                            print("四星:祭礼残章")
                        if h==22:
                            print("四星:流浪乐章")
                        if h==23:
                            print("四星:西风秘典")
                        if h==24:
                            print("四星:西风长枪")
                        if h==25:
                            print("四星:匣里灭辰")
                        if h==26:
                            print("四星:雨裁")
                        if h==27:
                            print("四星:祭礼大剑")
                        if h==28:
                            print("四星:钟剑")
                        if h==29:
                            print("四星:西风大剑")
                        if h==30:
                            print("四星:匣里龙吟")
                        if h==31:
                            print("四星:祭礼剑")
                        if h==32:
                            print("四星:笛剑")
                        if h==33:
                            print("四星:西风剑")
                    i2=0
            #三星
                else:
                    h=random.randint(1,13)
                    if h==1:
                        print("三星:弹弓")
                    if h==2:
                        print("三星:神射手之誓")
                    if h==3:
                        print("三星:鸦羽弓")
                    if h==4:
                        print("三星:翡玉法球")
                    if h==5:
                        print("三星:讨龙英杰谭")
                    if h==6:
                        print("三星:魔导绪论")
                    if h==7:
                        print("三星:黑缨枪")
                    if h==8:
                        print("三星:以理服人")
                    if h==9:
                        print("三星:沐浴龙血的剑")
                    if h==10:
                        print("三星:铁影阔剑")
                    if h==11:
                        print("三星:飞天御剑")
                    if h==12:
                        print("三星:黎明神剑")
                    if h==13:
                        print("三星:冷刃")
            s1.clear()
            s2.clear()
            n+=1
        print('\n')
    else:
        print("输入错误，请重新输入！")
                    
