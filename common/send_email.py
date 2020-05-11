import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




def send_msg(file_path):

    # 第一步： 连接到smtp服务器
    smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
    smtp.login("379923145@qq.com","algmmzptupjccbab")

    # 第二步：构建邮件
    smg = MIMEMultipart()

    text_smg = MIMEText(open(file_path,'r',encoding='utf8').read(),"html")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path,"rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='report.html')
    smg.attach(file_msg)

    smg["Subject"] = "接口测试报告"
    smg["From"] = "379923145@qq.com"
    smg["To"] = "1206348259@qq.com"

    # 第三步发送邮件
    smtp.send_message(smg,from_addr="379923145@qq.com",to_addrs="1206348259@qq.com")

