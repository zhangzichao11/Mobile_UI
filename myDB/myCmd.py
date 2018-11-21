import Mydb
import cmd
import sys
import md_logger
class Client(cmd.Cmd):

    def __init(self):
        cmd.Cmd.__init__(self)

    @staticmethod
    def do_hello(arg):
        print("do_hello", arg)

    @staticmethod
    def do_exit():
        sys.exit()

    do_EOF = do_exit

if __name__ == "__main__":
   #如果按错数字,继续要求输入
    mylog=md_logger.logger()
    while True:
        # noinspection PyBroadException
        try:
            number = int(input("查询请按:1  修改请按:2\n删除请按:3  退出程序请按:4\n"))
            client = Client()
            #如果选择了1，走查询模块
            if number == 1:
                #如果查询模块里面的选项选择错误,可以继续选择
                while True:
                    # noinspection PyBroadException
                    try:
                        userId = int(input("请输入您要查找music哪个包:\n"))
                        # 输入错误次数的统计
                        count = 0
                        #查询成功后，是否继续查询标志位
                        isReturn = False
                        #如果输入id有误,要求重新输入,,如果错误达到3次,退出循环,从新走查询模块
                        # noinspection PyTypeChecker
                        Mydb.MysqldbHelper.queryId(Mydb.MysqldbHelper, userId)
                        #如果选择有误,继续选择
                        while True:
                            # noinspection PyBroadException
                            try:
                                kp= int(input("继续查询,请按:1    退回上级查询模块请按:2\n"))
                                #查询成功后,如果选择1,退出该选择模块,返回输入id模块,继续进行输入查询
                                #如果选择2,也退出该选择模块,并根据标志是否退出,并设置是否退出输入模块的标志
                                if kp == 1:
                                    break
                                elif kp == 2:
                                    isReturn = True
                                    break
                                else:print("您选择有误,请重新输入您的选择!")
                            except:print("您选择有误,请重新输入您的选择!")
                    except Exception as e:
                        print("错误信息",e)
                        # noinspection PyUnboundLocalVariable
                        count= count + 1
                        if int(count)==3:
                            print("输入已经连续错误3次,请重新选择!\n")
                            break;
                        else:
                            mylog.error("输入信息有误 %s", e)
                            print("输入有误,请重新输入!")
                    #如果为真,退出输入模块,返回查询模块
                    if isReturn:
                        break
            #如果按4退出该查询模块,继续走总模块流程
            elif number == 4:
                break
            #如果选择2,走修改模块
            elif number == 2:
            #输入错误次数的统计
                count=0
                while True:
                    # noinspection PyBroadException
                    try:
                        userId=int(input("输入要修改music哪个包:\n"))
                        numberId = int(input("请输入最新的版本号:\n"))
                        # noinspection PyCallByClass,PyTypeChecker
                        Mydb.MysqldbHelper.change(Mydb.MysqldbHelper,userId , numberId)
                        #修改执行完成后,退出修改模块
                        break
                    except Exception as e:
                        #错误达到3次后,退出输入状态，返回上个模块
                        count = count + 1
                        if count == 3:
                            print("输入已经连续错误3次,请重新选择!\n")
                            break
                        else:
                            mylog.error("输入信息有误 %s", e)
                            print("输入信息有误,请重新输入!\n")
            #如果选择3,走删除模块
            elif number == 3:
                count=0
                while True:
                    # noinspection PyBroadException
                    try:
                        userId=int(input("输入要删除信息的id:"))
                        # noinspection PyCallByClass
                        Mydb.MysqldbHelper.delop(Mydb.MysqldbHelper,userId)
                        # 修改执行完成后,退出修改模块
                        break
                    except Exception as e:
                        # 错误达到3次后,退出输入状态，返回上个模块
                        count = count + 1
                        if count == 3:
                            print("输入已经连续错误3次,请重新选择!\n")
                            break
                        else:
                            mylog.error("输入信息有误 %s", e)
                            print("输入信息有误,请重新输入!")
            elif number == 4:
                break #这里必须先退出循环后再退出cmd
                client.do_exit()
                client.cmdloop()
            else:print("选择有误,请重新选择!")
        except Exception as e:

            mylog.error("选择信息有误 %s",e)
            print("选择有误,请重新选择!")
os.system("pause")