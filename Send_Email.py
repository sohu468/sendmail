# coding=utf-8
import smtplib, sys
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime

sender = "chicagohood2018@163.com"
receivers = ['enkun.zhang@externals.adidas.com', 
             'Baozhen.Wang@externals.adidas.com', 'Hans.Zuo@externals.adidas.com', 'Larry.Wu@externals.adidas.com',
             'Nancy.Du@externals.adidas.com', 'Felix.Wang@externals.adidas.com','Lin.Li@externals.adidas.com','shelly.huang@externals.adidas.com',
             'Wenying.Lu@externals.adidas.com','Cheney.You@externals.adidas.com', 'Annie.Chen2@adidas.com', 
             'June.Chen@adidas.com','Duo.Chen@adidas.com', 'Leon.Lee@adidas.com']
cc_receivers = ['nataliya.kolosov@adidas.com', 'Kevin.Fan@adidas.com']
receiver = receivers + cc_receivers


def sendEmail(argv):
    mail_host = "smtp.163.com"
    mail_user = "chicagohood2018"
    mail_pass = argv[1]

    title = 'Daily SSI Performance Smoke'
    date = str(datetime.datetime.now().month) + '/' + str(datetime.datetime.now().day)
    content = """<pre> 
    Hi Team,

    PFB SSI daily smoke and performance test report of %s in beta env:
        SSI Performance Test: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/SSI_Performance/HTML_20Report/">Performance Report</a>
        SSI batchAdd Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_beta/job/SSI_batchAdd_smoke_pipeline/Postman_20HTML_20Results/">batchAdd_Smoke_Report</a>
        SSI Personalized Product Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_beta/job/SSI_personalized_product_smoke_pipeline/Postman_20HTML_20Results/">Personalized_Product_Smoke_Report</a>
        SSI Personalized buyNow Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_beta/job/SSI_personlized_buyNow_smoke_pipeline/Postman_20HTML_20Results/">Personalized_buyNow_Smoke_Report</a>
        SSI Regular buyNow Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_beta/job/SSI_regular_buyNow_smoke_pipeline/Postman_20HTML_20Results/">Regular_buyNow_Smoke_Report</a>
        SSI Regular Product Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_beta/job/SSI_regular_product_smoke_pipeline/Postman_20HTML_20Results/">Regular_Product_Smoke_Report</a>
    
    PFB SSI daily smoke report of %s in staging env:
        SSI batchAdd Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_staging/job/SSI_batchAdd_smoke_pipeline/Postman_20HTML_20Results/">batchAdd_Smoke_Report</a>
        SSI Personalized Product Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_staging/job/SSI_personalized_product_smoke_pipeline/Postman_20HTML_20Results/">Personalized_Product_Smoke_Report</a>
        SSI Personalized buyNow Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_staging/job/SSI_personlized_buyNow_smoke_pipeline/Postman_20HTML_20Results/">Personalized_buyNow_Smoke_Report</a>
        SSI Regular buyNow Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_staging/job/SSI_regular_buyNow_smoke_pipeline/Postman_20HTML_20Results/">Regular_buyNow_Smoke_Report</a>
        SSI Regular Product Smoke: <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/job/test_automation_staging/job/SSI_regular_product_smoke_pipeline/Postman_20HTML_20Results/">Regular_Product_Smoke_Report</a>
 
    Please check <a href="https://jenkins.tools.adidas.com.cn/nite/job/test-automation/">DIT Jenkins</a> for more details.


    Thanks,
    DIT QA
    </pre>""" % (date, date)

    message = MIMEText(content, 'html')
    message['From'] = formataddr((str(Header('DIT QA', 'utf-8')), sender))
    message['To'] = ",".join(receivers)
    message['Cc'] = ",".join(cc_receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("mail has been send successfully.")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail(sys.argv)
