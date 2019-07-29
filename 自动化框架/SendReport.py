import smtplib
from email.mime.text import MIMEText

mail_host ="mail.iapppay.com"  #设置服务器
mail_user = "xiangkaizheng@iapppay.com"   #用户名
mail_pass ="iapppay002"   #口令
mail_postfix = "163.com"   #发件箱的后缀

# to_list:收件人； sub:主题； content：邮件内容

def send_mail(to_list,sub,reportpath):
    file = open(reportpath,"rb") #通过二进制方式打开文件的
    bcontent = file.readlines()   #读取到的文件的内容是以字节形式存储的
    file.close()
    content = ""
    for line in bcontent:#读取到的文件的内容是以字节形式存储的
        sline = str(line,encoding='utf-8')  #将字节类型的内容转换为字符串
        content = content + sline   #将读取的内容拼接成邮件正文内容
    # print("content:%s" % content)

    #这里的hello可以任意设置，收到信后，将按照设置显示
    me = "TestCenter" + "<" +mail_user + ">"
    #创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    #设置主题
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)   #连接smtp服务器
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())   #发送邮件
        s.close()
        print("邮件发送成功.")
        return True
    except Exception as e:
        print("发送失败，失败原因:%s." % e)
        return False

if __name__ =="__main__":
    #发送测试报告
    send_mail(["xiangkaizheng@iapppay.com"],"TestResult",r"D:\Users\Administrator\PycharmProjects\mswt\自动化框架\report\1.txt")
