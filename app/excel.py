#coding=utf8 
from openpyxl import Workbook
from openpyxl.compat import range
import pymysql
import time

while True:
    try:
        conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='conference',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from wechat")
        result = cur.fetchall()

        cur.close()
        conn.close()
    except:
        print 'access database wrong'
        time.sleep(30)
        continue

    def journey(n):
        if n == 1:
            return u'飞机'
        elif n == 2:
            return u'火车'
        elif n == 3:
            return u'其他'
        else:
            return u''

    def visit(n):
        if n == 1:
            return u'上午参观'
        elif n == 2:
            return u'下午参观'
        elif n == 3:
            return u'上午下午都参观'
        elif n == 4:
            return u'暂不确定是否参加'
        else:
            return u''

    result = [list(x) for x in result]
    for i in result:
        i[7] = journey(i[7])
        i[10] = journey(i[10])
        i[-1] = visit(i[-1])

    wb = Workbook()
    dest_filename = '/home/ubuntu/www/conference/conference.xlsx'
    ws1 = wb.active
    ws1.title = "data"
    info=[u'数据库存储序号',u'学校',u'单位',u'姓名',u'职务',u'电话号码',u'电子邮箱',u'到达方式',u'预计到达时间',u'订单号',u'离开方式',u'离开订单号',u'离开时间',u'发票邮寄地址',u'11月6日参观活动']
    i = 0
    ws1.append(info)
    for row in range(2,len(result)+2):
        ws1.append(result[i])
        i += 1

    wb.save(filename=dest_filename)
    time.sleep(30)
