# -*- coding:utf-8 -*-
import time
from Tkinter import *
import random
a = []
for i in range(6):##随机数生成
    a.append(random.randint(0, 100))
class CanvasDemo():
    #n1=70
    #n2=n1+40
    d1=390
    d2=d1-60
    weiyi=len(a)
    def __init__(self):

        n1=70
        n2=n1+40
        window=Tk()
        window.title("冒泡排序演示")
        self.canvas=Canvas(window,width=500,height=400,bg='white')##设置画布大小，颜色
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
        ##self.paixu()
        self.displayRect()
        self.n1=n1+60
        self.n2=n2+60
        btString=Button(frame,text="执行",command=self.paixu1)
        btString.grid(row=1,column=6)
        window.mainloop()


    def displayRect(self):##打印表格
        self.canvas.create_rectangle(60,30,420,90,tags="rect")##左上右下
        self.canvas.create_rectangle(120,30,360,90,tags="rect")
        self.canvas.create_rectangle(180,30,300,90,tags="rect")
        self.canvas.create_rectangle(240,30,240,90, tags="rect")
    def paixu1(self):      
        for i in range(0,len(a)):
            j=len(a)-1##添加交换之前
            self.weiyi=len(a)-1
            while j>i:
                self.displayString2()
                time.sleep(1)
                #if j>i:
                 #   self.canvas.delete("int")
                    
                ##self.weiyi=len(a)-1
                self.displayString3()
                time.sleep(1)
                if a[j-1]>a[j]:
                    a[j-1],a[j]=a[j],a[j-1]
                #j=j-1
                self.displayString4()
                if j>=i:
                    self.canvas.delete("int")
                self.displayString1()##打印交换之后的
                time.sleep(1)
                
                if j>=i:
                    self.canvas.delete("int")
                j=j-1
            self.displayString1()
                
                
        
    def displayLine(self):## 设置箭头指向
        self.canvas.create_line(self.n2,30,self.n2,10,self.n2+60,10,self.n2+60,30,width=1,arrow="last",tags="line")

    def displayString1(self):## 打印序列
        n1=90
        ##time.sleep(1)
        
        for z in range(len(a)):
            self.canvas.create_text(n1,60,text="%s"%a[z],font="Times 20 bold ",tags="int")
            n1=n1+60
        self.canvas.update()
        #self.update()
        #time.sleep(0.5)

    def displayString2(self):
        n2=90
        
        for z in range(len(a)):
            if z!=self.weiyi and z!=self.weiyi-1:
                self.canvas.create_text(n2,60,text="%s"%a[z],font="Times 20 bold ",tags="int")
            n2=n2+60
        
        self.weiyi=self.weiyi-1
        self.canvas.update()
    def displayString3(self):
        n2=90
        for z in range(len(a)):
            if z==self.weiyi:
                if a[z]>a[z+1]:
                    self.canvas.create_line(n2,30,n2,10,n2+60,10,n2+60,30,width=1,arrow="last",tags="line")
                self.canvas.create_text(n2,60,text="%s"%a[z],font="Times 20 bold ",tags="int1")
                self.canvas.create_text(n2+60,60,text="%s"%a[z+1],font="Times 20 bold",tags="int1")
                for x in range(0,10):
                    self.canvas.move("int1",0,20)
                    self.canvas.update()
                    time.sleep(0.1)
                    if(x==9):
                        self.canvas.delete("int1")
            n2=n2+60
        self.canvas.update()
    def displayString4(self):
        n2=90
        for z in range(len(a)):
            if z==self.weiyi:
                self.canvas.create_text(n2,300,text="%s"%a[z],font="Times 20 bold ",tags="int2")
                self.canvas.create_text(n2+60,300,text="%s"%a[z+1],font="Times 20 bold ",tags="int2")
                for x in range(0,10):
                    self.canvas.move("int2",0,-20)
                    self.canvas.update()
                    time.sleep(0.1)
                    if(x==9):
                        self.canvas.delete("int2","line")
            n2=n2+60

CanvasDemo()
