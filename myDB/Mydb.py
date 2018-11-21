# -*- coding: UTF-8 -*-
import json
import MySQLdb

import md_config
import md_logger
dbHost = md_config.getConfigDb('dbhost')
dbName = md_config.getConfigDb('dbname')
dbuser = md_config.getConfigDb('dbuser')
dbPasswd = md_config.getConfigDb('dbpasswd')
#这里要注意一下,port是int类型,否则会出错
dbPort = int(md_config.getConfigDb('dbport'))
dbCharset = md_config.getConfigDb('dbcharset')
#调用日志函数
mylog=md_logger.logger()
# noinspection PyGlobalUndefined
class MysqldbHelper:
    # 获取数据库连接
    @staticmethod
    def getCon():
        try:
            conn = MySQLdb.connect(host=dbHost,
                                   user=dbuser,
                                   passwd=dbPasswd,
                                   db=dbName,
                                   port=dbPort,
                                   charset=dbCharset,)
            mylog.info("数据库连接成功 %s",conn.info())
        except MySQLdb.Error as e:
            mylog.error("MysqldbError:%s" %e)
            print("MysqldbError:%s" % e)
            #conn=False
            # 查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典
        return conn
    #执行sql，执行成功返回True,否则返回False
    def select(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor(MySQLdb.cursors.DictCursor)
            count=cur.execute(sql)
            if count>0:
                fc = cur.fetchall()
            else:
                fc=False
        except MySQLdb.Error as e:
            fc=False
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
            # 带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
        return fc

    def updateByParam(self, sql, params):
        count=0
        try:
            conn = self.getCon
            cursor = conn.cursor()
            count=cursor.execute(sql, params)
            conn.commit()
        except MySQLdb.Error as e:
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
        return count

    def update(self, sql):
        global connU
        try:
            connU = self.getCon()
            cursorU = connU.cursor()
            cursorU.execute(sql)
            connU.commit()
            count = 1
        except MySQLdb.Error as e:
            connU.rollback()
            mylog.error("Mysqldb Error:%s" % e)
            print("Mysqldb Error:%s" % e)
            count = 0
        return count
    #下面是具体封装的sql语句方法
    #根据userId查询数据
    def queryId(self, userId):
        global musicId
        musicSql = "select id from main_app_appmanager where name='music%s'" % userId
        fc = self.select(self,musicSql)
        if  fc is False:
            print("您查询的数据不存在!")
        else:
            print("查询成功!")
            for row in fc:
                musicId = row.get('id')
        musicSet1 = "SELECT * FROM main_app_configcenter WHERE app_id=%s" % musicId
        fc = self.select(self, musicSet1)
        if  fc is False:
            print("您查询的数据不存在!")
        else:
            print("查询成功!")
            for row in fc:
                print(row)


    # 根据手机号查询数据
    def queryPhone(self, phone):

        queryPh = "select * from music_theme where order_num=%s" % phone
        fc = self.select(self, queryPh)
        if fc is False:
            print("您查询的数据不存在!")
        else:
            print("查询成功!")
            for row in fc:
                # print(row["id"])
                print(row)
    def ins(self):
        sql = "insert into pythontest values(5,'数据结构','this is a big book',now())"
        count = self.update(sql)
        print(count)

    def insparam(self):
        sql = "insert into pythontest values(%s,%s,%s,now())"
        params = (6, 'C#', 'good book')
        self.updateByParam(sql, params)

    def delop(self, userId):
        qyId = "select * from music_theme where id=%s" % userId
        fc = self.select(self, qyId)
        if fc is False:
            print("数据库中没有查询到该id数据!")
        else:
            sql = "delete from music_theme where id=%s" % userId
            count = self.update(self,sql)
            if count>0:
                print("数据删除成功!")
            else:print("数据删除失败!")

    # noinspection PyAssignmentToLoopOrWithParameter
    '''
    apkVersion
    '''
    def change(self, apkVersion ,numId):

        #先在main_app_appmanager数据表中查询到该包对应的app_id
        global app_id,count1
        apk_Id_Sql = "select id,identifier from main_app_appmanager where name='music%s'" % apkVersion
        #apk_identifier_Sql = "select identifier from main_app_appmanager where name='music%s'" % apkVersion
        ft = self.select(self, apk_Id_Sql)
        if ft is False:
            print("数据库中没有查询到该id数据!")
        else:
            print("数据库中存在该信息!正在修改中.......")
            for row in ft:
                apk_Id = int(row.get('id'))
                apk_identifier = row.get('identifier')

            #根据app_Id在main_app_configcenter表中查询出要修改的对应的具体id
            config_Id_Sql = "SELECT id FROM main_app_configcenter WHERE app_id=%s" % apk_Id
            # 根据apk_identifier在ads_sdk表中查询出要修改的对应的app_name
            update_Sdk_Sql = "update ads_sdk set version=1,`interval`=5,intervall=5,pone=100,ponel=100,home=100," \
                             "homel=100,ptwo=100,ptwol=100,pthr=80,pthrl=80 where app_name='%s'" % apk_identifier
            '''
            **先修改config配置里面的信息,修改完成后再去修改sdk广告的配置信息         
            '''
            fc = self.select(self, config_Id_Sql)
            if fc is False:
                print("您查询的数据不存在!")
            else:
                for row in fc:

                    select_Id = "SELECT * FROM main_app_configcenter WHERE id=%s" % int(row['id'])
                    ft = self.select(self, select_Id)
                    if ft is False:
                        print("您查询的数据不存在!")
                    else:
                        # noinspection PyAssignmentToLoopOrWithParameter
                        for row in ft:
                            if row['key'] == 'sheild':
                                MysqldbHelper.update_json_value(row['id'],json.loads(row['value']), numId)

                            elif row['key'] == 'update':
                                MysqldbHelper.update_json_value(row['id'], json.loads(row['value']), numId)

                            elif row['key'] == 'play':
                                MysqldbHelper.update_json_value(row['id'], json.loads(row['value']), numId)

                            elif row['key'] == 'apps':
                                MysqldbHelper.update_json_value(row['id'], json.loads(row['value']), numId)

                            elif row['key'] == 'ratings':
                                MysqldbHelper.update_json_value(row['id'], json.loads(row['value']), numId)
                print('config配置修改完成!')
                count1 = MysqldbHelper.update(MysqldbHelper, update_Sdk_Sql)
                if count1 > 0:
                    print('sdk广告的配置更新成功!')
                else:
                    print('sdk广告的配置更新失败!')



    dic = {}
    @staticmethod
    def json_txt(dic_json):
        if isinstance(dic_json,dict):
            for key in dic_json:
                print('key的值是:', key)
                print('dic_json[key]001的值是:', dic_json[key])
                if isinstance(dic_json[key],dict):
                    #print("****key001--：%s value--: %s" % (key, dic_json[key]))
                    print('dic_json[key]的值是:', dic_json[key])
                    MysqldbHelper.json_txt(dic_json[key])
                    #dic[key] = dic_json[key]
                else:
                    print("****key--：%s value--: %s" % (key, dic_json[key]))
                    #dic[key] = dic_json[key]

    # noinspection PyCallByClass
    '''
    keyId:要修改数据的id
    dic_json:该id数据的的vaule值
    numId:要增加的版本号
    '''

    # noinspection PyUnreachableCode,PyCallByClass
    @staticmethod
    def update_json_value(keyId,dic_json, numId):
        global count1
        if isinstance(dic_json, dict):
            for key in dic_json:
                    isExist = False
                    if isinstance(dic_json[key], dict):
                        MysqldbHelper.update_json_value(keyId,dic_json[key],numId)
                    elif key == 'organic_versions':

                        for num in dic_json[key]:
                            #当配置中已经改版本号,提示已存在
                            if numId == int(num):
                                isExist = True
                        if isExist:
                            continue
                        else:
                            #sheild的value更新前,保存到dic_old,更新后,再恢复,不然程序无法走下去
                            dic_old = dic_json
                            dic_json[key].append(numId)
                            #将dict转换成Json,并拼接成整个value的值
                            dic_json = '{"data":' + json.dumps(dic_json) + '}'
                            sheild_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper,sheild_Sql)
                            if count1 > 0:
                                dic_json = dic_old
                            else:print('sheild配置中的organic_versions的值更新失败!')
                    elif key == 'non_organic_versions':
                        for num in dic_json[key]:
                            #当配置中已经改版本号,提示已存在
                            if numId == int(num):
                                isExist = True
                        if isExist:
                            break
                        else:
                            dic_old = dic_json
                            dic_json[key].append(numId)
                            #将dict转换成Json,并拼接成整个value的值
                            dic_json = '{"data":' + json.dumps(dic_json) + '}'
                            sheild_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper,sheild_Sql)
                            if count1 > 0:
                                dic_json = dic_old
                            else:print('sheild配置中的non_organic_versions的值更新失败!')
                    elif key == 'mild_version':

                        numId = str(numId)
                        if dic_json[key] == numId:
                            break
                        else:
                            dic_json[key] = numId
                            dic_json='{"data":'+json.dumps(dic_json)+'}'
                            update_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper, update_Sql.replace(r'\r\n',r'\\r\\n'))
                            if count1 > 0:
                                break
                            else:
                                print('update的值更新失败!')
                        break
                    elif key == 'inapp_play':

                        for num in dic_json[key]:
                            #当配置中已经改版本号,提示已存在
                            if numId == int(num):
                                isExist = True
                        if isExist:
                            break

                        else:
                            dic_json[key].append(numId)
                            #将dict转换成Json,并拼接成整个value的值
                            dic_json = '{"data":' + json.dumps(dic_json) + '}'
                            play_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper,play_Sql)
                            if count1 > 0:
                                break
                            else:print('play配置中的inapp_play值更新失败!')

                    elif key == 'data':
                        #如果已默认无屏蔽,就直接退出该次操作
                        if dic_json[key] == [""]:
                            break
                        else:
                            dic_json[key] = [""]
                            #将dict转换成Json,并拼接成整个value的值
                            dic_json = json.dumps(dic_json)
                            play_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper,play_Sql)
                            if count1 > 0:
                                break
                            else:print('apps配置的值更新失败!')
                    elif key == 'show_rate':

                        dic_old = dic_json
                        #如果该配置已打开,就直接进入下一次循环判断
                        if dic_json[key]:
                            continue
                        else:
                            dic_json[key] = True
                            dic_json = '{"data":' + json.dumps(dic_json) + '}'
                            update_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper, update_Sql.replace(r'\r\n', r'\\r\\n'))
                            if count1 > 0:
                                dic_json = dic_old
                            else:
                                print('show_rate的值的值更新失败!')

                    elif key == 'ratings_switch':

                        if dic_json[key] == 1:
                            break
                        else:
                            dic_json[key] = 1
                            dic_json = '{"data":' + json.dumps(dic_json) + '}'
                            update_Sql = "update main_app_configcenter set value='%s' where id=%s" % (
                                dic_json, keyId)
                            # noinspection PyTypeChecker
                            count1 = MysqldbHelper.update(MysqldbHelper, update_Sql.replace(r'\r\n', r'\\r\\n'))
                            if count1 > 0:
                                break
                            else:
                                print('ratings_switch的值更新失败!')
        else:
            print("请输入正确的dic信息",dic_json)
