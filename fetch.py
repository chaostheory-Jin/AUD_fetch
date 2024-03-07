import requests
from bs4 import BeautifulSoup
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender = 'zzz@outlook.com'
    receiver = 'zzz@zzz.com'
    password = 'zzzz'
    smtp_server = 'smtp-mail.outlook.com'
    port = 587  # SMTP端口号，根据您的邮件服务商可能不同

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    body = MIMEText(body, 'plain')
    msg.attach(body)

    # 连接到SMTP服务器并发送邮件
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # 启动TLS加密
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

def check_and_alert(threshold, exchange_rate_p):
    exchange_rate = exchange_rate_p  # 假设这返回一个浮点数表示的汇率
    if exchange_rate < threshold:
        subject = "汇率提醒"
        body = f"当前汇率已低于{threshold}，当前值为：{exchange_rate}"
        send_email(subject, body)
        print("提醒邮件已发送。")
    else:
        print("汇率正常，无需发送提醒。")


def fetch_exchange_rate():
    url = "https://www.google.com/finance/quote/AUD-CNY?sa=X&ved=2ahUKEwj62_7yuNyEAxWNzDgGHVD_AgcQmY0JegQIARAk"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # This is a placeholder for the actual selector needed to find the exchange rate on the page.
    # You'll need to inspect the webpage to find the correct selector for the exchange rate data.
    exchange_rate_element = soup.find(class_ = "YMlKec fxKbKc")
    exchange_rate = exchange_rate_element.text.strip()  # Assuming the data you need is in text form
    threshold = 4.5
    #print("tag")
    check_and_alert(threshold, float(exchange_rate))
    print(f"Current exchange rate: {exchange_rate}")

def job():
    print("Fetching the current exchange rate...")
    fetch_exchange_rate()

# Schedule the job every hour
schedule.every().hours.do(job)
# 设置汇率阈值，例如，当汇率低于4.5时发送提醒
#threshold = 4.5
#check_and_alert(threshold)

print("Exchange rate fetcher started. Press Ctrl+C to stop.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Exchange rate fetcher stopped.")

