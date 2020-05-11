import decimal
from common.handle_db import HandleDB
from common.myconfig import conf




db = HandleDB()


sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone="{}"'
phone = conf.get_str("test_data",'user')


#  格式化sql语句
s_amount = db.get_one(sql.format(phone))[0]

amount = 100.1
#  将浮点数转换为decimal类型的数据，记得转换之前先转换为字符串（不然浮点数会有精度问题）
amount = decimal.Decimal(str(amount))

# print(amount,type(amount))
#
# print(s_amount+amount)
#
# print(type(amount))
