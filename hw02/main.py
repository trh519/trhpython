#绘制五星红旗，编写者为天津工业大学信息1601田润昊，时间2018年10月4日
#国旗的大小规格为660*440

from turtle import *
speed(4)
color('red')
begin_fill()

#画出五星红旗的红色旗面

penup()        #将画笔移至国旗的一个顶点
setx(-330)   
sety(220)
pendown()

fd(660)        #旗面，规格为660*440，原点在中心
right(90)
fd(440)
right(90)
fd(660)
right(90)
fd(440)

end_fill()


#定义星星函数
def xingxing(a,b,r,d,e):
    #绘制五星
    #参数的含义：
    #五星中心的横坐标  a
    #五星中心的纵坐标  b
    #五星外接圆的半径  r
    #五星中一个顶点与相隔的一个顶点的顶点之间的直线距离  d
    #四颗小五星画笔箭头从中心向东需要转动的角度   e
    
    penup()             #将画笔移至五星的中心
    setx(a)
    sety(b)
    setheading(e)       #将画笔的箭头转动相应的角度
    fd(r)               #将画笔移至五星的一角     
    pendown()

    color('yellow')     #填充颜色为黄色

    begin_fill()

    left(162)
    fd(d)

    left(144)
    fd(d)

    left(144)
    fd(d)

    left(144)
    fd(d)

    left(144)
    fd(d)

    end_fill()

    return()


#画星星
xingxing(-220,110,66,131.34,90)        #大星星
xingxing(-110,176,22,43.78,210.964)    #第一个小星星
xingxing(-66,132,22,43.78,188.1297)    #第二个小星星
xingxing(-66,66,22,43.78,164.055)      #第三个小星星
xingxing(-110,22,22,43.78,141.34)      #第四个小星星


done()
