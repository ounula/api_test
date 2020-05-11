import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




# 第一步： 连接到smtp服务器
smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login("musen_nmb@qq.com","algmmzptupjccbab")

# 第二步：构建邮件
smg = MIMEMultipart()

text_smg = MIMEText("这是邮件文本内容","plain","utf8")
smg.attach(text_smg)

file_msg = MIMEApplication(open(r"C:\project\py24_class\py24_api_test\reports\report.html","rb").read())
file_msg.add_header('content-disposition', 'attachment', filename='report.html')
smg.attach(file_msg)

smg["Subject"] = "报告"
smg["From"] = "379923145@qq.com"
smg["To"] = "1206348259@163.com"

# 第三步发送邮件
smtp.send_message(smg,from_addr="musen_nmb@qq.com",to_addrs="musen_nbm@163.com")

