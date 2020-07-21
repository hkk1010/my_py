#! /usr/bin/python
# coding:utf-8

class user():

    user_name=''
    password='12345'
    def __init__(self,newusername,newpassword):
        self.user_name=newusername
        self.password=newpassword
    def toString(self):
        print ("名字:",self.user_name,"密码：",self.password)

objectUser=[]
menu=["1.显示全部已注册用户","2.查找/修改/删除用户信息","3.添加新用户","4.退出系统"]
flag=1
while(flag):
    print("\n用户注册信息管理系统")
    for m in menu:
     print(m)

    num=input("请输入序号选择对应菜单：")
    num=num.split(".")
    askforNum=int(num[0])
    #1.显示全部已注册用户
    if(askforNum==1):
        for num1 in objectUser:
            num1.toString()
    elif(askforNum==2):
        finduser=input("输入要查找的用户：")
        flag2=0
        for num2 in objectUser:
            print(num2.newUser)
            exit()
            if(num2.newUser==finduser):
                flag2=1
                print("该用户已经注册了")
                print("请选择操作\n")
                ww=print("1.修改用户\n2.删除用户\n")
                aa=input("请输入你的选择:")
                if(aa=="1"):
                    temp2Name=input("请输入新的用户名：")
                    temp2Passwd = input("请输入新的密码:")
                    num2.userName = temp2Name
                    num2.passwd = temp2Passwd
                    break
                if(aa=="2"):
                    objectUser.remove(num2)
                    break
            if(flag2==0):
                print("该用户不存在")
    #添加新用户
    elif(askforNum==3):
        newUser=input("请输入新用户名：")
        newPass=input("请输入新用户名密码：")
        tempuser=user(newUser,newPass)
        objectUser.append(tempuser)
        print("已成功添加用户")
    #退出系统
    elif(askforNum==4):
        flag=0
        print("已退出系统")
        break
    else:
        print("输入的格式不对")
